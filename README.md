# ups-battery-manager

Battery manager for UPS power unit by Nipron.

# システム要件

## バッテリー表示要件

別途ドキュメントを参照

## バッテリー残量確認方法

- 10 秒ごとに残量確認と処理実行
- シャットダウン回数、バッテリー購入日時から要交換アラート
- `battery_status=1`: バッテリー充電あり
- `battery_status=0`: バッテリー残量低下

# 利用前設定方法

## USB ポート指定

1. `dmesg | grep tty`で`cp210x connverter`を探す
2. `settings.ini`の`PORT`, `ARDUINO_PORT`にシリアルポートを入力

## スタートアップ登録

1. アプリケーション一覧の検索窓で`session`と検索
2. 自動実行アプリケーション
3. 追加を押して、`start.sh`をスタートアップに登録

### `start.sh`の編集

- `cd /home/USER/ups-battery-manager`でカレントディレクトリを移動しておかないと`settings.ini`を読み込めない
- `python`と`ups-battery-manager.py`を絶対パスで入力する必要があるかも？

PC 再起動テスト後、`ps -aux | grep ups`でプロセス要確認

TODO:

# 開発環境

## Install & Run

```
./start.sh
```

## Requirements

- Pyserial

## Build

TODO:
