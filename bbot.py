# -*- coding:utf-8 -*-
<<<<<<< HEAD
#XMPPメッセージを受信したら任意文字を返信するサンプル

#xmppライブラリのインポート
import xmpp 

#JIDを指定
=======
#XMPP���b�Z�[�W����M������C�ӕ�����ԐM����T���v��

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
=======
#�n���h���̒�`
def message_handler(connect_object, message_node):
	mess_body=str(message_node.getBody())
	#chatstates��M���ɂ��n���h�������삷��̂�If����łӂ邢�ɂ�����
	if mess_body == "None":
		pass
	else:
		#��M���b�Z�[�W��W���o�͂ɕ\��
		print message_node.getBody()
		#�C�ӂ̕���������
		message	=	raw_input("Enter reply:")
		#���͕��������M���b�Z�[�W�̑��M���ɕԐM
		connect_object.send( xmpp.Message( message_node.getFrom(),message)) 


#XMPP�T�[�o�ɐڑ�
connection = xmpp.Client(server,debug=[]) 
#debug���[�h
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
#connection = xmpp.Client(server) 
connection.connect() 
result = connection.auth(jid.getNode(), password, "bbot-client")

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