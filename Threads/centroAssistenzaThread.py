import random, threading, time

listaDaRiparare = ["Prodotto #" + str(x) for x in range(random.randint(5, 10))]
threadRiparare = []
threadNotifiche = []
print(listaDaRiparare)

semaforoTecnici = threading.Semaphore(3)
semaforoImpiegati = threading.Semaphore(2)


def diagnosi(prodotto):
    print("Tecnico aspetta a diagnosticare il prodotto:", prodotto)
    with semaforoTecnici:
        nome_tecnico=threading.current_thread().name
        time.sleep(random.randint(1, 3))
        print(f"Tecnico {nome_tecnico} ha iniziato a diagnosticare il prodotto:", prodotto)
        n = random.randint(1, 3)
        time.sleep(n)
        print("Tecnico ha finito di diagnosticare il prodotto, impiegati devono attendere", n, "minuti")
        t=threading.Thread(target=notifica,args=(prodotto,))
        threadNotifiche.append(t)
        t.start()


def notifica(prodotto):
    print("Impiegati sono in attesa della notifica di diagnostiche")
    with semaforoImpiegati:
        time.sleep(random.randint(1, 3))
        print("Impiegati hanno ricevuto la notifica di diagnostiche per il prodotto:", prodotto)

for i in range(len(listaDaRiparare)):
    t = threading.Thread(target=diagnosi, args=(str(listaDaRiparare[i]),),name=f"Thread-{i}")
    threadRiparare.append(t)
    t.start()

for t in threadRiparare:
    t.join()

for t in threadNotifiche:
    t.join()