"""
處理金鑰建立與簽章驗證
"""

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import pem
PUBLIC_KEY_PATH = '/home/qsda82/client/noca_tls/keys/pubkey.pem'  # 公鑰
PRIVATE_KEY_PATH = '/home/qsda82/client/noca_tls/keys/prikey.pem'  # 私鑰

#建立私鑰
def key_pair_generate(): 

    #start = time.time()     
    #建立私鑰 
    key = RSA.generate(1024)
    f = open(PRIVATE_KEY_PATH,'wb')
    f.write(key.export_key('PEM'))
    f.close()
    
    #建立公鑰
    public_key = key.public_key()
    f = open(PUBLIC_KEY_PATH,'wb')
    f.write(public_key.export_key(format='PEM'))
    f.close()
    #end = time.time()
    #print("執行時間：%f 秒" % (end - start)) 

#取得公鑰，return公鑰(string)
def get_pubkey():
    certs = pem.parse_file(PUBLIC_KEY_PATH)
    pubkey=str(certs[0]).split('-----')
    #certs=str(certs[0]).split('\n')
    #pubkey=""
    #for i in range(1,len(certs)-1):
        #pubkey=pubkey+certs[i]
    #print(pubkey)
    return pubkey[2]

#簽章：return簽章，參數：欲傳送內容(byte)
def sign(message):
    #message = b'To be signed'
    key = RSA.import_key(open(PRIVATE_KEY_PATH).read())
    h = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(h)
    return signature

#驗證簽章：return驗證結果，參數：欲傳送內容(byte)
def sign_verify(message,signature,pubkey):
    h = SHA256.new(message)
    try:
        pkcs1_15.new(pubkey).verify(h, signature)
        return "Verify OK" 
    except (ValueError, TypeError):                                 
        return "Verify Fail" 
