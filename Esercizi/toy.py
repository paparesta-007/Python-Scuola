# calcoli la differenza tra due liste ricevute come parametro (la funzione dovrebbe rimuovere
# dalla prima lista tutti gli elementi della seconda lista) e la restituisca senza modificare l'ordine degli elementi.
# Esempio: dati a = [1, 2, 2, 2, 3] e b = [2], il risultato sia [1, 3]
def toy1(lista1,lista2):
    lista3=lista1.copy()
    for i in lista2: # scorro la lista2 e per ogni elemento di lista2 lo tolgo da lista1
        while i in lista3: # finchè l'elemento è presente in lista3 lo tolgo, 
            lista3.remove(i)
    return lista3


a = [1, 2, 2, 2, 3,6,6,6,8,10]
b = [2,6]


# dato un numero positivo restituisca un altro intero, con le cifre riordinate in ordine decrescente.
# Esempio: Input: 42145 Output: 54421
def toy2(numero):
    lista=[]
    while numero > 0:
        lista.append(numero % 10)
        numero = numero // 10
    lista.sort(reverse=True)
    s=""
    for i in range(len(lista)):
        s += str(lista[i])
    return int(s)
    
# dati due interi a e b, calcoli la somma di tutti gli interi compresi tra i numeri
# dati (estremi inclusi) e la restituisca. se i numeri sono uguali, restituisca quel numero. I numeri possono essere negativi e non ordinati
# Esempio: 5,-1 fa 14 
def toy3(a,b):
    if a==b:
        return "numeri uguali"
    else:
        somma=0
        if a>b:
            a,b=b,a 
        for i in range(a,b+1):
            somma+=i
        return somma


# Data una lista, ordinare al suo inerno solo i numeri pari. i campi della lista che hanno un valore dispari devono rimanere al loro posto.
# esempio: [9, 8, 7, 6, 5 ,4 , 4, 3, 1] diventa [9, 4, 7, 4, 5 ,6 , 8, 3, 1]
def toy4():
    lista=[9, 8, 7, 6, 5 ,4 , 4, 3, 1]
    listaAus=[]
    j=0
    for i in lista:
        if i%2==0:
            listaAus.append(i)
    listaAus.sort()
    print(listaAus)
    for k in range(len(lista)):
        if lista[k]%2==0:
            lista[k]=listaAus[j]
            j+=1
    return lista
def CodificaCesare(testo):
    aus=[]
    for i in testo:
        aus.append(i)

    cifrato=""
    for i in range(len(aus)):
        char_code = ord(aus[i])

        if char_code >= 65 and char_code <= 90:
            if char_code > 77: # ASCII 77 is 'M'. Checks if it's N-Z
                # Subtract 13 to wrap around (e.g., N -> A)
                cifrato += chr(char_code - 13)
            else: # It's A-M
                # Add 13 (e.g., A -> N)
                cifrato += chr(char_code + 13)

        # 5. Check if it's a lowercase letter (ASCII 97='a' to 122='z')
        elif char_code >= 97 and char_code <= 122:
             # Apply ROT13 shift for lowercase
            if char_code > 109: # ASCII 109 is 'm'. Checks if it's n-z
                # Subtract 13 to wrap around (e.g., n -> a)
                cifrato += chr(char_code - 13)
            else: # It's a-m
                # Add 13 (e.g., a -> n)
                cifrato += chr(char_code + 13)

        # 6. Handle non-alphabetic characters
        else:
            # Append the character unchanged (numbers, spaces, symbols)
            cifrato += aus[i]

    # 7. Return the resulting encrypted string
    return cifrato

# def CodificaCesare(testo):
#     cifrato = ""
#     for c in testo:
#         if 'A' <= c <= 'Z':
#             # Calcolo la posizione da 0 a 25
#             pos = ord(c) - ord('A')
#             nuova_pos = (pos + 13) % 26  # spostamento di 13, modulo 26
#             nuovo_char = chr(ord('A') + nuova_pos)
#             cifrato += nuovo_char
#         elif 'a' <= c <= 'z':
#             pos = ord(c) - ord('a')
#             nuova_pos = (pos + 13) % 26
#             nuovo_char = chr(ord('a') + nuova_pos)
#             cifrato += nuovo_char
#         else:
#             cifrato += c  # lascio intatti gli altri caratteri (spazi, punteggiatura, numeri)
#     return cifrato


print(toy1(a,b))
print(toy2(42145))
print(toy3(5,11))
print(toy4())
print(CodificaCesare("aA bB zZ 1234"))

