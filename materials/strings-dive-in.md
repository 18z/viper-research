### strings.py

#### 解說 

```
class Strings 繼承自 class Module。

class 內只有一個 function, run。

run 被呼叫後，首先用 __session__.is_set() 檢查 session 是否有開啟。
若無，則印出 No session opened。

接著檢查檔案路徑是否存在
若存在，
    則用 open(__session__.file.path, 'r').read() 開檔後讀擋
    若開不起來，則印出 Cannot open file
    
    接著用 re 模組的 findall function，搭配正圭表是式 [\x1f-\x7e]{6,}
    
    [\x1f-\x7e]{6,} 連續六個或以上的 ascii 字元，ascii 字元範圍從 31 - 126
    https://regex101.com/
    
    撈出來後，用 for迴圈將字串一個一個印出來。
```
