### session.py

#### 解說

```
line 29，初始化 instance。
其他程式便可 from session import __session__
直接用 __session__ 這個 instance。

接著看類別 Session
類別初始化時會定義兩個變數 self.file 以及 self.plugin。
兩者都設定為 None。

類別函式中，

set() 主要用來開啟 session。
並用 objects 中的 File 類別，協助計算 file hash 等資訊。

is_set() 用來檢查使用者當前是否在某個 session 中。

clear() 則用來關掉 session。
實際就是把 self.plugin 及 self.file 再度變為 None
```
