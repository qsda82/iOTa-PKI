"""
執行證書更新
"""
import RSA_key_operation
import iota_operation

#取得公鑰
pubkey=RSA_key_operation.get_pubkey()
#建立憑證
timenow = datetime.datetime.today()
timenow =  timenow.strftime("%b%d%I%M%S%Y")
id=bytes(pubkey, 'utf-8').hex()+timenow
cert=iota_operation.cert(str(id),pubkey,False,"Sha256WithRSAEncryption")
#print(cert)

#上鏈
index=hashlib.md5(pubkey.encode('utf-8')).hexdigest()#把pubkey用md5 hash做成index
iota_operation.upload_msg(index,cert)#將憑證上鏈
