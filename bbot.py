# -*- coding:utf-8 -*-
#XMPPメッセージを受信したら任意文字を返信するサンプル

#xmppライブラリのインポート
import xmpp 

#JIDを指定
user="tesaka2@altair" 
password="tesaka2" 
server="altair"
jid = xmpp.JID(user) 
 
#ハンドラの定義
def message_handler(connect_object, message_node):
	mess_body=str(message_node.getBody())
	#chatstates受信時にもハンドラが動作するのでIf分岐でふるいにかける
	if mess_body == "None":
		pass
	else:
		#受信メッセージを標準出力に表示
		print message_node.getBody()
		#任意の文字列を入力
		message	=	raw_input("Enter reply:")
		#入力文字列を受信メッセージの送信元に返信
		connect_object.send( xmpp.Message( message_node.getFrom(),message)) 


#XMPPサーバに接続
connection = xmpp.Client(server,debug=[]) 
#debugモード
#connection = xmpp.Client(server) 
connection.connect() 
result = connection.auth(jid.getNode(), password, "bbot-client")

#messageスタンザを受信したらハンドラが動作する 
connection.RegisterHandler('message', message_handler) 

#Presenseスタンザの送信
connection.sendInitPresence() 

#Pythonを継続稼動させるために無限ループ
while connection.Process(1):

	pass