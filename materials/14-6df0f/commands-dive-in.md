### commands.py

```
line 181
    在 cmd_store() 中的 help() 裡新增 tag 的 help message。

line 184
    store 指令參數處理部份，新增 tag 處理參數
    
line 193
    新增 tags 的 flag
    
line 203 204
    判斷使用者是否給予 -t 或 --tags 參數
        若有
            則將 value (參數值) 給予 tags
            
line 206 
    重構
    將上一版本檔案中 line 203 - 215 之間的程式碼提取功能
    提出 add_file() 功能
        將 obj 利用 store_sample() 儲存在 local 端，並用 new_path 接 store_sample() 回傳的檔案路徑
        檢查 new_path 是否為空值？
            若有
                則將 obj 透過 self.db.add() 存入資料庫
                並印出儲存成功訊息
        檢查是否 do_delete (將原始檔案刪除)
            若有
                則用 os.unlink(obj.path) 刪除
                若發生例外
                    則印出錯誤訊息 Failed deleting file

line 243
    用 add_file() 取代舊有的寫法
```
