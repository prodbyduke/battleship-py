# se vogliamo iniziare la comunicazione dovremmo mandare un pacchetto con "NC"
import packetSender
import packetReceiver

msg = "" 
msg += "NC, player1, 6969" #NC per la connessione, il nostro nome utente e la porta do0ve ascoltiamo così che l'altro possa salvarla

if packetSender.send(msg, "127.0.0.1", 20001): #dobbiamo avere l'ip del destinatario e la porta su cui manderemo i messaggi
    print("success")
else: 
    print("not success :(")

# quando invio il pacchetto aspetto la risposta per capire se vuole connettersi o no
packetReceiver.receiveConnection() # il metodo ancora non esiste però lo farò successivamente