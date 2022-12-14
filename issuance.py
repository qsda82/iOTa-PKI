"""
有新證書要發布時使用
"""
import RSA_key_operation
import iota_operation
import datetime
import hashlib
import time
#建立公私鑰
RSA_key_operation.key_pair_generate()
pubkey=RSA_key_operation.get_pubkey()

#建立憑證
timenow = datetime.datetime.today()
timenow =  timenow.strftime("%b%d%I%M%S%Y")
id=bytes(pubkey, 'utf-8').hex()+timenow
cert=iota_operation.cert(str(id),pubkey,False,"Sha256WithRSAEncryption")
#print(cert)

#上鏈
index=hashlib.md5(pubkey.encode('utf-8')).hexdigest()#把pubkey用md5 hash做成index
start = time.time() 
iota_operation.upload_msg(index,cert)#將憑證上鏈
end = time.time()
total_time=(end - start)
print(total_time)