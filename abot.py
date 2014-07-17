# -*- coding:utf-8 -*-
<<<<<<< HEAD
#XMPPãƒ¡ãƒƒã‚»ãƒ¼ã‚¸ã‚’å—ä¿¡ã—ãŸã‚‰ç‰¹å®šæ–‡å­—åˆ—ã‚’è¿”ã™ã‚µãƒ³ãƒ—ãƒ«

#xmppãƒ©ã‚¤ãƒ–ãƒ©ãƒªã®ã‚¤ãƒ³ãƒãƒ¼ãƒˆ
import xmpp 

#JIDã‚’æŒ‡å®š
=======
#XMPPƒƒbƒZ[ƒW‚ðŽóM‚µ‚½‚ç“Á’è•¶Žš—ñ‚ð•Ô‚·ƒTƒ“ƒvƒ‹

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
=======
#ƒnƒ“ƒhƒ‰‚Ì’è‹`
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
def message_handler(connect_object, message_node): 

	message	=	"Welcome to my first Bot:)"
	connect_object.send( xmpp.Message( message_node.getFrom(),message)) 

<<<<<<< HEAD
#XMPPã‚µãƒ¼ãƒã«æŽ¥ç¶š
connection = xmpp.Client(server,debug=[]) 
#debugãƒ¢ãƒ¼ãƒ‰
=======
#XMPPƒT[ƒo‚ÉÚ‘±
connection = xmpp.Client(server,debug=[]) 
#debugƒ‚[ƒh
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
#connection = xmpp.Client(server) 
connection.connect() 
result = connection.auth(jid.getNode(), password, "abot-client")

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