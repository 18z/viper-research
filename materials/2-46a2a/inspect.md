### 用 inspect 檢查引用模組是否為 Python 內建模組

#### 結論先提

* 只要路徑不包含 site-packages 則可能就是 Python 內建模組。

* 另一種情況路徑也可能不包含 site-packages，但可能為專案本身自定義之模組。

#### 檢查 sys 模組

使用 inspect.getsourcefile(sys) [1] 檢查結果：

```
Traceback (most recent call last):
  File "in.py", line 7, in <module>
    print inspect.getsourcefile(sys)
  File "/home/deanboole/.pyenv/versions/2.7.6/lib/python2.7/inspect.py", line 444, in getsourcefile
    filename = getfile(object)
  File "/home/deanboole/.pyenv/versions/2.7.6/lib/python2.7/inspect.py", line 403, in getfile
    raise TypeError('{!r} is a built-in module'.format(object))
TypeError: <module 'sys' (built-in)> is a built-in module
```

出現 ```TypeError: <module 'sys' (built-in)> is a built-in module。```

出現 TypeError 可能原因為 [2]：

```
At best, you could use the inspect module to try and find some indicators, 
for example, using inspect.getsourcefile() to find where the source file is located, 
then using that to check if it's a core library. 

This won't work particularly well, 
however, as any modules in C will return a TypeError as they are builtins - 
but you can't presume they are from the standard library, 
as any C extension module will do the same thing.
```

#### 檢查 os 模組

使用 inspect.getsourcefile(os) 檢查結果：

```
/home/user/.pyenv/versions/2.7.6/lib/python2.7/os.py
```

參考文獻：

[1] https://docs.python.org/3/library/inspect.html#inspect.getsourcefile

[2] http://stackoverflow.com/questions/12854442/python-how-to-check-if-an-imported-module-package-class-is-from-standard-librar
