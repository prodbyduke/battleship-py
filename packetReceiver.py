import socket
import packetReceiver
localIP = "127.0.0.1"  # da modificare
localPort = 20001  # da modificare
bufferSize = 1024

def receiveConnection():

    return "succes"

peerIP = ""
msgToSend = "Hello peer"  # messaggio da inviare come prova per vedere se funziona
bytesToSend = str.encode(msgToSend)
# Creo un datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Mi collego ad un address e all'ip
UDPServerSocket.bind((localIP, localPort))
print("Sono pronto a ricevere")


# ciclo che aspetta finché non mi arriva un certo tipo di pacchetto
while(message != "D"): #  aspetto finche nel pacchetto non ricevo la stringa D
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0] #nella prima parte ci sarà il mesaggio e nella seconda l'ip 
    address = bytesAddressPair[1]



    incomingMsg = "Message from the other peer:{}".format(message)  # ricevo il messaggio dell'altro peer
    # ricevo l'IP dell'altro peer che mi servirà solo durante la connessione
    peerIP = "Other peer's IP Address:{}".format(address)

    print(incomingMsg)
    print(peerIP)
    # mando la risposta
    UDPServerSocket.sendto(bytesToSend, address)
