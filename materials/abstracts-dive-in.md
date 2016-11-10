### abstracts.py

#### 解說

```
建立 Module 類別供其他模組繼承。
建立模組應有基本藍圖。

類別中，類別變數 cmd, description, args
皆為空。

模組繼承後，便會再模組內定義。

類別變數除了 set_args 將 args 值給予 self.args 以外
其餘 usage, help, run 皆沒實作。

值得注意的是，raise NotImplementedError。
使用者若在模組中沒實作 usage, help, run。
則使用到該模組功能時，會raise NotImplementedError。
```
