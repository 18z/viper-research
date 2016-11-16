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
```
