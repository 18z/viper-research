### globals() 介紹

#### 此函式為 Python 內建，可用來查看所有全域變數 (包含 import module 相關資訊)。

```python
import inspect
import sys 
import os
import androguard
from hello import ooo

print globals()
```

執行結果：

```
{
'__builtins__': <module '__builtin__' (built-in)>, 
'__file__': 'in.py', 
'inspect': <module 'inspect' from '/home/deanboole/.pyenv/versions/2.7.6/lib/python2.7/inspect.pyc'>, 
'__package__': None, 'sys': <module 'sys' (built-in)>, 
'__name__': '__main__', 
'androguard': <module 'androguard' from '/home/deanboole/.pyenv/versions/2.7.6/lib/python2.7/site-packages/androguard/__init__.pyc'>, 
'os': <module 'os' from '/home/deanboole/.pyenv/versions/2.7.6/lib/python2.7/os.pyc'>, 
'__doc__': None, 'ooo': <function ooo at 0x117dc80>
}
```

#### 解釋：

* 由執行結果回傳一個 dictionary， 沒意外的話，module name 會顯示在 key 欄位，而 module source file location 會顯示在 value 欄位。

* 若有類似 ```from hello import ooo```, hello 為 py file， ooo 為 function。 則用 globals() 時需修改為  import hello 方便檢查。 
