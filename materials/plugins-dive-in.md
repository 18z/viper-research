### plugins.py

#### 解說

```
plugins.py 裡面主要做了
1. 使用 pkgutil 模組，該模組提供實用 function 以支援 import 系統。
2. 使用 inspect 模組，針對所匯入之模組做一些基本檢查，例如：是否為 class 等。

首先看到 pkgutil 模組，該模組提供走訪特定路徑下 package 的功能。
此處用到的是 pkgutil.walk_packages()
https://docs.python.org/2/library/pkgutil.html

傳入參數通常只會有兩個 (手冊上共三個)
1. path: 走訪模組之路徑
2. prefix: 印出 module name 之前的 prefix，通常為 module.__name__ + '.'

此 function 回傳三個東西
1. module_loader: 尚不知為何物， plugins.py 中沒用到
2. module_name: 用在 __import__ 之參數
3. ispkg: 檢查是否為 package

若被檢查出是個 package，則 continue。
package 與 module 差別如下

A module is a single file (or files) that are imported under one import and used. e.g.
    import my_module

A package is a collection of modules in directories that give a package hierarchy.
    from my_package.timing.danger.internets import function_of_love

http://stackoverflow.com/questions/7948494/whats-the-difference-between-a-python-module-and-a-python-package

若不是，則使用 __import__, 將 module import。

__import__ 為 python 內建函式
傳入值有 name, globals, locals, fromlist, level

name: The function imports the module name

globals, locals: potentially using the given globals and locals 
                 to determine how to interpret the name in a package context.
                 
fromlist: The fromlist gives the names of objects or submodules 
          that should be imported from the module given by name.

level: specifies whether to use absolute or relative imports. 
       The default is -1 which indicates both absolute and relative imports will be attempted.
       




```
