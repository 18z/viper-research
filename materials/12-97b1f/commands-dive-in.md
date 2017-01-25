### commands.py

```
line 172 
    cmd_store() 
            usage() message 新增參數說明

line 180
    help() message 新增說明
    
line 184
    getopt 新增處理參數
    
line 191
    新增 folder flag, default == False
    
line 199
    處理參數這塊，新增對 folder flag 的處理

line 202
    檢查 folder 是否存在 與 os.path.isdir(folder) 是否存在
        若存在
        用迴圈把 file_names 從 os.walk(folder) 取出
            用迴圈將單一檔案 file_name 從 file_names 取出
                處理 file_name
                處理路徑
                處理基本資訊(用 File)
                用 store_sample() 取得 new_path
                存入 db
         若不存在
         則用老方法做

line 283
    cmd_find() 修改查詢後結果
    欄位原本有 Name, Type, Size, SHA256
    將 Size 拿掉
```
