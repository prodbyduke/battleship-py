from packetSender import send
from packetReceiver import listenJustOnce

rispostaColpo = ""

def sendAttack(cella):
    msg = "H," 
    msg += cella

    if send(msg, "127.0.0.1", 6969): #dobbiamo avere l'ip del destinatario e la porta su cui manderemo i messaggi
        print("success")
        return True
    else: 
        print("not success :(")

def waitResponse():
    returnedMsg = listenJustOnce()
    return returnedMsg
