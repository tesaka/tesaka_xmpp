# -*- coding:utf-8 -*-
<<<<<<< HEAD
#XMPPメッセージを受信したら特定文字列を返すサンプル

#xmppライブラリのインポート
import xmpp 

#JIDを指定
=======
#XMPP���b�Z�[�W����M��������蕶�����Ԃ��T���v��

#xmpp���C�u�����̃C���|�[�g
import xmpp 

#JID���w��
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
user="tesaka2@altair" 
password="tesaka2" 
server="altair"
jid = xmpp.JID(user) 
 
<<<<<<< HEAD
#ハンドラの定義
=======
#�n���h���̒�`
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
def message_handler(connect_object, message_node): 

	message	=	"Welcome to my first Bot:)"
	connect_object.send( xmpp.Message( message_node.getFrom(),message)) 

<<<<<<< HEAD
#XMPPサーバに接続
connection = xmpp.Client(server,debug=[]) 
#debugモード
=======
#XMPP�T�[�o�ɐڑ�
connection = xmpp.Client(server,debug=[]) 
#debug���[�h
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
#connection = xmpp.Client(server) 
connection.connect() 
result = connection.auth(jid.getNode(), password, "abot-client")

<<<<<<< HEAD
#messageスタンザを受信したらハンドラが動作する
connection.RegisterHandler('message', message_handler) 

#Presenseスタンザの送信
connection.sendInitPresence() 

#Pythonを継続稼動させるために無限ループ
=======
#message�X�^���U����M������n���h�������삷��
connection.RegisterHandler('message', message_handler) 

#Presense�X�^���U�̑��M
connection.sendInitPresence() 

#Python���p���ғ������邽�߂ɖ������[�v
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
while connection.Process(1):

	pass