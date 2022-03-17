import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json
import pprint

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
NUM_WORKERS=4

#Versione 1 
def genera_richieste1(num,address,port):
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()

    #1. Generazione casuale:
    #   di uno studente (valori ammessi: 5 cognomi a caso tra cui il tuo cognome)
    #   di una materia (valori ammessi: Matematica, Italiano, inglese, Storia e Geografia)
    #   di un voto (valori ammessi 1 ..10)
    #   delle assenze (valori ammessi 1..5) 
    studenti=random.randint(0,4)
    voto=random.randint(1,10)
    assenze=random.randint(1,5)
    if(studenti==0):
        stu="Rossi"
    elif(studenti==1):
        stu="Iannucci"
    elif(studenti==2):
        stu="Bianchi"
    elif(studenti==3):
        stu="Verdi"
    else:
        stu="Esposito"
    materia=random.randint(0,4)
    if(materia==0):
        mat="Matematica"
    elif(materia==1):
        mat="Storia"
    elif(materia==2):
        mat="Italiano"
    elif(materia==3):
        mat="Geografia"
    else:
        mat="Inglese"
        print(f"{studenti}{mat}{stu}{voto}{assenze}")
    voto=random.randint(1,10)
    assenze=random.randint(1,5)
    #2. comporre il messaggio, inviarlo come json
    #   esempio: {'studente': 'Studente4', 'materia': 'Italiano', 'voto': 2, 'assenze': 3}
    messaggio= {'studenti': 'Bianchi', 'materia': 'Italiano', 'voto': 2, 'assenze': 3}
    #3. ricevere il risultato come json: {'studente':'Studente4','materia':'italiano','valutazione':'Gravemente insufficiente'}
    data=json.dumps(messaggio)
    sock_service.sendall(data.encode("UTF-8"))
    data=sock_service.recv(1024)
    
    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        print(f"{threading.current_thread().name} : Risultato: {data.decode()}")
        #4 stampare la valutazione ricevuta esempio: La valutazione di Studente4 in italiano è Gravemente insufficiente
    s.close()
    end_time_thread=time.time()
    print(f"{threading.current_thread().name} tempo di esecuzione time=", end_time_thread-start_time_thread)

if __name__ == '__main__':
    start_time=time.time()
    # PUNTO A) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)
    # alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    # PUNTO B) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)  
    # tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i thread e attenderne la fine
    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    process=[]
    # PUNTO C) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3) 
    # tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i processi e attenderne la fine
    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)
