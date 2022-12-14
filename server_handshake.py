# -*- coding: utf-8 -*-
import socket
import iota_client
from Crypto.PublicKey import RSA
import json
import random,string
import rsa
import base64
import ipfshttpclient
import secrets
import codecs
import requests
import RSA_key_operation
import verify
import iota_operation
#LOCAL_NODE_URL = "http://192.168.0.160:14265"
#kevin="https://kevintw.nchu.edu.tw/"
#client = iota_client.Client(nodes_name_password=[[LOCAL_NODE_URL]], node_sync_disabled=True)


class CR_server:
    def __init__(self):
        self.HOST = '192.168.0.104'
        self.PORT = 8000
        #self.iota_client=iota_client.Client(nodes_name_password=[[LOCAL_NODE_URL]], node_sync_disabled=True)
   
    #socket設定與連線
    def socket(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#讓ip可以重複使用
        server.bind((self.HOST, self.PORT))
        server.listen(10)
        while True:
            conn, addr = server.accept()
            client_iota_msg_id=str(conn.recv(1024), encoding='utf-8')#接收client傳的iota_msg_id
            print('iota_msg_id:', client_iota_msg_id)#印出接收訊息
            vertication=verify.cert_verify(client_iota_msg_id,5)
            if vertication==1:
                print("verify ok")
            elif vertication==0:
                print("verify fail")
                conn.close()
            
            conn.close()
if __name__ == "__main__":
    CR_server=CR_server()
    CR_server.socket()