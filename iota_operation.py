"""
處理iota相關作業
"""
import iota_client
import ipfshttpclient
import os
import random,string
import json
import requests
import codecs
from time import gmtime, strftime
import datetime
import hashlib
import RSA_key_operation
LOCAL_NODE_URL = "http://192.168.0.160:14265"
kevin="https://kevintw.nchu.edu.tw/"
client = iota_client.Client(nodes_name_password=[[LOCAL_NODE_URL]], node_sync_disabled=True)
SEED = "e8300375bd1a31ea4566d7a6fadcad42bb48122b283b5fbd981e9088c7e98095"
cid_example="17847f4ba82a2ee64710ca23448214cb5de579676b08beddaa3aa091bd0227f8"


#上鏈，參數：index(string),cert(json)，return：iota_hash(string)
def upload_msg(index,cert):
    print(f'message() Indexation')
    message_id_indexation = client.message(index=index, data_str=cert)#client.message()回傳的是他的message id
    print(f'Indexation sent with message_id: {message_id_indexation}')
    data=json.dumps(message_id_indexation)
    j=json.loads(data)
    iota_hash=str(j["message_id"])
    return iota_hash


#建立憑證，參數：公鑰(string)，return：憑證(json)
def cert(ID,pub_key,revo,algo):
    data={"certificate": 
        {
        "ID": "",
        "Public Key Value": "",
        "Validity": 
            {
            "Not Before": "",
            "Not After": ""
            },
        "Revocation": "",
        "Algorithm":"",
        "Transparnecy":""
        },
        "Signature": {
            "Sign": ""
        }
        }

    time_range = datetime.timedelta(days = 365) 
    timenow = datetime.datetime.today() 
    new_time = timenow + time_range 
    
    timenow =  timenow.strftime("%b %d %I:%M:%S %Y")
    time1year =  new_time.strftime("%b %d %I:%M:%S %Y") 
    data["certificate"]["Validity"]["Not Before"]=str(timenow)+" GMT"
    data["certificate"]["Validity"]["Not After"]=str(time1year)+" GMT"
    data["certificate"]["Public Key Value"]=pub_key
    data["certificate"]["ID"]=ID
    data["certificate"]["Revocation"]=revo
    data["certificate"]["Algorithm"]=algo
    data["certificate"]["Transparnecy"]=''.join(random.sample(string.ascii_letters , 32))
    sign = json.dumps(data["certificate"]).encode('utf-8')
    #print(RSA_key_operation.sign(sign).hex() )
    data["Signature"]["Sign"]=RSA_key_operation.sign(sign).hex()
    cert=json.dumps(data)
    return cert
 
def transparnecy():
    data={"transparnecy": 
        {
        "messageID": "",
        "timestamp": "",
        }
        }
    timenow = datetime.datetime.today()
    timenow =  timenow.strftime("%b %d %I:%M:%S %Y")
    #sign = json.dumps(cert["certificate"]).encode('utf-8')
    data["transparnecy"]["messageID"]=self_cid
    data["transparnecy"]["timestamp"]=str(timenow)+" GMT"
    data=json.dumps(data)
    return data

#用訊息index來回查message id的陣列(可能會有很多筆)        
def msg_index_info(index):
   # print(f"find_messages() for indexation_keys = ['Hi']")
   # messages = client.find_messages(indexation_keys=[index])
   # print(f'Messages: {messages}')
    #return message_id_indexation_queried
    r = requests.get("https://explorer-api.iota.org/search/mainnet/"+index)
    j=json.loads(r.text)
    return j["indexMessageIds"]#回傳list

#根據messageID取得index
def msg_get_index(cid):
    r = requests.get("https://explorer-api.iota.org/search/mainnet/"+cid)
    j=json.loads(r.text)
    binary_str = codecs.decode(j['message']['payload']['index'], "hex")
    message_raw=str(binary_str,'utf-8')
    return message_index

#取得鏈上原始資料
def msg_raw(cid):
    r = requests.get("https://explorer-api.iota.org/search/mainnet/"+cid)
    j=json.loads(r.text)
    binary_str = codecs.decode(j['message']['payload']['data'], "hex")
    message_raw=str(binary_str,'utf-8')
    return message_raw

#取得pubkey，回傳pubkey(string)
def get_pubkey(cid):
    j=json.loads(msg_raw(cid))
    return bytes.fromhex(j["certificate"]["Public Key Value"])

#取得簽章，回傳簽章(bytes)
def get_signature(cid):    
    j=json.loads(msg_raw(cid))
    print(type(bytes.fromhex(j["Signature"]["Sign"])))
#pubkey=RSA_key_operation.get_pubkey()
#print(type(hashlib.md5(pubkey.encode('utf-8')).hexdigest()))
#cert=cert("1","MCowBQYDK2VwAyEAAxeFIctkv3djEcFM7WoQ0q0u7fJf5jzSMze0WpAd3Hc=","RSA") 
#upload_msg("FOBmCeksYlxfEtMdnrIzhJpZujRvDoKG",cert)#上鏈
#key = RSA.import_key(open('CR_pubkey.pem').read())
#print(key)
#j=json.loads(cert)

#sign=j["Signature"]["Sign"]
#print(bytes.fromhex(sign))
#RSA_key_operation.verify(sign)

#cert("789")
    #j=json.loads(tsr_data)
    #pk_text=str(j["certificate"]["Public Key Value"] )
    #print(pk_text)
    #



#將dict存成json
#with open("sample.json", "w") as outfile:
#json.dump(data, outfile)

#tsr_file = open("sample.json", "rb") 

#tsr_data = tsr_file.read()#把檔案讀成byte形式 

