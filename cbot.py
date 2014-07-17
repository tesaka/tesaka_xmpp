# -*- coding:utf-8 -*-
#XMPPメッセージを受信したら任意文字を返信するサンプル(連続受信可能)

#ライブラリのインポート
import threading
import sys
import xmpp 

#JIDを指定
user="tesaka2@altair" 
password="tesaka2" 
server="altair"
jid = xmpp.JID(user) 

#返信用の関数reply_messの定義
def reply_mess():
	message	=	raw_input()
	conn_obj.send( xmpp.Message( mess_node.getFrom(),message)) 
 
#ハンドラの定義
def message_handler(connect_object, message_node): 
	#グローバル変数の定義
	global mess_body
	global conn_obj
	global mess_node
	#グローバル変数に代入
	mess_body=str(message_node.getBody())
	conn_obj=connect_object
	mess_node=message_node
	#chatstates受信時にもハンドラが動作するのでIf分岐でふるいにかける
	if mess_body == "None":
		pass
	else:
		#スレッドをフォークしてreply_mess関数を実行させる
		thread = threading.Thread(target=reply_mess)
		thread.daemon = True
		thread.start()
		#受信メッセージを標準出力に表示
		sys.stdout.write("\r\n")
		print mess_body
		sys.stdout.write("Enter reply:")

#XMPPサーバに接続
connection = xmpp.Client(server,debug=[]) 
#debugモード
#connection = xmpp.Client(server) 
connection.connect() 
result = connection.auth(jid.getNode(), password, "cbot-client")

#messageスタンザを受信したらハンドラが動作する 
connection.RegisterHandler('message', message_handler) 

#Presenseスタンザの送信
connection.sendInitPresence() 

#Pythonを継続稼動させるために無限ループ
while connection.Process(1):

	pass