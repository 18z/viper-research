### yarascan.py

#### 解說

```
首先 import yara 模組
若 import 成功，則將 HAVE_YARA flag 設為 True。

若失敗，則跳出 ImportError，並將 HAVE_YARA flag 設為 False。


class YaraScan 繼承自 class Module。

Yarascan 中只有一個 function, run。
在 run function 中，
首先檢查 HAVE_YARA flag，若 flag 為 False，
則印出 Missing dependency, install yara
接著結束 run

接著處理 console.py line 128 傳過來的參數。
用 getopt 處理。
此地接收參數 r

self.args[0:] 似乎與 self.args 沒差異？
作者寫法尚待研究。

接著將 rule_path 設為空字串

接著再處理 opts
將 opt 也就是 -r 或 --rule 後面所接的 rule 路徑
塞給 rule_path

假如 rule_path 是空的，或者 rule_path 路徑不存在
則將 rule_path 填為 data/yara/index.yara

接著再檢查一次 rule_path 路徑是否存在
若否，則印出 No valid Yara ruleset at rule_path
接著跳出 run

line 43 用 yara.compile 將 rule_path 底下的 rule，初始化成一 instance。(待確認
接著建立一個名為 paths 的空 list

line 46 檢查 session 是否 open
若有，則用 __session__.file.path 將檔案路徑 append 到 paths list 中。
若無，則初始化 db instance，並將 db 內所有樣本撈出來。

接著逐一將樣本路徑 append 到 paths 中。

最後，用一 for 迴圈，將 paths 中的樣本一一掃描。


```
