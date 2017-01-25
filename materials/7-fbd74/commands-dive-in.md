### commands.py

```
line 171 ~ 180
    在 cmd_store() 中新增了刪除原檔參數說明

line 183
    getopt 新增 d 參數
    
line 189
    新增 do_delete flag
    
line 190 ~ 195
    處理參數，並依參數更改 flag
    
line 203
    檔案存入資料庫後，檢查 do_delete flag
    若是，
        則 os.unlink(__session__.file.path)
```
