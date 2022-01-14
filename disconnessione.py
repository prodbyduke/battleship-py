import imp
from xmlrpc.client import boolean
from packetSender import send
import data
#import packetReceiver

#immagino che questa funzione sarà richiamata da un bottone 
def disconnect(messaggio:boolean):
    msg = "D, " #D per disconnettersi 
    msg += str(messaggio)

    if send(msg, data.opponentIP, data.LISTENPORT): #dobbiamo avere l'ip del destinatario e la porta su cui manderemo i messaggi
        print("success")
    else: 
        print("not success :(")

    # se invio il pacchetto devo aspettare la risposta 
    #packetReceiver.receiveConnection() # il metodo ancora non esiste però lo farò successivamente
