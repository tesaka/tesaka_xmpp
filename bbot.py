# -*- coding:utf-8 -*-
#XMPP���b�Z�[�W����M������C�ӕ�����ԐM����T���v��

#xmpp���C�u�����̃C���|�[�g
import xmpp 

#JID���w��
user="tesaka2@altair" 
password="tesaka2" 
server="altair"
jid = xmpp.JID(user) 
 
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
#connection = xmpp.Client(server) 
connection.connect() 
result = connection.auth(jid.getNode(), password, "bbot-client")

#message�X�^���U����M������n���h�������삷�� 
connection.RegisterHandler('message', message_handler) 

#Presense�X�^���U�̑��M
connection.sendInitPresence() 

#Python���p���ғ������邽�߂ɖ������[�v
while connection.Process(1):

	pass