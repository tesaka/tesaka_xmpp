# -*- coding:utf-8 -*-
<<<<<<< HEAD
#XMPPãƒ¡ãƒƒã‚»ãƒ¼ã‚¸ã‚’å—ä¿¡ã—ãŸã‚‰ä»»æ„æ–‡å­—ã‚’è¿”ä¿¡ã™ã‚‹ã‚µãƒ³ãƒ—ãƒ«

#xmppãƒ©ã‚¤ãƒ–ãƒ©ãƒªã®ã‚¤ãƒ³ãƒãƒ¼ãƒˆ
import xmpp 

#JIDã‚’æŒ‡å®š
=======
#XMPPƒƒbƒZ[ƒW‚ðŽóM‚µ‚½‚ç”CˆÓ•¶Žš‚ð•ÔM‚·‚éƒTƒ“ƒvƒ‹

#xmppƒ‰ƒCƒuƒ‰ƒŠ‚ÌƒCƒ“ƒ|[ƒg
import xmpp 

#JID‚ðŽw’è
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
user="tesaka2@altair" 
password="tesaka2" 
server="altair"
jid = xmpp.JID(user) 
 
<<<<<<< HEAD
#ãƒãƒ³ãƒ‰ãƒ©ã®å®šç¾©
def message_handler(connect_object, message_node):
	mess_body=str(message_node.getBody())
	#chatstateså—ä¿¡æ™‚ã«ã‚‚ãƒãƒ³ãƒ‰ãƒ©ãŒå‹•ä½œã™ã‚‹ã®ã§Ifåˆ†å²ã§ãµã‚‹ã„ã«ã‹ã‘ã‚‹
	if mess_body == "None":
		pass
	else:
		#å—ä¿¡ãƒ¡ãƒƒã‚»ãƒ¼ã‚¸ã‚’æ¨™æº–å‡ºåŠ›ã«è¡¨ç¤º
		print message_node.getBody()
		#ä»»æ„ã®æ–‡å­—åˆ—ã‚’å…¥åŠ›
		message	=	raw_input("Enter reply:")
		#å…¥åŠ›æ–‡å­—åˆ—ã‚’å—ä¿¡ãƒ¡ãƒƒã‚»ãƒ¼ã‚¸ã®é€ä¿¡å…ƒã«è¿”ä¿¡
		connect_object.send( xmpp.Message( message_node.getFrom(),message)) 


#XMPPã‚µãƒ¼ãƒã«æŽ¥ç¶š
connection = xmpp.Client(server,debug=[]) 
#debugãƒ¢ãƒ¼ãƒ‰
=======
#ƒnƒ“ƒhƒ‰‚Ì’è‹`
def message_handler(connect_object, message_node):
	mess_body=str(message_node.getBody())
	#chatstatesŽóMŽž‚É‚àƒnƒ“ƒhƒ‰‚ª“®ì‚·‚é‚Ì‚ÅIf•ªŠò‚Å‚Ó‚é‚¢‚É‚©‚¯‚é
	if mess_body == "None":
		pass
	else:
		#ŽóMƒƒbƒZ[ƒW‚ð•W€o—Í‚É•\Ž¦
		print message_node.getBody()
		#”CˆÓ‚Ì•¶Žš—ñ‚ð“ü—Í
		message	=	raw_input("Enter reply:")
		#“ü—Í•¶Žš—ñ‚ðŽóMƒƒbƒZ[ƒW‚Ì‘—MŒ³‚É•ÔM
		connect_object.send( xmpp.Message( message_node.getFrom(),message)) 


#XMPPƒT[ƒo‚ÉÚ‘±
connection = xmpp.Client(server,debug=[]) 
#debugƒ‚[ƒh
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
#connection = xmpp.Client(server) 
connection.connect() 
result = connection.auth(jid.getNode(), password, "bbot-client")

<<<<<<< HEAD
#messageã‚¹ã‚¿ãƒ³ã‚¶ã‚’å—ä¿¡ã—ãŸã‚‰ãƒãƒ³ãƒ‰ãƒ©ãŒå‹•ä½œã™ã‚‹ 
connection.RegisterHandler('message', message_handler) 

#Presenseã‚¹ã‚¿ãƒ³ã‚¶ã®é€ä¿¡
connection.sendInitPresence() 

#Pythonã‚’ç¶™ç¶šç¨¼å‹•ã•ã›ã‚‹ãŸã‚ã«ç„¡é™ãƒ«ãƒ¼ãƒ—
=======
#messageƒXƒ^ƒ“ƒU‚ðŽóM‚µ‚½‚çƒnƒ“ƒhƒ‰‚ª“®ì‚·‚é 
connection.RegisterHandler('message', message_handler) 

#PresenseƒXƒ^ƒ“ƒU‚Ì‘—M
connection.sendInitPresence() 

#Python‚ðŒp‘±‰Ò“®‚³‚¹‚é‚½‚ß‚É–³ŒÀƒ‹[ƒv
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
while connection.Process(1):

	pass