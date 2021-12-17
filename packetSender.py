import socket

msgFromMe = "prova"
bytesToSend = str.encode(msgFromMe) #converto il mesaggio in byte 
serverAddressPort = ("127.0.0.1", 20001) #dovremo usare due porte diverse (per ora le teniamo uguali)
bufferSize = 1024

# Creo la socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# invio all'altro peer il messaggio
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
#ricevo il mesaggio di risposta (per testare la comunicazione)
answerReceived = UDPClientSocket.recvfrom(bufferSize)

msg = "Message {}".format(answerReceived[0])

print(msg)
