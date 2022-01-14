import ThreadWait 
import ThreadMain
from threading import Thread

#questo è il thread che aspetterà ogni pacchetto 
tInfinite = Thread(target= ThreadWait.RicezionePacchetti)
tMain = Thread(target= ThreadMain.main)
tInfinite.start()
#questo è il thread main
tMain.start()