import threading
import time
import random

lockPunteggio=threading.Lock()
lock=threading.Lock()

# thread1=threading.Thread(target=iniziaProva,args=("Thread 1",))
# thread2=threading.Thread(target=iniziaProva,args=("Thread 2",))

def inizio():
    def iniziaProva(index):
        print(f"Thread {index} Processo iniziato")
        r=random.randint(1,5)
        time.sleep(r)
        with lockPunteggio:
            classifica.append((r,index)) # crea una tupla
        print(f"C{index} - Processo finito in ",r," secondi")
    
    listaThread=["C"+str(x) for x in range(11)]
    print(listaThread)

    classifica=[]
    threads=[]
    listaPunteggioPartecipanti=[0 for _ in range(11)]
    for i in range(len(listaThread)):
        t=threading.Thread(target=iniziaProva,args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print(classifica)
    classifica.sort(reverse=True)

  
    print(classifica)
    
    print("*** Classifica ***")  
    for i in range(len(classifica)):
        index=classifica[i][1]
        listaPunteggioPartecipanti[index]+=10-i
        print(f"Il concorrente {listaThread[index]} ha ottenuto {listaPunteggioPartecipanti[index]} punti")
    # print()
    
    

inizio()
# thread1.start()
# thread2.start()
# thread2.join()
# thread1.join()
