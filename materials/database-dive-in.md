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

```
