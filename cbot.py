# -*- coding:utf-8 -*-
<<<<<<< HEAD
#XMPPメッセージを受信したら任意文字を返信するサンプル(連続受信可能)

#ライブラリのインポート
=======
#XMPP���b�Z�[�W����M������C�ӕ�����ԐM����T���v��(�A����M�\)

#���C�u�����̃C���|�[�g
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
import threading
import sys
import xmpp 

<<<<<<< HEAD
#JIDを指定
=======
#JID���w��
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
user="tesaka2@altair" 
password="tesaka2" 
server="altair"
jid = xmpp.JID(user) 

<<<<<<< HEAD
#返信用の関数reply_messの定義
=======
#�ԐM�p�̊֐�reply_mess�̒�`
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
def reply_mess():
	message	=	raw_input()
	conn_obj.send( xmpp.Message( mess_node.getFrom(),message)) 
 
<<<<<<< HEAD
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
=======
#�n���h���̒�`
def message_handler(connect_object, message_node): 
	#�O���[�o���ϐ��̒�`
	global mess_body
	global conn_obj
	global mess_node
	#�O���[�o���ϐ��ɑ��
	mess_body=str(message_node.getBody())
	conn_obj=connect_object
	mess_node=message_node
	#chatstates��M���ɂ��n���h�������삷��̂�If����łӂ邢�ɂ�����
	if mess_body == "None":
		pass
	else:
		#�X���b�h���t�H�[�N����reply_mess�֐������s������
		thread = threading.Thread(target=reply_mess)
		thread.daemon = True
		thread.start()
		#��M���b�Z�[�W��W���o�͂ɕ\��
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
		sys.stdout.write("\r\n")
		print mess_body
		sys.stdout.write("Enter reply:")

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
result = connection.auth(jid.getNode(), password, "cbot-client")

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