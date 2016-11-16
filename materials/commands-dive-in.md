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



```
