# CommandControl
SPRとGPSR用のコードで、音声認識結果のテキストをもらって返答のテキストを書くところ

## install
```
$ pip install xmltodict
```

## 大会当日にすること
[ ] SPRを行う部屋を`SPR_PLAY_ROOM`で設定しとく.`vim CommandControl/Behavior.py`
[ ] 部屋のドアの数を記入する
[ ] Object.xmlとLocation.xmlのデータを記入する
[ ] SPRに使うかGPSRに使うかの変更をする

## Xmlファイルについて
- 新しくプログラムから参照されるxmlファイルを追加する場合は、XmlPerser.pyを触ればいいです
- `size='10'`とかしてるのの単位はmmです

## このプログラムはキモい
なにがキモいか？

- 以下のxmlデータを{'category':'toiletries','name':'shampoo'}として変数に格納するようにしている。
```
本来階層構造になってるものを浅くする必要はあるのか?
<category name="toiletries" defaultLocation="bathroom cabinet" room="bathroom">
  <object name="shampoo"       difficulty="moderate"                               />
</category>
```
- めっちゃファイル分割しとる
- xmlファイルがetcファイルとかにまとまってない ---> windowsとlinuxではpathの関係で分割すると面倒になるのでこうしてる雑魚
- xmlファイルにデータを手打ちする必要がある。excelでポチポチしてそれを利用したほうが楽

