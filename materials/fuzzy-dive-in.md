### fuzzy.py

#### 解說

```
先檢查 pydeep 是否 import 成功，
若有，則 flag HAVE_PYDEEP = True
若無，HAVE_PYDEEP = False

Class Fuzzy 繼承 Module class。

裡面就一個 function run。
run function 被呼叫後，會先用 __session__.is_set() 檢查 session 是否開啟。
若無則印出 No session opened。
接著跳出 run funtion。

接著檢查 HAVE_PYDEEP flag，
若 HAVE_PYDEEP = False，則印出 Missing dependency, install pydeep (`pip install pydeep`)
接著跳出 run function。

再來檢查 __session__.file.ssdeep 是否存在
若無，則印出 No ssdeep hash available for opened file。

通過三層檢查後，則初始化一個 db instance。
透過 db.find(key='all') 撈出所有的樣本。

接著用 for 迴圈進行比對
迴圈內，首先比對 __session_.file.sha256 是否與 sample.sha256 相等，若相等，則繼續迴圈。
也就是說，如果此 session 開啟檔案的 sha256 與資料庫中的樣本相同，則跳過並繼續迴圈。

接著，若 sample.ssdeep 不存在，也直接繼續迴圈下一輪。

迴圈內，通過兩道關卡檢查後，就用 pydeep.compare 比較 __session__.file.ssdeep 與資料庫中樣本的 ssdeep。
最後，印出資料庫中樣本的 sha256 以及比較後的分數。
```
