
# 關於
#### iOTa-PKI提供一個新型的PKI解決方案，以分散式帳本IOTA為主軸，達到憑證存放與管理的成效，透過iOTa-PKI可以做到：
* 去中心化
* 沒有上傳成本(gas 花費)
* 驗證成本較低
* 免於單點CA所受的危害

# Prerequisites
#### 運行iOTa_PKI必須先安裝：
* IOTA Client Python Library:https://wiki.iota.org/iota.rs/libraries/python/api_reference#api-reference
* PyCryptodome:https://pycryptodome.readthedocs.io/en/latest/src/introduction.html
* Hornet node:https://wiki.iota.org/hornet/welcome

# 執行
#### 需具備兩台載相同網路下的主機，其中一台先執行`server_handshake.py`開啟socket服務
`python server_handshake.py`


#### 另一台執行`client_handshake.py`開啟交握對話

`python client_handshake.py`
# 架構圖
![](https://i.imgur.com/9spGWOE.png)

#### Steps:
1. 建立key pair
2. 根據規定上傳憑證資料
3. 發出對話請求，並提出信任證書數量
4. 回傳iota MessageID
5. 驗證憑證資訊(證書狀態、公鑰、簽章、時效、撤銷、使用次數)
6. 上傳使用紀錄
7. 獲得憑證，可用於TLS交握

# 成果
#### 相較於不同證書鏈長度的憑證，iOTa-PKI具有較低的驗證成本
![](https://i.imgur.com/eOdqKzj.jpg)





