### pe.py

#### 解說

```
用 HAVE_PEFILE 及 HAVE_MAGIC 兩 flag
表示 pefile, magic 兩 module 是否被成功 import

class PE 繼承自 class Module

instance 初始化時，先將 self.pe = None (尚不知用意

PE 內有 function 如下：
__get_filetype()
imports()
exports()
resources()
help()
run()

1. __get_filetype()
    先檢查有無 import magic 套件
    若無，則 return None

    此處作者用了兩種方法取得 file_type
    1. 先用 magic-python module 來做。
        https://github.com/mammadori/magic-python
    2. 若第一種方法行不通，則用 python-magic 來做。
        https://github.com/ahupp/python-magic

    與 objects.py 相比，這裡少了用 subprocess 呼叫 file 指令來做。

2. imports()
    先檢查 self.pe 是否存在
    若無，則跳出 imports()

    self.pe 在 run function 中 line 155 給予

    用 hasattr 判斷 DIRECTORY_ENTRY_IMPORT 是否為 self.pe instance 內的 attribute
    若是，則用迴圈一一取出 self.pe.DIRECTORY_ENTRY_IMPORT as entry
    接著印出 entry.dll
    再用迴圈一一取出 entry.imports as symbol
    印出 hex(symbol.address) 以及 symbol.name

3. exports()
    先檢查 self.pe 是否存在
    若無，則跳出 exports()

    印出 [*] Exports:

    接著用 hasattr 判斷 DIRECTORY_ENTRY_IMPORT 是否為 self.pe instance 內的 attribute
    若是，則用迴圈一一取出 self.pe.DIRECTORY_ENTRY_EXPORT.symbols as symbol
    接著印出
        1. hex(self.pe.OPTIONAL_HEADER.ImageBase + symbol.address)
        2. symbol.name
        3. symbol.ordinal

4. resources()
    先檢查 self.pe 是否存在
    若無，則跳出 resources

    function usage
    印出 usage: pe resources [-d=folder]
    顯數 resources 底下還有 -d 參數可用

    function help
    呼叫 usage 先印一次簡單的用法。
    再更細部印出 resources 底下的參數、用法。

    接著用 getopt 抓出 resources 後面的參數
    self.args[0] could be resources, imports or exports

    line 87, dump_to 先設為 None
    接著處理 opts
    若參數是 -h or --help 則呼叫 help()
    若參數是 -d or --dump
    則將 value (也就是儲存 resources files 的目標資料夾) assign 給 dump_to

    接著建立一名為 resources 的空 list。

    line 98, 接著用 hasattr 判斷 DIRECTORY_ENTRY_IMPORT 是否為 self.pe instance 內的 attribute
    若是，則用迴圈一一取出 self.pe.DIRECTORY_ENTRY_RESOURCE.entries as resource_type
        迴圈內，先建立一名為 resource 的空字典
        若 resource_type.name 不是 None
            則 name = str(resource_type.name)
        若是 None
            則 name = str(pefile.RESOURCE_TYPE.get(resource_type.struct.Id))

        接著檢查 name 是否 == None
            若是，則 name = str(resource_type.struct.Id)

        接著又用 hasattr 檢查 directory 是否為 resource_type 的 attribute
            若是，則用迴圈一一取出 resource_type.directory.entries as resource_lang
                迴圈內
                1. 用 self.pe.get_data() 將結果給予 data
                2. 用 self.__get_filetype(data) 將結果給予 filetype
                3. 用 pefile.LANG.get() 將結果給予 language
                4. 用 pefile.get_sublang_name_for_lang() 將結果給予 sublanguage
                5. 讓 ('%-8s' % hex(resource_lang.data.struct.OffsetToData)).strip() 處理後結果給予 offset
                6. 讓 ('%-8s' % hex(resource_lang.data.struct.Size)).strip() 處理後結果給予 size

                最後將 name, offset, size, filetype, language, sublanguage 丟入 resource list中。

                若 dump_to 不是空
                    則用 os.path.join 將 __session__.file.md5, offset, name 合併為 resource_path
                    再將 resource_path append 到 resource list 中

                    接著開檔將資料寫入檔案

                寫完後，再將 resource append 到 resources list 中。

    line 136, 設定 headers list
    若 dump_to 非為空
        則 headers.append('Dumped To')

    line 138, 用 pretty table 印出 resources

    看到這裡，感覺 line 191, 的 resource 字典沒被用到？

5. help()
    印出 Choose an option!

6. run()
    首先檢查 session 是否 open
        若否則印出 No session opened
        接著離開 run

    接著檢查是否有成功 import pefile
        若無，則印出 Missing dependency, install pefile (`pip install pefile`)

    試
        用 pefile.PE(__session__.file.path) 將結果給 self.pe
    若失敗
        則印出 Unable to parse PE file
        並離開 run

    檢查參數長度是否為零
        若是，則呼叫 help()
        並離開 run

    若 self.args[0] == 'imports'
        呼叫 self.imports()
    若為 'exports'
        呼叫 self.exports()
    若為 'resources'
        呼叫 self.resources()
```

```python
class Demo:
    def __init__(self, i):
        self.i = i
        self.x = "xxx"
        self.y = "yyy"
        self.z = "zzz"

    def __str__(self):
        return str(self.i)

    def hello(self):
        print("hello " + self.__str__())

d = Demo(22)
print(hasattr(d, "t"))
print(hasattr(d, "u"))
print(hasattr(d, "v"))
print(hasattr(d, "w"))
print(hasattr(d, "x"))
print(hasattr(d, "y"))
print(hasattr(d, "z"))
```
