### Viper tour 

可參考 [Viper LEGO](https://github.com/18z/viper-research/blob/master/materials/lego.md)

1. viper.py -> console.py -> colors.py

 ```
 啟動 viper console 介面，console 介面顯示 prompt 時，會使用不同顏色顯示。
 ```
2. viper.py -> console.py -> session.py -> out.py -> colors.py

 ```
 啟動 viper console 介面時，會先檢查是否有 session 正開啟中，若有則印出 __session__.file.path。
 另外，若輸入 $self 關鍵字時，則會用到函式 keywords 檢查是否有 session 開啟，並印出 __session__.file.path。 
 ```

3. viper.py -> console.py -> session.py -> objects.py

 ```
 與 tour 2 相關，主要是 session.py 內用到了 objects.py 中的 File。
 其中，File 計算與提供檔案基本資訊，例如：檔案類型，sha256 hash value, file path 等。
 ```

4. viper.py -> console.py -> plugins.py -> abstracts.py -> colors.py

 ```
 console 介面會 listen 使用者輸入的指令，並檢查是否為內建 modules 指令。
 modules loaded 前會檢查其是否為 abstracts.py 中 Module class 的孩子，且不是 Module class 本身。
 ```

5. viper.py -> console.py -> plugins.py -> module/fuzzy.py -> out.py -> colors.py

 ```
 若 console 接到內建模組 fuzzy 指令，則會透過 plugins.py 載入 fuzzy 模組。
 用 dict 與 inspect 實作。 inspect 取得 module object。
 plugins[member_object.cmd] = dict(obj=member_object, description=member_object.description)
 將相對應指令塞入 dict 的 key 值，並透過建立巢狀字典，將 obj=member_object。
 開發者就可透過 module = __modules__[root]['obj']() 初始化模組的 instance。
 ```

6. viper.py -> console.py -> plugins.py -> module/fuzzy.py -> abstracts.py -> colors.py

 ```
 fuzzy.py 模組需要繼承 abstracts.py 中的基因。 
 ```

7. viper.py -> console.py -> plugins.py -> modules/fuzzy.py -> database.py -> out.py -> colors.py

 ```
 fuzzy.py 透過 Database 尋找相似檔案。
 ```

8. viper.py -> console.py -> plugins.py -> modules/fuzzy.py -> database.py -> objects.py

 ```
 新增樣本到資料庫中，會利用 objects.File 算出樣本基本資訊 (sha256, md5 等)。
 或是
 objects.py 中同時定義了 Singleton 模式，供 Database 類別繼承，保證一個類別只能有一個 instance。
 但此處 fuzzy.py 沒用到任何一種功能。
 ```

9. viper.py -> console.py -> plugins.py -> modules/fuzzy.py -> session.py -> out.py -> colors.py

 ```
 fuzzy.py 用 session.py 來檢查三件事。
 1. __session__.is.set() 檢查 session 是否開啟。
 2. 檢查該 session 中樣本是否有 ssdeep hash available。
 3. 用 pydeep 比較現在分析的檔案 (__session__.file.ssdeep) 跟從 db 裡撈出之樣本 (sample.ssdeep)。
 ```

10. viper.py -> console.py -> plugins.py -> modules/fuzzy.py -> session.py -> objects.py 

 ```
 此處 session.py 中 objects.py 沒被用到。
 objects.py 用來負責計算與提供，正被分析檔案的基本資訊，例如：檔案類型，sha256 hash value 等。
 而此事，早在 session 一打開時就計算完畢了。
 ```

11. viper.py -> console.py -> plugins.py -> modules/pe.py -> out.py -> colors.py

 ```
 若 console 接到內建模組 pe 指令，則會透過 plugins.py 載入 pe 模組。
 用 dict 與 inspect 實作。 inspect 取得 module object。
 plugins[member_object.cmd] = dict(obj=member_object, description=member_object.description)
 將相對應指令塞入 dict 的 key 值，並透過建立巢狀字典，將 obj=member_object。
 開發者就可透過 module = __modules__[root]['obj']() 初始化模組的 instance。
 ```

12. viper.py -> console.py -> plugins.py -> modules/pe.py -> objects.py

 ```
 此處 objects.py 中 File 沒被用到。
 ```

13. viper.py -> console.py -> plugins.py -> modules/pe.py -> abstracts.py -> colors.py

 ```
 pe.py 模組需要繼承 abstracts.py 中的基因。 
 ```

14. viper.py -> console.py -> plugins.py -> modules/pe.py -> session.py -> out.py -> colors.py 

 ```
 pe.py 用 session.py 來檢查三件事。
 1. __session__.is.set() 檢查 session 是否開啟。
 2. 用 pefile.PE 打開樣本取得 PE 資訊，其中樣本路徑由 __session__.file.path 取得。
 3. 將 PE file 中的 resource dump (圖片等資訊) 出來且指定 dump 到特定資料夾時會用到。
 ```

15. viper.py -> console.py -> plugins.py -> modules/pe.py -> session.py -> objects.py

 ```
 此處 session.py 中 objects.py 沒被用到。
 objects.py 用來負責計算與提供，正被分析檔案的基本資訊，例如：檔案類型，sha256 hash value 等。
 而此事，早在 session 一打開時就計算完畢了。
 ```

16. viper.py -> console.py -> plugins.py -> modules/strings.py -> out.py -> colors.py

 ```
 若 console 接到內建模組 strings 指令，則會透過 plugins.py 載入 strings 模組。
 用 dict 與 inspect 實作。 inspect 取得 module object。
 plugins[member_object.cmd] = dict(obj=member_object, description=member_object.description)
 將相對應指令塞入 dict 的 key 值，並透過建立巢狀字典，將 obj=member_object。
 開發者就可透過 module = __modules__[root]['obj']() 初始化模組的 instance。
 ```

17. viper.py -> console.py -> plugins.py -> modules/strings.py -> abstracts.py -> colors.py

 ```
 strings.py 模組需要繼承 abstracts.py 中的基因。 
 ```

18. viper.py -> console.py -> plugins.py -> modules/strings.py -> session.py -> out.py -> colors.py

 ```
 strings.py 用 session.py 來檢查三件事。
 1. __session__.is.set() 檢查 session 是否開啟。
 2. 檢查 __session__.file.path 是否存在。
 3. 用 open(__session__.file.path, 'r').read() 讀取檔案，爬字串。
 ```

19. viper.py -> console.py -> plugins.py -> modules/strings.py -> session.py -> objects.py 

 ```
 此處 session.py 中 objects.py 沒被用到。
 objects.py 用來負責計算與提供，正被分析檔案的基本資訊，例如：檔案類型，sha256 hash value 等。
 而此事，早在 session 一打開時就計算完畢了
 ```

20. viper.py -> console.py -> plugins.py -> modules/virustotal.py -> out.py -> colors.py

 ```
 若 console 接到內建模組 virustotal 指令，則會透過 plugins.py 載入 virustotal 模組。
 用 dict 與 inspect 實作。 inspect 取得 module object。
 plugins[member_object.cmd] = dict(obj=member_object, description=member_object.description)
 將相對應指令塞入 dict 的 key 值，並透過建立巢狀字典，將 obj=member_object。
 開發者就可透過 module = __modules__[root]['obj']() 初始化模組的 instance。
 ```

21. viper.py -> console.py -> plugins.py -> modules/virustotal.py -> abstracts.py -> colors.py

 ```
 virustotal.py 模組需要繼承 abstracts.py 中的基因。
 ```

22. viper.py -> console.py -> plugins.py -> modules/virustotal.py -> session.py -> out.py -> colors.py

 ```
 virustotal.py 用 session.py 來檢查三件事。
 1. __session__.is.set() 檢查 session 是否開啟。
 2. 利用 __session__.file.md5 取得檔案 md5 hash，餵到 virustotal 查詢。
 ```

23. viper.py -> console.py -> plugins.py -> modules/virustotal.py -> session.py -> objects.py

 ```
 此處 session.py 中 objects.py 沒被用到。
 objects.py 用來負責計算與提供，正被分析檔案的基本資訊，例如：檔案類型，sha256 hash value 等。
 而此事，早在 session 一打開時就計算完畢了
 ```

24. viper.py -> console.py -> plugins.py -> modules/yarascan.py -> out.py -> colors.py

 ```
 若 console 接到內建模組 strings 指令，則會透過 plugins.py 載入 pe 模組。
 用 dict 與 inspect 實作。 inspect 取得 module object。
 plugins[member_object.cmd] = dict(obj=member_object, description=member_object.description)
 將相對應指令塞入 dict 的 key 值，並透過建立巢狀字典，將 obj=member_object。
 開發者就可透過 module = __modules__[root]['obj']() 初始化模組的 instance。
 ```

25. viper.py -> console.py -> plugins.py -> modules/yarascan.py -> abstracts.py -> colors.py

 ```
 yarascan.py 模組需要繼承 abstracts.py 中的基因。 
 ```

26. viper.py -> console.py -> plugins.py -> modules/yarascan.py -> database.py -> out.py -> colors.py

 ```
 yarascan.py 從 db 裡撈出所有樣本 samples = db.find(key='all')，
 並用
 rules.match(path)
 掃描樣本。
 ```

27. viper.py -> console.py -> plugins.py -> modules/yarascan.py -> database.py -> objects.py

 ```
 新增樣本到資料庫中，會利用 objects.File 算出樣本基本資訊 (sha256, md5 等)。
 或是
 objects.py 中同時定義了 Singleton 模式，供 Database 類別繼承，保證一個類別只能有一個 instance。
 但此處 yarascan.py 沒用到任何一種功能。
 ```

28. viper.py -> console.py -> plugins.py -> modules/yarascan.py -> session.py -> out.py -> colors.py

 ```
 virustotal.py 用 session.py 來檢查三件事。
 1. __session__.is.set() 檢查 session 是否開啟。
 2. 利用 __session__.file.path 取得檔案路徑。
 ```

29. viper.py -> console.py -> plugins.py -> modules/yarascan.py -> session.py -> objects.py

 ```
 此處 session.py 中 objects.py 沒被用到。
 objects.py 用來負責計算與提供，正被分析檔案的基本資訊，例如：檔案類型，sha256 hash value 等。
 而此事，早在 session 一打開時就計算完畢了
 ```
 
30. viper.py -> console.py -> plugins.py -> modules/yarascan.py -> storage.py 

 ```
 yarascan.py 掃描檔案前，需透過 storage 中的 get_sample_path 取得已儲存檔案之路徑。
 ```

31. viper.py -> console.py -> commands.py -> out.py -> colors.py

 ```
 啟動 viper console 介面，console 會 import commands.py 中定義的 viper 系統指令。
 其中，輸入指令後，針對 viper 不同執行狀態，印出客製化相對應之輸出訊息與顏色。
 ```

32. viper.py -> console.py -> commands.py -> colors.py

 ```
 同上，
 但輸入指令後，有些 output 訊息不一定會用到 out.py 的格式。
 所以直接用 colors.py 中的顏色顯示輸出。
 ```

33. viper.py -> console.py -> commands.py -> session.py -> out.py -> colors.py

 ```
 commands.py 用 session.py 處理下列事：
 1. 檔案被分析時，就會開啟 session，並將檔案相關資訊 (file type, hash value, file path etc.) 載入。
 2. 用 __session__.clear() 關掉 session。
 3. 印出檔案資訊時，會先檢查 session 是否 open。
 4. 儲存檔案到 local repository 時，以及儲存檔案資訊到 db 時，會先檢查 session 是否 open。
 5. 刪除檔案，以及刪除 db 中檔案資訊時，會先檢查 session 是否 open。
 ```

34. viper.py -> console.py -> commands.py -> session.py -> objects.py

 ```
 基本同上，
 在 open session 時，會先用 objects.py 中的 File 計算檔案 hash。  
 ```

35. viper.py -> console.py -> commands.py -> plugins.py -> abstracts.py -> colors.py

 ```
 在 cmd_help() 中，plugins.py 中 __modules__.item() 用來列出模組清單。
 ```

36. viper.py -> console.py -> commands.py -> plugins.py -> modules/fuzzy.py -> out.py -> colors.py

 ```
 commands.py 主要是定義系統指令，plugins.py 中的 __modules__ 只用來列出模組清單。
 沒做其他事。
 如果 plugins.py 要往下走，這部份請看 console.py。
 ```

37. viper.py ->  console.py -> commands.py -> plugins.py -> modules/fuzzy.py -> abstracts.py -> colors.py

 ```
 同上
 ```

38. viper.py -> console.py -> commands.py -> plugins.py -> modules/fuzzy.py -> database.py -> out.py -> colors.py

 ```
 同上
 ```

39. viper.py -> console.py -> commands.py -> plugins.py -> modules/fuzzy.py -> database.py -> objects.py 

 ```
 同上
 ```
 
40. viper.py -> console.py -> commands.py -> plugins.py -> modules/fuzzy.py -> session.py -> out.py -> colors.py

 ```
 同上
 ```
 
41. viper.py -> console.py -> commands.py -> plugins.py -> modules/fuzzy.py -> session.py -> objects.py

 ```
 同上
 ```
 
42. viper.py -> console.py -> commands.py -> plugins.py -> modules/pe.py -> out.py -> colors.py

 ```
 同上
 ```
 
43. viper.py -> console.py -> commands.py -> plugins.py -> modules/pe.py -> objects.py

 ```
 同上
 ```
 
44. viper.py -> console.py -> commands.py -> plugins.py -> modules/pe.py -> abstracts.py -> colors.py

 ```
 同上
 ```
 
45. viper.py -> console.py -> commands.py -> plugins.py -> modules/pe.py -> session.py -> out.py -> colors.py

 ```
 同上
 ```
 
46. viper.py -> console.py -> commands.py -> plugins.py -> modules/pe.py -> session.py -> objects.py

 ```
 同上
 ```
 
47. viper.py -> console.py -> commands.py -> plugins.py -> modules/strings.py -> out.py -> colors.py

 ```
 同上
 ```
 
48. viper.py -> console.py -> commands.py -> plugins.py -> modules/strings.py -> abstracts.py -> colors.py

 ```
 同上
 ```
 
49. viper.py -> console.py -> commands.py -> plugins.py -> modules/strings.py -> session.py -> out.py -> colors.py

 ```
 同上
 ```
 
50. viper.py -> console.py -> commands.py -> plugins.py -> modules/strings.py -> session.py -> objects.py

 ```
 同上
 ```
 
51. viper.py -> console.py -> commands.py -> plugins.py -> modules/virustotal.py -> out.py -> colors.py 

 ```
 同上
 ```
 
52. viper.py -> console.py -> commands.py -> plugins.py -> modules/virustotal.py -> abstracts.py -> colors.py

 ```
 同上
 ```
 
53. viper.py -> console.py -> commands.py -> plugins.py -> modules/virustotal.py -> session.py -> out.py -> colors.py

 ```
 同上
 ```
 
54. viper.py -> console.py -> commands.py -> plugins.py -> modules/virustotal.py -> session.py -> objects.py

 ```
 同上
 ```
 
55. viper.py -> console.py -> commands.py -> plugins.py -> modules/yarascan.py -> out.py -> colors.py 

 ```
 同上
 ```
 
56. viper.py -> console.py -> commands.py -> plugins.py -> modules/yarascan.py -> abstracts.py -> colors.py

 ```
 同上
 ```
 
57. viper.py -> console.py -> commands.py -> plugins.py -> modules/yarascan.py -> database.py -> out.py -> colors.py

 ```
 同上
 ```
 
58. viper.py -> console.py -> commands.py -> plugins.py -> modules/yarascan.py -> database.py -> objects.py

 ```
 同上
 ```
 
59. viper.py -> console.py -> commands.py -> plugins.py -> modules/yarascan.py -> session.py -> out.py -> colors.py

 ```
 同上
 ```
 
60. viper.py -> console.py -> commands.py -> plugins.py -> modules/yarascan.py -> session.py -> objects.py

 ```
 同上
 ```
 
61. viper.py -> console.py -> commands.py -> plugins.py -> modules/yarascan.py -> storage.py

 ```
 同上
 ```
 
62. viper.py -> console.py -> commands.py -> database.py -> out.py -> colors.py 

 ```
 commands.py 中 self.db = Database() 初始化 db instance。
 此 instance 用來
 1. cmd_store function 中用來儲存檔案。
 2. cmd_delete function 中用來尋找欲刪除檔案，以及刪除檔案。
 3. cmd_find function 中用來尋找檔案。
 ```

63. viper.py -> console.py -> commands.py -> database.py -> objects.py

 ```
 在資料庫中操作時(儲存、尋找、刪除檔案)時，需要 objects.py 提供相關資訊以操作。
 ```

64. viper.py console.py commands.py storage.py

 ```
 cmd_store function 中，用到 store_sample，在檔案儲存前，將儲存路徑給定義好。
 cmd_open function 中，用到 get_sample_path，取得檔案路徑。
 cmd_delete function 中，用到 get_sample_path，取得欲刪除檔案之路徑。
 
 ```
