import time
import threading
import random

# Creazione di un lock per sincronizzare l'accesso ai punteggi
lockPunteggio = threading.Lock()

# Elenco dei nomi delle squadre
elencoSquadre = ["Team Alpha", "Team Beta", "Team Omega", "Team Phoenix", "Team Delta", "Team Sigma", "Team Rocket", "Team Nova"]

# Lista che tiene traccia del punteggio di ciascuna squadra
punteggioSquadra = [0 for i in range(len(elencoSquadre))]

# Funzione per la Prima Prova
def PrimaProva():
    def eseguiTest(i):
        """Simula l'esecuzione della prova per la squadra i"""
        print(f"{elencoSquadre[i]} inizia la prova")
        numCasuale = random.randint(1, 5)  # Tempo casuale per la prova
        time.sleep(numCasuale)  # Simulazione del tempo di attesa
        with lockPunteggio:  # Sincronizza l'accesso alla lista dei punteggi
            leaderboard.append((numCasuale, i))  # Aggiungi il risultato (tempo, indice della squadra) quest'ultimo l'ho passato come param
        print(f"{elencoSquadre[i]} ha finito la prova")

    # Lista per tracciare i thread e i risultati della prova
    threads = []
    leaderboard = []
    
    # Creazione e avvio dei thread per ogni squadra
    for i in range(len(elencoSquadre)):
        t = threading.Thread(target=eseguiTest, args=(i,))
        threads.append(t)
        t.start()

    # Attende il completamento di tutti i thread
    for t in threads:
        t.join()

    # Ordinamento dei risultati in base ai tempi (dal più basso al più alto)
    leaderboard.sort()

    # Assegna i punteggi alle squadre in base alla posizione nella classifica
    for i in range(len(leaderboard)):
        if i < 2:  # Le prime 2 squadre non ottengono punti
            punteggioSquadra[leaderboard[i][1]] += 0
        else:  # Le altre squadre ottengono un punteggio decrescente
            punteggioSquadra[leaderboard[i][1]] += 10 - i
        print(f"La squadra {elencoSquadre[leaderboard[i][1]]} ha ottenuto {punteggioSquadra[leaderboard[i][1]]} punti")


# Funzione per la Seconda Prova
def SecondaProva():
    def eseguiSecondoTest(index):
        """Simula l'esecuzione della seconda prova per la squadra index"""
        print(f"{elencoSquadre[index]} inizia la seconda prova")
        numCasuale = random.randint(1, 5)  # Tempo casuale per la prova
        time.sleep(numCasuale)  # Simulazione del tempo di attesa
        with lockPunteggio:  # Sincronizza l'accesso alla lista dei punteggi
            leaderboard.append((numCasuale, index))  # Aggiungi il risultato (tempo, indice della squadra)
        print(f"{elencoSquadre[index]} ha finito la seconda prova")

    # Selezioniamo 5 squadre in modo casuale per partecipare alla seconda prova
    listaPartecipanti2 = []
    tutti = 0
    while tutti != 5:
        rand = random.randint(0, len(elencoSquadre) - 1)  # Genera un indice casuale
        if rand not in listaPartecipanti2:  # Evita duplicati
            listaPartecipanti2.append(rand)
            tutti += 1
    print(listaPartecipanti2)  # Mostra quali squadre parteciperanno alla seconda prova

    # Lista per tracciare i thread e i risultati della prova
    leaderboard = []
    threads = []

    # Creazione e avvio dei thread per ogni partecipante
    for i in range(len(listaPartecipanti2)):
        t = threading.Thread(target=eseguiSecondoTest, args=(listaPartecipanti2[i],))
        threads.append(t)
        t.start()

    # Attende il completamento di tutti i thread
    for t in threads:
        t.join()

    # Ordinamento dei risultati in base ai tempi (dal più basso al più alto)
    leaderboard.sort()

    # Assegna i punteggi alle squadre in base alla posizione nella classifica
    for i in range(len(leaderboard)):
        if i < 2:  # Le prime 2 squadre non ottengono punti
            punteggioSquadra[leaderboard[i][1]] += 0
        else:  # Le altre squadre ottengono un punteggio decrescente
            punteggioSquadra[leaderboard[i][1]] += 10 - i
        # print(f"La squadra {elencoSquadre[leaderboard[i][1]]} ha ottenuto {punteggioSquadra[leaderboard[i][0]]} punti")

    # Ordina tutte le squadre in base ai punteggi in ordine decrescente
    listaCompleta = []
    for i in range(len(elencoSquadre)):
        listaCompleta.append((punteggioSquadra[i], elencoSquadre[i]))

    # Ordina in ordine decrescente per punteggio
    listaCompleta.sort(reverse=True)

    # Stampa i punteggi finali e i migliori 3
    print("\n")
    for i in range(len(listaCompleta)):
        print(f"La squadra {listaCompleta[i][1]} ha ottenuto {listaCompleta[i][0]} punti")
    print(f"I migliori 3 sono {listaCompleta[0][1]}, {listaCompleta[1][1]} e {listaCompleta[2][1]}")

# Esecuzione delle prove
PrimaProva()
SecondaProva()
