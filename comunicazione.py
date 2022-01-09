from packetSender import send
from packetReceiver import listenJustOnce
import data

rispostaColpo = ""

def sendAttack(cella):
    msg = "H," 
    msg += cella

    if send(msg, data.opponentIP, data.LISTENPORT): #dobbiamo avere l'ip del destinatario e la porta su cui manderemo i messaggi
        print("success")
        return True
    else: 
        print("not success :(")

def waitResponse():
    returnedMsg = listenJustOnce()
    return returnedMsg

def answerShoot(shootResult):
    msg = "RH, "
    msg += str(shootResult)
    if send(msg, data.opponentIP, data.LISTENPORT):
        print("answer sent")
        return True
    return False
