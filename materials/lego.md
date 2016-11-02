### Viper Lego

#### colors.py

* 客製化輸出訊息之顏色，讓 programmer 易操控輸出字串之顏色。

#### out.py

* viper 會依據不同執行狀態，印出相對應的客製化訊息。
* 此程式客製化不同執行狀態 (info, warning, error, success) 輸出訊息。
* 客製化表單。(以表單呈現 viper 之模組或指令)

#### out.py + colors.py

* 針對 viper 不同執行狀態，客製化相對應之輸出訊息與顏色。

#### abstracts.py

* 定義模組之基因。
* 未來新增加之模組會繼承此基因，並依不同狀況修改。

#### abstracts.py + colors.py

* 只看到 abstracts.py 中 import colors。但未看到使用 colors 中功能。
