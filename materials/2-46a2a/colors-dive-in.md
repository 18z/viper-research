### colors.py

#### 解說

```
# 程式內沒有進入點，需由外部呼叫程式內 function 才能運作。

# 此程式客製化輸出訊息之顏色，讓 programmer 易操控輸出字串之顏色。
# 若欲印出綠色字串，則可使用 green() function。

green(input 為 text，即欲印出之字串)
    回傳 color(字串, 顏色代碼)。

# 回傳時 color(字串, 顏色代碼) function 被呼叫。
function 執行後會先用 sys.platform 檢查系統是否為 win32，也會用 os.getenv("TERM") 檢查使用的 terminal 為何。
    若系統為 win32 且 terminal 不是 xterm。
    則直接回傳 text，也就是沒有經過色碼加工過的字串。
    第 16 行的 return 就不會被執行。

若未符合上述條件，則回傳 "\x1b[%dm%s\x1b[0m" % (color_code, text)
# %d:是整數的 format code
# %s:是字串的 format code

# 假如 text = "12345"
# 經過 "\x1b[%dm%s\x1b[0m" % (32, text)
# 則 print "\x1b[%dm%s\x1b[0m" % (32, text) 就會印出綠色的 12345
```
