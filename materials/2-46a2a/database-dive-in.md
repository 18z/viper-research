### database.py

#### 解說

```
Base = declarative_base()
依據手冊 http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/basic_use.html

declarative_base() 回傳一 base class，好讓表單 class 繼承。
接著便定義表單欄位。

declarative_base() 基礎類別包含 MetaData object。

在 tag 中，定義表單之間關係。用到 association_table
多對多關係，
一個樣本可以對應到很多個 tag
一個 tag 可以對應到很多樣本

association_table 也是一張表。
表內只有放 foreign key。

cascade='all, delete'
依據手冊 cascade 表示當一張表格變動時，其他關聯表格的相依動作之定義。
The all symbol is a synonym for 
save-update, merge, refresh-expire, expunge, delete, 
and using it in conjunction with delete-orphan 
indicates that the child object 
should follow along with its parent in all cases, 
and be deleted once it is no longer associated with that parent.

筆者理解如下
all 即包含 save-update, merge, refresh-expire, expinge, delet 這些動作
通常會與 all 一起使用的定義就是 delete-orphan。

所以，可能作者誤用，因此重複用了 delete，或當時 sqlalchemy 版本如此撰寫。

初步理解：
delete: 父親被刪除，所有兒子被刪除。
delete-orphan: 若有孤兒，則刪除所有孤兒。
backref: 讓 Tag 也可以 reference 回去 malware，但無法刪除 malware。

__table_args__: 除了 name, metadata, mapped Column 這些參數設定之外，其他設定可用 __table_args__
http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/table_config.html

Index: 設定 table 參數。理解是 place a uniq index anonymously on md5, crc32, sha1, sha256, sha512 欄位。
http://docs.sqlalchemy.org/en/latest/core/constraints.html

接著是 to_dict()，
大致理解是將表單中 column 塞到字典中。
目前尚未看到 to_dict() 在專案中被使用。

__repr__()
https://docs.python.org/2/reference/datamodel.html
Called by the repr() built-in function and by string conversions (reverse quotes) 
to compute the “official” string representation of an object. 
依據手冊，此 function 回傳字串。該字串是一物件之官方描述。

This is typically used for debugging, 
so it is important that the representation 
通常在 debugging 時會用。
is information-rich and unambiguous.
因此，官方描述需明確不模糊。

class Malware(Base) 中
最後一部分是初始化 __init__ class 中用到之變數。

接著是 class Tag(Base)
與 class Malware 相同，皆是資料表的設定，觀念相同，因此不贅述。

最後是 class Database:
首先看到 __metaclass__，
簡單說，metaclass 就是建立類別時的規範，
如果我們在寫類別時，加入 __metaclass__ 屬性，
則表示 python 會用 __metaclass__ 來創建該類別。

一般來說 python 都是用 type 來創建類別。
也就是說，若無特別指定，一般 class 都是 type 的 class instance。
用 __metaclass__ 指定，才會用其他元類來創建 class instance。

那 __metaclass__，也就是 Singleton 中都寫了什麼？
簡單說，就是寫一個類別。

那 __metaclass__ 跟繼承父類別差別是？
__metaclass__ 感覺是更接近源頭的東西。
跟繼承父類別相比，似乎可以做更多更細膩的操弄。
例如此地用於限制 Database 只能同時間只能存在一個 instance。

參考文獻： http://blog.jobbole.com/21351/

Databse 類別初始化時，
先建立資料庫引擎 instance。
poolclass = NullPool 
表示不使用 connection pool。也就是不允許閒置連線。

engine.echo = False
表示 engine 將不紀錄所有 statement。 

engine.pool_timeout = 60
此處與 NullPool 對不上來。目前不知如何解釋。

Base.metadata.create_all(self.engine)
create the table and tell it to create it in the database engine that is passed
在 self.engine 中建立 table。

self.Session = sessionmaker(bind=self.engine)
透過將 session 綁定 self.engine，並建立 Session instance。
即可透過 Session 與 database 互動，例如：query 等。

__del__
可用 del db instance 來拋棄現有的 engine。

接著看到 add function。
在 commands.py 中，cmd_store function 被呼叫。

傳入參數為 obj，name, tags。
但 name, tags 預設皆為 None。
cmd_store function 傳入的參數只有 obj。

進入 add function 後
首先初始化 session instance，開啟跟 engine 的  conversation。

接著檢查 name 變數有無給值，
若無則將 obj.name 之值給予 name 變數。

接著確認 obj 是否是 File class 的 instance。
若是，則初始化 malware_entry instance，並將 obj 相關資訊傳入Malware 建構子。
將 malware_entry instance 加入 session。
並透過 session.commit() 將資料寫入資料庫。

若是 Insert or update duplicate key in SQLAlchemy 則 raise integrityError。
接著 session.rollback() 恢復至 commit() 之前
並將 malware_entry 改成資料庫中已存在的 malware。

其他一般錯誤發生，則 raise SQLAlchemyError。

錯誤發生時，皆會呼叫 session.rollback()，
The session object's default behavior is to expire all state.
個人猜測，恢復所有狀態至 commit 前。

若有 tags，
則先將 tags 用 strip() 移除多餘空白字元。
接著，若 tags中有 "," 則用 split 將每個以逗號區隔的字串獨立
並依序塞入 list。
隨後再將 list 裡每個字串轉成小寫。
若是空字串，則 continue。

每個被切出來的字串
會透過 malware_entry.tag.append(Tag(tag)) 處理
首先，以 Tag 初始化一 instance，並將它 append 到 malware_entry.tag list 中。
此處先猜測 relationship 處理後結果，是 list。
以上動作理解成，malware_entry 這個 sample，透過 relationship，將 tag instance 綁在一起。
綁定後，透過 session.commit() 將綁定結果寫入資料庫中。

當然，寫入時也會檢查是否有 IntegrityError 以及 SQLAlchemyError。
若發生 IntegrityError，
則會先 session.rollback()
接著用 session.query() 從資料庫中找出同一個 tag，並將結果 append 到 malware_entry.tag 
再 session.commit() 一次。

若第二次 commit() 失敗，則跳 SQLAlchemyError，並 session.rollback()

不了解為何要二次 commit。

接著看到 delete function。

首先用 session 初始化與 db 的 conversation。
透過 find 找到的 id，去 query Malware 表。
接著透過 session.delete(malware) 刪除樣本。
再透過 session.commit() 將更動寫入資料庫。

這裡只檢查是否有 SQLAlchemyError，
若有，則 session.rollback()
最後不管如何，會將 session.close()。

接著看到 find function
兩個欄位，第一欄位為 key
第二欄位為 value。

搜尋可分成列出資料庫所有資料模式
以及
以 md5, sha256, ssdeep,tag 的搜尋模式。

最後是 list_tags() function。
也就是將所有 tags 都列出來。

```
