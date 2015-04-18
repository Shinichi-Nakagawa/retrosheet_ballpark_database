# retrosheet_ballpark_database
MLB ballpark database for Retrosheet

## Description

Retrosheetの球場一覧をスクレイピング、GISデータとして利用可能とするプロジェクトです。

## Requirement

### Python Version

3.4.2(少なくとも3系推奨)

### Library
> pip install -r requirements.txt

### install

事前にGoogle Map API(V3)のAPI Keyを取得してください（方法は、、、ググってください）。

config.ini.exampleをコピーしてconfig.iniを作成、API Keyを取得したキーに書き換えましょう。

> cp config.ini.example config.ini

## 使い方

まず、データを取得&Geocodingを実施します。

> python ballparks.py

このコマンドが終わるとparklist.jsonが生成されます。

ちゃんと生成されたら以下のコマンドを実行してください。

> python create_database.py

これでballpark.dbという名前でsqlite3のデータベースが出来ます。

中身を見たい時はbottleのアプリを実行してください。

> python map.py

これでhttp://localhost:8000に接続すると地図が表示され、球場の位置が確認できます。

