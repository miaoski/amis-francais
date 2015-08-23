關於
====
本字典由在花蓮鐵份部落服務的巴黎外方會潘世光神父慨允釋出，供非商業使用。


編輯說明
========
轉換後與方敏英字典的格式相容。

```
# 這個開頭的是註解
title (單詞)
def1 (法語定義)
- 阿美語片語
  法語解釋
- 阿美語例句
  法語解釋
=> 相關詞, 逗號隔開, 字根請放這裡
def2 (法語字義2)
- 阿美語片語
  法語解釋
- 阿美語例句
  法語解釋
```

拼寫
----
請保留原有的拼法，如 negneg 請不要寫成 nengneng, 轉換格式的時候，我們會用程式轉成現在比較通用的形式。


切法
====
請先安裝 `tesseract`, `PIL`, `BeautifulSoup`。以第 10 頁為例:
```
$ tesseract pic/010.jpg hocr/010.html -l fra hocr
$ cd hocr
$ sqlite3 toufu.sq3 < toufu.sql
$ python hocr2pars.py 010
```
我們試過先切成一條一條的，再丟進 tesseract ，辨識率比一次辨識整頁低了許多。所以改用這個方式。


License
=======
字典由潘世光神父 (Maurice Poinsot) 及博利亞神父 (Louis Pourrias) 編著，依慣例著作權應屬 [Missions Etrangères de Paris] (http://www.mepasie.org/).
