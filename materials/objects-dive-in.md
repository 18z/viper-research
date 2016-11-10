### objects.py

#### 解說

```
objects.py 中有兩個 class。

Singleton 以及 File

先看 File。

File 繼承自 object 類別。
在類別產生 instance 時，初始化會設定基本變數欄位
例如：path, name, size, type, md5, sha1, sha256, sha512, crc32, ssdeep。
其中 path 在初始化時就會給定， size (file size) 一開始設定為零。
其餘變數皆設定為空字串。

在初始化時，會用到類別函式 is_valid() 檢查下列事項：

1. os.path.exists(self.path)
  檢查檔案路徑是否存在
2. as.path.isfile(self.path)
  檢查是否為檔案
3. os.path.getsize(self.path) != 0
  檢查檔案大小是否為零
  
is_valid() 將檢查過程通通塞在 return 中以簡化程式碼。
三者條件都要成立， return 1，若其中一者不成立則 return 0。

若 is_valid() 為 1。
則會將 self.name, self.size, self.type 變數塞入值。
self.name = os.path.basename(self.path)
self.size = os.path.getsize(self.path)
self.type 之值，則是用到類別函式 get_type()取得。

接著執行類別函式 self.get_hashes()
以及填入 self.ssdeep 之值。

self.ssdeep 之值，是用類別函式 get_ssdeep() 取得。

接著來看類別函式 get_type()

作者用了三種方法來取得 file type。
1. 先用 magic-python module 來做。
   https://github.com/mammadori/magic-python
2. 若第一種方法行不通，則用 python-magic 來做。
   https://github.com/ahupp/python-magic
3. 若第二種方法行不通，再用 subprocess 呼叫 file 指令來做。

最後，不管用了哪個方法，都會執行 ms.close()。
這是為了第一個方法所寫。
因此，也用 try except 將 ms.close() 包起來。
若執行失敗(也就是用了第二或第三種方法取得 file_type)，則 pass。

其中需要注意，很多網路上的教學都將 magic-python 與 python-magic 搞混。
因兩者 import 時，都只要寫 import magic。
此狀況導致有 magic-python 使用者去 python-magic 作者 issue 發問。
因此，python-magic 作者親自澄清，兩者是不一樣套件，只是剛好同名。
詳見：https://github.com/ahupp/python-magic/issues/45

接著，利用 get_hashes() 計算各種 file hashes。
get_hashes() 中，首先用 hashlib.md5() 及 hashlib.sh256() 等
初始化 instances。

接者呼叫 get_chunks() 將大檔案切割成 chunks，防止檔案太大無法一次全部放進 memory 中。

get_chunks() 中，每個 chunk 切割大小為 16 * 1024 bits，
且用 yield 確保 chunks 會依序切割下去，而非每次只切割到第一段。
其中，fd.read(16 * 1024) 會切割第一段 chunk，
再執行一次則會切割第二段。

line 69，中 self.get_chunks() 是 generator 型態
用 for 迴圈，將 generator 中的每一個 chunk.next() 依序抓出來。
並用 md5.update(chunk) 將每一段接在一起。

最後，再用 md5.hexdigest()，將接在一起完整檔案，計算 file hash。

```
