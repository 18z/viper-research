### network.py

#### 解說

```
程式邏輯由 function download(url, tor=False) 包起來
  download 內還有一個 function create_connection(address, timeout=None, source_address=None)
  create_connection 是在 tor = True 的情況下用的
  目的是客製化 create_connection 然後 assign 給 socket.create_connection 
  至於為何要這樣做，待未來深度探討。

  line 15 import socket 模組

  line 17 檢查是否 tor flag = True
    若是，則用 socks 及 socket 更改設定

  try:
    line 22 用 urllib2 request url
    line 24 更改 USER AGENT
    line 27 request url 後取得之回傳內容
  except HTTPError
    印出錯誤訊息
  except URLError
    若有用 tor 且 error number 改成 111
      Connection refused, maybe Tor is not running
    否則
      印出錯誤訊息
  except Exception
    其他錯誤就在此印出
  else 要是沒有例外發生時
    return data
```
