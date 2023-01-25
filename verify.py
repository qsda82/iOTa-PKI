import RSA_key_operation
import json
import datetime
import iota_operation
#至iota取得公鑰並做成公鑰檔
def make_pk(j):
    pk_text=str(j["certificate"]["Public Key Value"] )
    public_pem_prefix = '-----BEGIN PUBLIC KEY-----'
    public_pem_suffix = '-----END PUBLIC KEY-----'
    #pk=base64.b64encode(a.decode())
    public_key = '{}{}{}'.format(public_pem_prefix, pk_text, public_pem_suffix)
    #print(public_key)
    #key = RSA.import_key(public_key)
    return public_key
#驗證是否過期
def validity_verify(j):
    timenow = datetime.datetime.today()
    after=datetime.datetime.strptime(j["certificate"]["Validity"]["Not After"],'%b %d %H:%M:%S %Y GMT')
    if timenow<after :
        return 1
    else:
        return 0
#驗證是否撤銷
def revocation_verify(j):
    revocation=str(j["certificate"]["Revocation"])
    if revocation=="False" :
        return 1
    else:
        return 0
#驗證使用次數
def useage_verify(j,useage_times):
    Transparnecy_list=iota_operation.msg_index_info(j["certificate"]["Transparnecy"])
    if len(Transparnecy_list) >= useage_times:
        return 1
    else:
        return 0
#取得新的證書
def cert_up_to_date(index):
    cid_list=iota_operation.msg_index_info(index)
    time_list=[]
    for i in cid_list:
        cert_json=iota_operation.msg_raw(i)#取得證書內容
        j=json.loads(cert_json)
        time=datetime.datetime.strptime(j["certificate"]["Validity"]["Not Before"],'%b %d %H:%M:%S %Y GMT')
        time_list.append(time)
    for i in range(len(time_list)):
        if time_list[i] == max(time_list):
            return cid_list[i]
    return 0
    
#證書驗證
def cert_verify(cid,useage_times):
    index=iota_operation.msg_get_index(cid)#根據cid取得其index
    newest_cid=cert_up_to_date(index)#根據index取得最新的cid值
    if newest_cid == cid:#檢查證書鏈是否為最新的證書
        cert_json=iota_operation.msg_raw(cid)#取得證書內容
        j=json.loads(cert_json)#將證書存為json檔
        print(j)
        pubkey=make_pk(j)#製作成公鑰檔
        message = json.dumps(j["certificate"]).encode('utf-8')#取得證書簽章
        sign=RSA_key_operation.sign_verify(message,bytes.fromhex(j["Signature"]["Sign"]),pubkey)#簽章驗證
        validity=validity_verify(j)#時效驗證
        revocation=revocation_verify(j)#撤銷驗證
        useage=useage_verify(j,useage_times)#使用次數驗證
        if sign==1 and validity==1 and revocation==1 and useage==1:
            iota_operation.upload_msg(j["certificate"]["Transparnecy"],iota_operation.transparnecy())#驗證完成後，要將使用紀錄上鏈做透明化證明(Transparnecy)
            return 1
        else:
            return 0
    else:
        return 0
