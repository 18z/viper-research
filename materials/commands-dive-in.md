### commands.py

#### 解說

```
此程式主要功能為定義 viper 系統指令。

有 1 類別 Commands
及 8 類別函式
    cmd_clear, 
    cmd_close, 
    cmd_delete, 
    cmd_find, 
    cmd_help, 
    cmd_info, 
    cmd_open, 
    cmd_store 

類別 instance 初始化時，做兩件事
1. 用 self.db = Database() 開啟與 db 的連線

2. 定義 self.commands
self.commands 是用兩層 巢狀字典組成
字典第一層 key 值是系統指令， value 是第二層字典。
第二層字典內有兩個 item。
    第一個 item 是 obj，對應到類別函式，
    第二個 item 是 description，即描述指令功能之文字

因此 console.py 只要呼叫 self.cmd.commands[第一層(指令)][第二層(obj)]()
就可執行 viper 系統函式。

接下來逐一看類別函式。

1. cmd_clear()
此函式用 os.system('clear') 清除 shell 上訊息。

2. cmd_help()
此函式會印出 help 訊息，即系統指令與模組指令。
首先印出 Commands
並用迴圈 將 commands 中 items 抓出來，

所以 command_name 就是 key (指令), command_item 就是 value(obj 與 description)。
隨後將 key 與 value 塞進 list
再將此 list 塞進 rows (也是個 list)

接著用 prettytable 的 table 將系統指令以表格印出。

同樣的方法運用至將模組指令與描述以 table 印出。
(plugins.py 中， line 30 將模組指令以與系統指令相同之巢狀字典方式，組成)


3. cmd_open
此函式首先接收 *args，不定參數，也就是可以接參數，但參數數量不限。
函式中，定義了兩個函式 usage() 與 help()
usage() 印出 open 使用方法簡單說明
help() 中印出方法簡單說明與參數詳細說明

接者用 getopt 開始 parse 參數
getopt 回傳兩 item。
1. opts
2. argv

opts 是個 list of (option, value)
argv 是其他沒被定義到的參數值 list

用 try 來 parse 參數
若執行失敗，則 raise getopt.GetoptError 
接著再印出 usage()
再 return，結束 cmd_open

接下來設定 is_file變數，預設是 False

再來用迴圈處理 opts
主要將 option 拿出來，看到底是 -h 還是 -f
若是 -h，則印出 help()後直接 return 結束 cmd_open
若是 -f 則將 is_file 改為 True

接著變檢查 argv，也就是沒被定義的參數 list 長度是否為零
如果是零，則表示 -f 後面沒有接檔案路徑。
所以印出 usage()後，接 return 結束 cmd_open
若 argv 長度非零，則將 list 中第一個 item 抓為檔案位置，也就是 target。

接著，檢查 is_file flag 是否為 True，
若是，則用 os.path.expanduser() 處理 target 路徑，主要功能是將 ~ replace 成 $HOME。
接著用 os.path.exists() 檢查路徑是否存在，以及使用 os.path.isfile()檢查是否為檔案。
若不存在或不是檔案，則印出 File not found 錯誤訊息

若存在，則用 __session__.set() 開啟 session。

若 is_file flag 為 False
則用 .strip().lower() 方法將 argv[0] 先以空白為區隔丟進 list，再將 list 裡面字串通通轉為小寫。
接著用 get_sample_path，取得檔案路徑
若路徑 (path) 不是空的
則用 __session__.set() 開啟 session。
```
