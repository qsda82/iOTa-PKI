"""
執行證書撤銷
"""
import RSA_key_operation
import iota_operation

cert_index=""
pubkey=RSA_key_operation.get_pubkey()
cert=iota_operation.cert(id_get(),pubkey,True,"Sha256WithRSAEncryption")
iota_operation.upload_msg(cert_index,cert)

def id_get():
    cid=iota_operation.msg_index_info(cert_index)
    cert=iota_operation.msg_raw(cid[0])
    j=json.loads(cert)
    return str(j["certificate"]["ID"])