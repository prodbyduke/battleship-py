from packetSender import send
from packetReceiver import listenJustOnce

global_rispostaColpo = ""

def sendAttack():
    msg = "" 
    msg += "H, a-1" #H per la l'hit e poi le coordinate

    if send(msg, "127.0.0.1", 6969): #dobbiamo avere l'ip del destinatario e la porta su cui manderemo i messaggi
        returnedMsg = listenJustOnce()
        splittedMsg = returnedMsg.split(", ")
        if(splittedMsg[0] == "RH"):
            global_rispostaColpo = splittedMsg[1] #questa variabile servirà ad un altro file per capire se abbiamo colpito ecc...
        print("success")
    else: 
        print("not success :(")

# se invio il pacchetto devo aspettare la risposta 
    #packetReceiver.receiveConnection() # il metodo ancora non esiste però lo farò successivamente

sendAttack()