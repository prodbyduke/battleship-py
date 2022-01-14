import data
from startComm import answerStartComm, receiveAnswer
from comunicazione import answerShoot

def RicezionePacchetti():
    data.creaSocket()
    print("Sono pronto a ricevere")
    while True :
        bytesAddressPair = data.UDPServerSocket.recvfrom(data.BUFFERSIZE)
        message = bytesAddressPair[0] #nella prima parte ci sarà il mesaggio e nella seconda l'ip 
        formattedMsg = format(message)
        splittedMsg = formattedMsg.split(", ")
        #questo switch controllerà la prima parte del paccheto e in base a quella richiamerà dei metodi
        if splittedMsg[0] == "NC":
            answerStartComm(data.notBusy) #devo inviare la risposta al destinatario, se sono occupato gli manderò false così possiamo connetterci
            data.turn = 0;
        elif splittedMsg[0] == "H": 
            shootResult = data.shootResult(splittedMsg[1]) #invio al metodo le coordinate e mi aspetto che mi dia -1, 0 o 1
            chk = answerShoot(shootResult)
            data.turn = 1; #imposto il turno a 1 per dire che è il nostro turno
            data.changeTurn() #metodo che serve per cambiare il turno graficamente
        elif splittedMsg[0] == "D": 
            data.closeGame() #metodo che chiuderà il gioco
        elif splittedMsg[0] == "RC": 
            data.turn = 1
            receiveAnswer(splittedMsg[1])
            

#questo thread sarà quello che aspetterà per tutta la partita dei pacchetti
#ricevo pacchetti e in base a cosa sono Es.("NC") avrò uno switch con i casi e mi richiamerà i metodi necessari
