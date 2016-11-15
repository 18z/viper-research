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
首先利用 readline 模組建立 auto-complete 功能。
其中 complete 函式為 completer，可以說實質做出補齊之函式。

complete 中，傳入兩個參數，一為 text，另一為 state。
text 為使用者輸入到一半的字串。
state 為補齊之候選字串 position。

complete 回傳 (glob.glob(text+'*')+[None])[state]
首先看到 glob.glob(text+'*')
glob.glob 作用即是幫忙找出檔名符合特定規則的文件。
例如：目錄下有 1, 123, 223
則 glob.glob('1'+'*')
可幫找出 1, 123 兩檔案。

glob.glob()之回傳值為 list 型態。
因此，glob.glob(text+'*')+[None]就是在 glob 回傳的 list 最後，再加上 None。
用意為 告知 completer 已經沒有符合規則之檔案名稱了。

詳情可看文件解釋
The completer function is called as function(text, state), 
for state in 0, 1, 2, ..., until it returns a non-string value.
參考文獻：https://docs.python.org/2/library/readline.html

最後，comeplete 函式，回傳的是單一符合規則的檔名字串。

```
