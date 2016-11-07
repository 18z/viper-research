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
 將相對應指令塞入 dict 的 key 值，並透過建立巢狀迴圈，將 obj=member_object。
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
 將相對應指令塞入 dict 的 key 值，並透過建立巢狀迴圈，將 obj=member_object。
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
 若 console 接到內建模組 strings 指令，則會透過 plugins.py 載入 pe 模組。
 用 dict 與 inspect 實作。 inspect 取得 module object。
 plugins[member_object.cmd] = dict(obj=member_object, description=member_object.description)
 將相對應指令塞入 dict 的 key 值，並透過建立巢狀迴圈，將 obj=member_object。
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
 
 ```

21. viper.py console.py plugins.py modules/virustotal.py abstracts.py colors.py

22. viper.py console.py plugins.py modules/virustotal.py session.py out.py colors.py

23. viper.py console.py plugins.py modules/virustotal.py session.py objects.py

24. viper.py console.py plugins.py modules/yarascan.py out.py colors.py

25. viper.py console.py plugins.py modules/yarascan.py abstracts.py colors.py

26. viper.py console.py plugins.py modules/yarascan.py database.py out.py colors.py

27. viper.py console.py plugins.py modules/yarascan.py database.py objects.py

28. viper.py console.py plugins.py modules/yarascan.py session.py out.py colors.py

29. viper.py console.py plugins.py modules/yarascan.py session.py objects.py
 
30. viper.py console.py plugins.py modules/yarascan.py storage.py 

31. viper.py console.py commands.py out.py colors.py

32. viper.py console.py commands.py colors.py

33. viper.py console.py commands.py session.py out.py colors.py

34. viper.py console.py commands.py session.py objects.py

35. viper.py console.py commands.py plugins.py abstracts.py colors.py

36. viper.py console.py commands.py plugins.py modules/fuzzy.py out.py colors.py

37. viper.py console.py commands.py plugins.py modules/fuzzy.py abstracts.py colors.py

38. viper.py console.py commands.py plugins.py modules/fuzzy.py database.py out.py colors.py

39. viper.py console.py commands.py plugins.py modules/fuzzy.py database.py objects.py 

40. viper.py console.py commands.py plugins.py modules/fuzzy.py session.py out.py colors.py

41. viper.py console.py commands.py plugins.py modules/fuzzy.py session.py objects.py

42. viper.py console.py commands.py plugins.py modules/pe.py out.py colors.py

43. viper.py console.py commands.py plugins.py modules/pe.py objects.py

44. viper.py console.py commands.py plugins.py modules/pe.py abstracts.py colors.py

45. viper.py console.py commands.py plugins.py modules/pe.py session.py out.py colors.py

46. viper.py console.py commands.py plugins.py modules/pe.py session.py objects.py

47. viper.py console.py commands.py plugins.py modules/strings.py out.py colors.py

48. viper.py console.py commands.py plugins.py modules/strings.py abstracts.py colors.py

49. viper.py console.py commands.py plugins.py modules/strings.py session.py out.py colors.py

50. viper.py console.py commands.py plugins.py modules/strings.py session.py objects.py

51. viper.py console.py commands.py plugins.py modules/virustotal.py out.py colors.py 

52. viper.py console.py commands.py plugins.py modules/virustotal.py abstracts.py colors.py

53. viper.py console.py commands.py plugins.py modules/virustotal.py session.py out.py colors.py

54. viper.py console.py commands.py plugins.py modules/virustotal.py session.py objects.py

55. viper.py console.py commands.py plugins.py modules/yarascan.py out.py colors.py 

56. viper.py console.py commands.py plugins.py modules/yarascan.py abstracts.py colors.py

57. viper.py console.py commands.py plugins.py modules/yarascan.py database.py out.py colors.py

58. viper.py console.py commands.py plugins.py modules/yarascan.py database.py objects.py

59. viper.py console.py commands.py plugins.py modules/yarascan.py session.py out.py colors.py

60. viper.py console.py commands.py plugins.py modules/yarascan.py session.py objects.py

61. viper.py console.py commands.py plugins.py modules/yarascan.py storage.py

62. viper.py console.py commands.py database.py out.py colors.py 

63. viper.py console.py commands.py database.py objects.py

64. viper.py console.py commands.py storage.py
