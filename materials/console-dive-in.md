### console.py

#### 解說

```
console.py 中有一 class, Console。
此 class 中共有
parse, keywords, stop, start
四個函式。

初始化 instance 時，會先將 
self.active = True 
設定 active flag 為真

且將 self.cmd = Commands()
初始化 Commands() 的 instance
並指派給 self.cmd

接下來針對每個函式一一解說

首先是 parse()
傳入參數為 data，即為使用者在 console中輸入之字串
parse 中
root 表示為指令本身
args 表示為指令參數

用 data.split() 以空白為區隔，將 data 切割成 list。
list 中第 0 個 item 即表示 root。
剩下的就是參數。

parse 處理完後，回傳 root 及 args。

第二個函式是 keywords()
傳入參數也是 data。

主要用來檢查現在是否有 session opened
檢查方法為，看 data 中有無關鍵字 $self。

若有，則再檢查 __session__.is_set()
session 是否有開。
若有，則將 $self 取代為 __session__.file.path 檔案路徑
否則，印出 "No session opened"

最後再 return data。

第三個函式是 stop()
功能只有一個
將 self.active 的 flag 改成 False。

最後一個是 start()

```
