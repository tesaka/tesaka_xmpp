# -*- coding:utf-8 -*-
#XMPPメッセージを受信したら特定文字列を返すサンプル

#xmppライブラリのインポート
import xmpp 

#JIDを指定
user="tesaka2@altair" 
password="tesaka2" 
server="altair"
jid = xmpp.JID(user) 
 
#ハンドラの定義
def message_handler(connect_object, message_node): 

	message	=	"Welcome to my first Bot:)"
	connect_object.send( xmpp.Message( message_node.getFrom(),message)) 

#XMPPサーバに接続
connection = xmpp.Client(server,debug=[]) 
#debugモード
#connection = xmpp.Client(server) 
connection.connect() 
result = connection.auth(jid.getNode(), password, "abot-client")

#messageスタンザを受信したらハンドラが動作する
connection.RegisterHandler('message', message_handler) 

#Presenseスタンザの送信
connection.sendInitPresence() 

#Pythonを継続稼動させるために無限ループ
while connection.Process(1):

	pass