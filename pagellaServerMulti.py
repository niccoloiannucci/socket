import socket
from threading import Thread
import json


SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225

#Versione 1 
def ricevi_comandi1(sock_service,addr_client):
    while True:
        data=sock_service.recv(1024)
        if not data: 
                break
        data=data.decode()
        data=json.loads(data)        
        #1. recuperare dal json studente, materia, voto e assenze

        #2. restituire un messaggio in json contenente studente, materia e una valutazione testuale :
        # voto < 4 Gravemente insufficiente
        # voto [4..5] Insufficiente
        # voto = 6 Sufficiente
        # voto = 7 Discreto 
        # voto [8..9] Buono
        # voto = 10 Ottimo
        if  (voto<4):
            messaggio="gravemente insufficiente"
        elif(voto>=4 and voto<=5):
            messaggio="insufficiente"
        elif(voto==6)
            messaggio="sufficiente"
        elif(voto>7 and voto<8)
            messaggio="discreto"
        elif(voto>8 and voto<9)
            messaggio="Sufficiente"
        elif(voto==10)
            messaggio="ottimo"
    sock_service.sendall(messaggio.encode("UTF-8"))
    sock_service.close()