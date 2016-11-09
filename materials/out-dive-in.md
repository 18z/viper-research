### out.py

#### 解說

```
程式內沒有進入點，需由外部呼叫程式內 function 才能運作。

此程式功能有

1. 此程式客製化不同執行狀態 (info, warning, error, success) 輸出訊息。
    假設用到 print_info() function。
    
    則會印出 print(bold(cyan("[*]")) + " {0}".format(message))
    我們逐步拆解
    先將 colors.py 中的 function 拿掉。即可簡化成
    print("[*]" + " {0}".format(message))
    
    若 message 為 "hello" 字串。
    則印出結果： [*] hello
    其中，{0} 表示印出 .format 中第零個位置的字串。
    
    {0}, {1} 位置可用下列範例理解
    
    >>> print '{0} and {1}'.format('spam', 'eggs')
    spam and eggs
    >>> print '{1} and {0}'.format('spam', 'eggs')
    eggs and spam
    

2. 客製化表單。(以表單呈現 viper 之模組或指令)


```
