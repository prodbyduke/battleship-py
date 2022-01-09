import data
import socket
from threading import Thread
from startComm import answerStartComm
from comunicazione import answerShoot

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((data.LOCALIP, data.LISTENPORT))

def ThreadWait():
    print("Sono pronto a ricevere")
    bytesAddressPair = UDPServerSocket.recvfrom(data.BUFFERSIZE)
    message = bytesAddressPair[0] #nella prima parte ci sarà il mesaggio e nella seconda l'ip 
    formattedMsg = format(message)
    splittedMsg = formattedMsg.split(", ")
    #questo switch controllerà la prima parte del paccheto e in base a quella richiamerà dei metodi
    match splittedMsg[0]: 
        case "NC":
            result = answerStartComm(data.notBusy) #devo inviare la risposta al destinatario, se sono occupato gli manderò false così possiamo connetterci 
            return result
        case "H": 
            shootResult = "" #qui richiamero il metodo che mi dirà se sono stato colpito oppure no
            chk = answerShoot(shootResult);
            return chk
        case "D": 
            closeGame(); #metodo che chiuderà il gioco

#questo thread sarà quello che aspetterà per tutta la partita dei pacchetti
#ricevo pacchetti e in base a cosa sono Es.("NC") avrò uno switch con i casi e mi richiamerà i metodi necessari
