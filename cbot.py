# -*- coding:utf-8 -*-
#XMPP���b�Z�[�W����M������C�ӕ�����ԐM����T���v��(�A����M�\)

#���C�u�����̃C���|�[�g
import threading
import sys
import xmpp 

#JID���w��
user="tesaka2@altair" 
password="tesaka2" 
server="altair"
jid = xmpp.JID(user) 

#�ԐM�p�̊֐�reply_mess�̒�`
def reply_mess():
	message	=	raw_input()
	conn_obj.send( xmpp.Message( mess_node.getFrom(),message)) 
 
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
		sys.stdout.write("\r\n")
		print mess_body
		sys.stdout.write("Enter reply:")

#XMPP�T�[�o�ɐڑ�
connection = xmpp.Client(server,debug=[]) 
#debug���[�h
#connection = xmpp.Client(server) 
connection.connect() 
result = connection.auth(jid.getNode(), password, "cbot-client")

#message�X�^���U����M������n���h�������삷�� 
connection.RegisterHandler('message', message_handler) 

#Presense�X�^���U�̑��M
connection.sendInitPresence() 

#Python���p���ғ������邽�߂ɖ������[�v
while connection.Process(1):

	pass