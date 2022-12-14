"""
處理交握驗證
"""
import socket
import iota_client
import rsa
import base64
import json
import ipfshttpclient
import RSA_key_operation
import iota_operation
import time
LOCAL_NODE_URL = "http://192.168.0.160:14265"
iota_msg_id="3b58be5fa918c15147fe0b41de10198929154c8b8db761b39b3413af1692ed1b"

#ipfs_cert_cim_test="QmQDXnom85YxSxjM68pyfbhjcY6Exxe8fZWNKHNpttgPxc"
#SEED = "e8300375bd1a31ea4566d7a6fadcad42bb48122b283b5fbd981e9088c7e98095"
#client = iota_client.Client(nodes_name_password=[[LOCAL_NODE_URL]], node_sync_disabled=True)

class CR_client:
    def __init__(self):
        self.HOST = '192.168.0.104'
        self.PORT = 8000 
        self.clientMessage = 'Hello!'


    #socket連線，交握時記得到證書的transparency上鏈資鏈
    def socket(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.HOST, self.PORT))
            sock.send(iota_msg_id.encode())#傳iota地址
            sock.close()

if __name__ == "__main__":
    CR_client=CR_client()
    CR_client.socket()#socket連線&驗證

    
       
    



