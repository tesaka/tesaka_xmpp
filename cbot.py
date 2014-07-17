# -*- coding:utf-8 -*-
<<<<<<< HEAD
#XMPPãƒ¡ãƒƒã‚»ãƒ¼ã‚¸ã‚’å—ä¿¡ã—ãŸã‚‰ä»»æ„æ–‡å­—ã‚’è¿”ä¿¡ã™ã‚‹ã‚µãƒ³ãƒ—ãƒ«(é€£ç¶šå—ä¿¡å¯èƒ½)

#ãƒ©ã‚¤ãƒ–ãƒ©ãƒªã®ã‚¤ãƒ³ãƒãƒ¼ãƒˆ
=======
#XMPPƒƒbƒZ[ƒW‚ðŽóM‚µ‚½‚ç”CˆÓ•¶Žš‚ð•ÔM‚·‚éƒTƒ“ƒvƒ‹(˜A‘±ŽóM‰Â”\)

#ƒ‰ƒCƒuƒ‰ƒŠ‚ÌƒCƒ“ƒ|[ƒg
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
import threading
import sys
import xmpp 

<<<<<<< HEAD
#JIDã‚’æŒ‡å®š
=======
#JID‚ðŽw’è
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
user="tesaka2@altair" 
password="tesaka2" 
server="altair"
jid = xmpp.JID(user) 

<<<<<<< HEAD
#è¿”ä¿¡ç”¨ã®é–¢æ•°reply_messã®å®šç¾©
=======
#•ÔM—p‚ÌŠÖ”reply_mess‚Ì’è‹`
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
def reply_mess():
	message	=	raw_input()
	conn_obj.send( xmpp.Message( mess_node.getFrom(),message)) 
 
<<<<<<< HEAD
#ãƒãƒ³ãƒ‰ãƒ©ã®å®šç¾©
def message_handler(connect_object, message_node): 
	#ã‚°ãƒ­ãƒ¼ãƒãƒ«å¤‰æ•°ã®å®šç¾©
	global mess_body
	global conn_obj
	global mess_node
	#ã‚°ãƒ­ãƒ¼ãƒãƒ«å¤‰æ•°ã«ä»£å…¥
	mess_body=str(message_node.getBody())
	conn_obj=connect_object
	mess_node=message_node
	#chatstateså—ä¿¡æ™‚ã«ã‚‚ãƒãƒ³ãƒ‰ãƒ©ãŒå‹•ä½œã™ã‚‹ã®ã§Ifåˆ†å²ã§ãµã‚‹ã„ã«ã‹ã‘ã‚‹
	if mess_body == "None":
		pass
	else:
		#ã‚¹ãƒ¬ãƒƒãƒ‰ã‚’ãƒ•ã‚©ãƒ¼ã‚¯ã—ã¦reply_messé–¢æ•°ã‚’å®Ÿè¡Œã•ã›ã‚‹
		thread = threading.Thread(target=reply_mess)
		thread.daemon = True
		thread.start()
		#å—ä¿¡ãƒ¡ãƒƒã‚»ãƒ¼ã‚¸ã‚’æ¨™æº–å‡ºåŠ›ã«è¡¨ç¤º
=======
#ƒnƒ“ƒhƒ‰‚Ì’è‹`
def message_handler(connect_object, message_node): 
	#ƒOƒ[ƒoƒ‹•Ï”‚Ì’è‹`
	global mess_body
	global conn_obj
	global mess_node
	#ƒOƒ[ƒoƒ‹•Ï”‚É‘ã“ü
	mess_body=str(message_node.getBody())
	conn_obj=connect_object
	mess_node=message_node
	#chatstatesŽóMŽž‚É‚àƒnƒ“ƒhƒ‰‚ª“®ì‚·‚é‚Ì‚ÅIf•ªŠò‚Å‚Ó‚é‚¢‚É‚©‚¯‚é
	if mess_body == "None":
		pass
	else:
		#ƒXƒŒƒbƒh‚ðƒtƒH[ƒN‚µ‚Äreply_messŠÖ”‚ðŽÀs‚³‚¹‚é
		thread = threading.Thread(target=reply_mess)
		thread.daemon = True
		thread.start()
		#ŽóMƒƒbƒZ[ƒW‚ð•W€o—Í‚É•\Ž¦
>>>>>>> fd904b3cedf18d496782c1023722d72c3c01bd1c
		sys.stdout.write("\r\n")
		print mess_body
		sys.stdout.write("Enter reply:")

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
result = connection.auth(jid.getNode(), password, "cbot-client")

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