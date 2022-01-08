import data
import socket


UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((data.LOCALIP, data.LISTENPORT))

#quiesto thread sarà quello che aspetterà per tutta la partita dei pacchetti
#ricevo pacchetti e in base a cosa sono Es.("NC") avrò uno switch con i casi e mi richiamerà i metodi necessari
