import threading, random, time

lockPreparato = threading.Lock()
lockRider = threading.Lock()
semaforoRider = threading.Semaphore(2)  # massimo 2 rider che possono consegnare alla volta
semaforoCuochi = threading.Semaphore(3)  # massimo 3 cuochi per questa pizzeria

listaOrdini = ["Ordine #" + str(x) for x in range(1, random.randint(1, 11))]
listaPreparato = [0 for _ in range(len(listaOrdini))]  # 0 se non cucinato, 1 se preparato
listaConsegnato = [0 for _ in range(len(listaOrdini))]
print(listaOrdini, listaPreparato, listaConsegnato)

threadsRider = []  # Dichiaro la lista dei thread dei rider

def consegna(index):
    print(f"Rider è partito per la consegna #{index}")
    with semaforoRider:
        n = random.randint(4, 6)
        time.sleep(n)
        print(f"Rider ha finito la consegna #{index}")
        with lockRider:
            listaConsegnato[index] = 1

def cucina(index, chef):
    print(f"Ordine #{index} sta aspettando di preparare")
    with semaforoCuochi:
        print(f"Ordine #{index} messo a cucinare")
        n = random.randint(2, 6)
        time.sleep(n)
        print(f"Ordine #{index} ha finito di cucinare")
        with lockPreparato:
            listaPreparato[index] = 1

        riderThread = threading.Thread(target=consegna, args=(index,))
        threadsRider.append(riderThread)
        riderThread.start()

threads = []  # Dichiaro la lista dei thread dei cuochi

# Creo e avvio i thread per i cuochi
for i in range(len(listaOrdini)):  # Finché ci sono ordini da completare
    t = threading.Thread(target=cucina, args=(i, "Cuoco-" + str(i)))  # gli passo l'indice
    threads.append(t)
    t.start()

# Aspetto che tutti i thread dei cuochi finiscano
for t in threads:
    t.join()

# Aspetto che tutti i thread dei rider finiscano
for r in threadsRider:
    r.join()

print("Finito tutto")
