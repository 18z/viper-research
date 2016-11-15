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


```
