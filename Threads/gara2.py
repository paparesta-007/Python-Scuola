import time, random, threading
from operator import indexOf

listaConcorrentiTotali = ["C" + str(x) for x in range(1, 11)]
listaPunteggio = [0 for _ in range(1, 11)]
lockPunteggio=threading.Lock()
threadsPrimaProva=[]
threadsSecondaProva=[]
threadsPremiazione=[]
def prendiConcorrenti(numConcorrenti):
    lista = []
    while len(lista) != numConcorrenti:
        n = random.randint(1, 10)
        s = "C" + str(n)
        if s not in lista:
            lista.append(s)
    return lista


def prendiPunteggio(index,minSleep,maxSleep):
    concorrente = listaConcorrentiTotali[index]
    print(f"Concorrente {concorrente} attende la prova")
    p=random.randint(minSleep, maxSleep)
    time.sleep(p)
    print(f"Concorrente {concorrente} ha iniziato la prova")
    time.sleep(p)
    with lockPunteggio:
        print(f"Concorrente {concorrente} ha finito la prova con un punteggio di N-{p}")
        listaPunteggio[index] =listaPunteggio[index]+ p



def primaProva():
    listaConcorrenti = prendiConcorrenti(7)

    for i in listaConcorrenti:
        # Trovo l'indice del concorrente nella lista
        index = listaConcorrentiTotali.index(i)
        t=threading.Thread(target=prendiPunteggio,args=(index,1,3))
        threadsPrimaProva.append(t)
        t.start()

    for t in threadsPrimaProva:
        t.join()
    print("*** Prima prova finita con successo ***")

def SecondaProva():
    listaSecondaProva=prendiConcorrenti(3)

    for i in listaSecondaProva:
        index=listaConcorrentiTotali.index(i)
        t=threading.Thread(target=prendiPunteggio,args=(index,2,4))
        threadsSecondaProva.append(t)
        t.start()

    for t in threadsSecondaProva:
        t.join()
    print("*** Seconda prova finita con successo ***")


def visualizzaPunteggio(index):
    print(f"Il concorrente {listaConcorrentiTotali[index]} ha totalizzato {listaPunteggio[index]} punti!")
    time.sleep(1)

def Premiazione():
    for i in range(len(listaConcorrentiTotali)):

        t=threading.Thread(target=visualizzaPunteggio,args=(i,))
        threadsPremiazione.append(t)
        t.start()

    for t in threadsPremiazione:
        t.join()

primaProva()
SecondaProva()
Premiazione()