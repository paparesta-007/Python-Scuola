import threading
import time
import random

listaPartecipanti = []
listaPunteggioPartecipanti = []
lockPunteggio = threading.Lock()

def creaLista():
    for i in range(1, 11):
        s = "C" + str(i)
        listaPartecipanti.append(s)
        listaPunteggioPartecipanti.append(0)
    print("Lista creata:", listaPartecipanti)

def primaProva(n):
    def prendiPunteggio(index, classifica):
        print(f"Concorrente {listaPartecipanti[index]} attende di iniziare la prima prova")
        time.sleep(random.randint(1, 3))
        print(f"Concorrente {listaPartecipanti[index]} inizia la prima prova")
        tempoAspettato = random.randint(1, 3)
        time.sleep(tempoAspettato)
        with lockPunteggio:
            classifica.append((tempoAspettato, index))
        print(f"Concorrente {listaPartecipanti[index]} termina la prima prova con tempo {tempoAspettato}")
    
    threads = []
    classifica = []
    for i in range(n):
        t = threading.Thread(target=prendiPunteggio, args=(i, classifica))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    classifica.sort()
    for i, (_, index) in enumerate(classifica):
        listaPunteggioPartecipanti[index] += 10 - i 

def secondaProva(k):
    def provaCasuale(index):
        print(f"Concorrente {listaPartecipanti[index]} attende di iniziare la seconda prova")
        time.sleep(random.randint(2, 4))
        print(f"Concorrente {listaPartecipanti[index]} inizia la seconda prova")
        tempoAspettato = random.randint(2, 4)
        time.sleep(tempoAspettato)
        punti = random.randint(1, 10)
        with lockPunteggio:
            listaPunteggioPartecipanti[index] += punti
        print(f"Concorrente {listaPartecipanti[index]} termina la seconda prova con punti {punti}")
    
    threads = []
    for i in range(k):
        t = threading.Thread(target=provaCasuale, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

def premiazione():
    for i in range(len(listaPartecipanti)):
        print(f"Concorrente {listaPartecipanti[i]} termina la gara con totale {listaPunteggioPartecipanti[i]} punti")

creaLista()
primaProva(7)
secondaProva(3)
premiazione()