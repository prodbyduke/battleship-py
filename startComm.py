# se vogliamo iniziare la comunicazione dovremmo mandare un pacchetto con "NC"
from packetSender import send
from packetReceiver import listenJustOnce
from packetReceiver import startListening

def startComunication():
    msg = "NC, player1, 6969" #NC per la connessione, il nostro nome utente e la porta do0ve ascoltiamo così che l'altro possa salvarla

    if send(msg, "127.0.0.1", 6969): #dobbiamo avere l'ip del destinatario e la porta su cui manderemo i messaggi
        returnedMsg = listenJustOnce()
        splittedMsg = returnedMsg.split(", ")
        if(splittedMsg[0] == "RC"):
            if(splittedMsg[1] == "true"):
                print("inizia la comunicazione")
        print("success")
    else: 
        print("not success :(")

# quando invio il pacchetto aspetto la risposta per capire se vuole connettersi o no
#packetReceiver.receiveConnection() # il metodo ancora non esiste però lo farò successivamente