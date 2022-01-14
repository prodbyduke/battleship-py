import data

#questo metodo serve solo per aspettare una risposta singola (per esempio quando inizio la comunicazione)
def listenJustOnce():
    print("Aspetto la risposta")
    bytesAddressPair = data.UDPServerSocket.recvfrom(data.BUFFERSIZE)
    message = bytesAddressPair[0] 
    formattedMsg = format(message)
    return formattedMsg 
        
