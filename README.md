# CommandControl
SPRとGPSR用のコードで、音声認識結果のテキストをもらって返答のテキストを書くところ

## install
'''
$ pip install xmltodict
'''

## このプログラムはキモい
なにがキモいか？

- 以下のxmlデータを{'category':'toiletries','name':'shampoo'}として変数に格納するようにしている。
本来階層構造になってるものを浅くする必要はあるのか?
~~~
<category name="toiletries" defaultLocation="bathroom cabinet" room="bathroom">
  <object name="shampoo"       difficulty="moderate"                               />
</category>
~~~
