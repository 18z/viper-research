### commands.py

#### 解說

```
line 3 
  import tempfile

line 7 
  import 自建 module function download

line 78, 79 
  在 open()
       help()
         新增 url 與 tor 參數說明

line 83 
  getopt 增加可接收 url 與 tor 參數

line 90, 91
  增加 is_url 與 use_tor 兩 flag 

line 99 ~ 102
  判定 flag 是否須更改

line 118
  若 is_url flag == True
  則用 download function (tor flag 在此使用) 抓檔案
  並將結果用 tempfile 存起來

line 125
  幫 tmp.name 用 __session__.set() 處理基本資訊。
```
