import socket
import json
from threading import Thread
from tkinter.tix import INTEGER
SERVER_ADDRESS='127.0.0.1'
SERVER_PORT=22225
class Client():
    """
        Questa calsse rappresenta una persona che opera come client
    """
    def connessione_server(self, address, port):
        """
            Metodo per stabilire la connessione con il server
        """
        sock_service=socket.socket()
        sock_service.connect((address, port))
        print("Connesso  a " + str((address, port)))
        return sock_service
    
    def invia_comandi(self, sock_service):
        """
            Metodo per inviare le richieste di servizio e ricevere le risposte
        """
        while True:
                n1=int(input("Scegliere il p.numero: "))
                n2=int(input("Scegliere il s.numero: "))
                oper=input("Inserisci l'operazione da effettuare: ")
                messaggio={'primoNumero':n1, 'operazione':oper, 'secondoNumero':n2}
                messaggio=json.dumps(messaggio)
                sock_service.sendall(messaggio.encode("UTF-8"))
                data=sock_service.recv(1024)
                print("Risultato: ",data.decode())
c1=Client()
sock_server=c1.connessione_server(SERVER_ADDRESS, SERVER_PORT)
c1.invia_comandi(sock_server)