import packetSender
import packetReceiver

msg = "D, " #D per disconnettersi 
msg += str(True)

if packetSender.send(msg, "127.0.0.1", 20001): #dobbiamo avere l'ip del destinatario e la porta su cui manderemo i messaggi
    print("success")
else: 
    print("not success :(")

# se invio il pacchetto devo aspettare la risposta 
packetReceiver.receiveConnection() # il metodo ancora non esiste però lo farò successivamente