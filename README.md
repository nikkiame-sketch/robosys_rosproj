# 2021年度 ロボットシステム学課題２

ある体積の液体を任意のグラスに注いだ時の液面の高さを計算するプログラムです。

ロボットが液体をグラスに注ぐようなケースを想定して製作しました。

このプログラムにより、画像等から液面の高ささえ計測することが出来れば、体積や重量を計測するセンサがなくても概ね一定量を注ぐことが出来ます

円錐台形または円柱形のグラスに対応しています。



授業で扱った上田先生 （https://github.com/ryuichiueda) のプログラムに必要な処理を追記させていただき製作しています。

動作環境:Raspberry pi 3b,ubuntu20.04LTS




## 実行方法

### 1：amount.py内の次の設定を書き換える

  1.1 グラスのサイズの定義
  
    70行目のglassクラスのインスタンス生成の際の3つの引数の値がグラスのサイズ。
    第1引数から順に、グラスの底の直径、グラスの上部の直径、グラスの高さ
    
  1.2 パブリッシャーの設定（必要に応じて）
  
    67行目の'input'の部分を任意のパブリッシャーに変更する
    
    
### 2：amount.pyを実行する

  2.1 端末１から以下のコマンドでrosを立ち上げる
  ```
  roscore
  ```
  
  2.2 端末２からamount.pyを起動する
  ```
  chmod +x amount.py
  rosrun mypkg amount.py
  ```
  
  2.3 端末３でamount.pyの出力を表示する
  ```
  rostopic echo /amount
  ```
  
  2.3 パブリッシャーを通じて液量(ml)を渡すと、液面の高さ（mm）が出力される
  
  
