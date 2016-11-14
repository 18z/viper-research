### storage.py

#### 解說

```
主要兩個 function。

1. store_sample 
2. get_sample_path

store_sample 中，主要用 os.path.join 建立權限為 0750 的資料夾
資料夾共有五層
第一層：binaries
第二層至第五層，則以樣本 sha256 值的前四字母或數字為資料夾名稱。

隨後再用 sha256 為檔名，將檔案寫入資料夾中。

get_sample_path 中，功能是將 sample 的 path 回傳。
```
