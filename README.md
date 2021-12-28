# 2021年度 ロボットシステム学課題２

グラス内の液面の高さから、液体の体積を算出するプログラムです。

ロボットが液体をグラスに注ぐようなケースを想定して製作しました。

円錐台形または円柱形のグラスに対応しています。



授業で扱った上田先生（https://github.com/ryuichiueda)のプログラムに必要な処理を追記する形で製作しています。

動作環境:Raspberry pi 3b,ubuntu20.04LTS




## 実行方法

### 1：amount.py内の次の設定を書き換える

  1.1 グラスのサイズの定義
  
    70行目のglassクラスのインスタンス生成の際の3つの引数の値がグラスのサイズ。
    第1引数から順に、グラスの底の直径、グラスの上部の直径、グラスの高さ
    
  1.2 パブリッシャーの設定
  
    67行目の'count_up'の部分を任意のパブリッシャーに変更する
    
    
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
  
  2.3 先ほど登録したパブリッシャーを起動する
  
  
