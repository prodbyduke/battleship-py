# se vogliamo iniziare la comunicazione dovremmo mandare un pacchetto con "NC"
from packetSender import send
from packetReceiver import listenJustOnce
import data

def startComunication():
    msg = "NC, playerX" #NC per la connessione, il nostro nome utente 
    if send(msg, data.opponentIP, data.LISTENPORT): #dobbiamo avere l'ip del destinatario e la porta su cui manderemo i messaggi
        print("success")
    else: 
        print("not success :(")

def receiveAnswer(risposta):
    if(risposta == "True"): #ricevo una stringa quindi devo controllare la stringa e non il booleano
        #chiamerà un metodo che farà iniziare il gioco 
        print("inizia la comunicazione")

def answerStartComm(busy): #busy mi dirà se siamo occupati o pure no con un altro utente
    msg = "RC, "
    msg += str(busy)
    msg += ", playerX"
    if send(msg, data.opponentIP, data.LISTENPORT):
        print("answer sent")
        return True
    return False

# quando invio il pacchetto aspetto la risposta per capire se vuole connettersi o no
#packetReceiver.receiveConnection() # il metodo ancora non esiste però lo farò successivamente