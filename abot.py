# -*- coding:utf-8 -*-
#XMPP���b�Z�[�W����M��������蕶�����Ԃ��T���v��

#xmpp���C�u�����̃C���|�[�g
import xmpp 

#JID���w��
user="tesaka2@altair" 
password="tesaka2" 
server="altair"
jid = xmpp.JID(user) 
 
#�n���h���̒�`
def message_handler(connect_object, message_node): 

	message	=	"Welcome to my first Bot:)"
	connect_object.send( xmpp.Message( message_node.getFrom(),message)) 

#XMPP�T�[�o�ɐڑ�
connection = xmpp.Client(server,debug=[]) 
#debug���[�h
#connection = xmpp.Client(server) 
connection.connect() 
result = connection.auth(jid.getNode(), password, "abot-client")

#message�X�^���U����M������n���h�������삷��
connection.RegisterHandler('message', message_handler) 

#Presense�X�^���U�̑��M
connection.sendInitPresence() 

#Python���p���ғ������邽�߂ɖ������[�v
while connection.Process(1):

	pass