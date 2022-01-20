from email.headerregistry import Address
import socket

def send(msg, ip, porta):
    # Creo la socket
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    bytesToSend = str.encode(msg)  # converto il mesaggio in byte
    otherAdress = (ip, porta)

    # invio all'altro peer il messaggio
    UDPClientSocket.sendto(bytesToSend, otherAdress)
    print("inviato")
    return True

# ricevo il mesaggio di risposta (per testare la comunicazione)
#answerReceived = UDPClientSocket.recvfrom(bufferSize)
#msg = "Message {}".format(answerReceived[0])
# print(msg)
