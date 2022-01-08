import socket
from packetSender import send
import data

otherAdress = ("", 0)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((data.LOCALIP, data.LISTENPORT))

#metodo che aspetta un pacchetto per l'inizio della comunicazione 
def waitPacket():
    print("Sono pronto a ricevere")
    bytesAddressPair = UDPServerSocket.recvfrom(data.BUFFERSIZE)
    message = bytesAddressPair[0] #nella prima parte ci sarà il mesaggio e nella seconda l'ip 
    formattedMsg = format(message)
    splittedMsg = formattedMsg.split(", ")
    print(formattedMsg)
    #questo è l'indirizzo con ip e porta dell'altro peer 
    otherAdress = (splittedMsg[1], splittedMsg[2])
    #se la prima parte del messaggio splittato è NC allora inizio la comunicazione 
    if(splittedMsg[0] == "NC"):
        msgToSend = "RC, "  # messaggio da inviare come prova per vedere se funziona
        msgToSend += str(True) # dico all'altro che voglio iniziare la comunicazione
        msgToSend += ", kiroxy" #invio il nome utente 
        bytesToSend = str.encode(msgToSend)
        UDPServerSocket.sendto(bytesToSend, otherAdress)
        #l'idea è quella di fare un altro metodo che sia sempre attivo finchè non ricevo la stringa di chiusura
        print("connessione stabilita")
        startListening()
    #incomingMsg = "Message from the other peer:{}". formattedMsg # ricevo il messaggio dell'altro peer
    # ricevo l'IP dell'altro peer che mi servirà solo durante la connessione
    #print(incomingMsg)
    print(splittedMsg)
#questo sarebbe il metodo che sta sempre attivo e riceve pacchetti (non sono sicuro di usarlo però)
def startListening():
    while True:
        print("Continuo la comunicazione")
        bytesAddressPair = UDPServerSocket.recvfrom(data.BUFFERSIZE)
        message = bytesAddressPair[0] 
        formattedMsg = format(message)
        splittedMsg = formattedMsg.split(", ")
        if splittedMsg[0] == "D" : 
            break
#questo metodo serve solo per aspettare una risposta singola (per esempio quando inizio la comunicazione)
def listenJustOnce():
    print("Aspetto la risposta")
    bytesAddressPair = UDPServerSocket.recvfrom(data.BUFFERSIZE)
    message = bytesAddressPair[0] 
    formattedMsg = format(message)
    return formattedMsg 
        
