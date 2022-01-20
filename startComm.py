# se vogliamo iniziare la comunicazione dovremmo mandare un pacchetto con "NC"
from packetSender import send
import data

def startComunication():
    msg = "NC, " + data.player1.name #NC per la connessione, il nostro nome utente 
    if send(msg, data.tempIp, data.LISTENPORT): #dobbiamo avere l'ip del destinatario e la porta su cui manderemo i messaggi
        print("Communication requested")
    else: 
        print("Error")

def receiveAnswer(risposta):
    if(risposta == "True"): #ricevo una stringa quindi devo controllare la stringa e non il booleano
        data.opponentIP = data.tempIp
        data.ready = True
        print("Communication accepted")
    else:
        print("Communication refused")

def answerStartComm(busy): #busy mi dirà se siamo occupati o pure no con un altro utente
    msg = "RC, "
    msg += str(busy) + ", " + data.player1.name
    if send(msg, data.opponentIP, data.LISTENPORT):
        print("Replied")
        return True
    return False

# quando invio il pacchetto aspetto la risposta per capire se vuole connettersi o no
#packetReceiver.receiveConnection() # il metodo ancora non esiste però lo farò successivamente