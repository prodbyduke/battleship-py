import socket

bufferSize = 1024
# Creo la socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

def send(msg, ip, porta):
    bytesToSend = str.encode(msg)  # converto il mesaggio in byte
    # dovremo usare due porte diverse (per ora le teniamo uguali)
    serverAddressPort = (ip, porta)

    # invio all'altro peer il messaggio
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    return True
# ricevo il mesaggio di risposta (per testare la comunicazione)
#answerReceived = UDPClientSocket.recvfrom(bufferSize)
#msg = "Message {}".format(answerReceived[0])
# print(msg)
