import socket
from packetSender import send
import data

otherAdress = ("", 0)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((data.LOCALIP, data.LISTENPORT))

#questo metodo serve solo per aspettare una risposta singola (per esempio quando inizio la comunicazione)
def listenJustOnce():
    print("Aspetto la risposta")
    bytesAddressPair = UDPServerSocket.recvfrom(data.BUFFERSIZE)
    message = bytesAddressPair[0] 
    formattedMsg = format(message)
    return formattedMsg 
        
