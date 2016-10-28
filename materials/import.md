### Import 用法

#### import module

* 優點：
    * 若需使用 module 裡的東西時，隨時可用。不需對 import statement 做調整。
  
* 缺點：
    * 每次使用模組內 item 時，皆需前綴，例如： module.black。

#### from module import black

* 優點：
    * 使用 black 時不需前綴。
  
* 缺點：
    * 失去 black 的前綴，讀者不易判斷 black 是引用字 module。 也容易發生重複定義 black 而程式出錯。
  
#### 參考文獻
[1] http://stackoverflow.com/questions/710551/import-module-or-from-module-import
