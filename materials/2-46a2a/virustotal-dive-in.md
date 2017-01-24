### virustotal.py

#### 解說

```
使用 virustotal 官方 public api。

class virustotal 繼承自 class Module

class function run 運行後
會先用 __session__.is_set() 檢查 session 是否 open。
若無，則印出 No session opened
並結束 run function。

若 session 有開啟，
則用 urllib.urlencode 將資料 encode 成百分號編碼 (percent-encoding)或稱 URL encoding，
encode 後，將結果 pass 給 urlopen 當 optional data argument。
參考資料 ： https://docs.python.org/2/library/urllib.html#urllib.urlopen

接著用 urllib2.request 初始化一個 request instance
將此 instance 餵入 urlopen 後，得到 response。
response.read() 處理過後，得到 response_data

接著將 response_data 以 json.loads方式讀取，並將讀取結果傳給 virustotal。

查看檢測結果，將 engine 及 signature 爬出，並 append 到 rows list 中。最後用 prettytable 將結果印出。
```

```
    {
     'response_code': 1,
     'verbose_msg': 'Scan finished, scan information embedded in this object',
     'resource': '99017f6eebbac24f351415dd410d522d',
     'scan_id': '52d3df0ed60c46f336c131bf2ca454f73bafdc4b04dfa2aea80746f5ba9e6d1c-1273894724',
     'md5': '99017f6eebbac24f351415dd410d522d',
     'sha1': '4d1740485713a2ab3a4f5822a01f645fe8387f92',
     'sha256': '52d3df0ed60c46f336c131bf2ca454f73bafdc4b04dfa2aea80746f5ba9e6d1c',
     'scan_date': '2010-05-15 03:38:44',
     'positives': 40,
     'total': 40,
     'scans': {
        'nProtect': {'detected': true, 'version': '2010-05-14.01', 'result': 'Trojan.Generic.3611249', 'update': '20100514'},
        'CAT-QuickHeal': {'detected': true, 'version': '10.00', 'result': 'Trojan.VB.acgy', 'update': '20100514'},
        'McAfee': {'detected': true, 'version': '5.400.0.1158', 'result': 'Generic.dx!rkx', 'update': '20100515'},
        'TheHacker': {'detected': true, 'version': '6.5.2.0.280', 'result': 'Trojan/VB.gen', 'update': '20100514'},
        .
        .
        .
        'VirusBuster': {'detected': true, 'version': '5.0.27.0', 'result': 'Trojan.VB.JFDE', 'update': '20100514'},
        'NOD32': {'detected': true, 'version': '5115', 'result': 'a variant of Win32/Qhost.NTY', 'update': '20100514'},
        'F-Prot': {'detected': false, 'version': '4.5.1.85', 'result': null, 'update': '20100514'},
        'Symantec': {'detected': true, 'version': '20101.1.0.89', 'result': 'Trojan.KillAV', 'update': '20100515'},
        'Norman': {'detected': true, 'version': '6.04.12', 'result': 'W32/Smalltroj.YFHZ', 'update': '20100514'},
        'TrendMicro-HouseCall': {'detected': true, 'version': '9.120.0.1004', 'result': 'TROJ_VB.JVJ', 'update': '20100515'},
        'Avast': {'detected': true, 'version': '4.8.1351.0', 'result': 'Win32:Malware-gen', 'update': '20100514'},
        'eSafe': {'detected': true, 'version': '7.0.17.0', 'result': 'Win32.TRVB.Acgy', 'update': '20100513'}
      },
     'permalink': 'https://www.virustotal.com/file/52d3df0ed60c46f336c131bf2ca454f73bafdc4b04dfa2aea80746f5ba9e6d1c/analysis/1273894724/'
    }
```
