# conf.d
紛らわしいですが、"swatch" のconfigを置くところです。<Br>
slack webhook関連はscriptsディレクトリです。

# swatchについて
  swatch(Simple WATCHDOG): linuxの各種ログを監視するスクリプトだそうです。<br>
  監視しているログに特定の文字列パターンを見つけた際に、指定したアクションを実行することができます。<br>
  [詳しくはこちら](https://ja.linux-console.net/?p=238)
  
# auth.log.conf
  ubuntuでsshのログが保存されるauth.logを監視するconfigファイルです。<br>
  認証成功時、およびパターン別の認証失敗時の動作を定義しています。  
