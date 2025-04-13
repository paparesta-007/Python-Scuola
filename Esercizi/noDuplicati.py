lst = [1, 2, 3, 2, 4, 3, 5, 1, 6]

def noDuplicati(lst):
    """
    Funzione che restituisce una lista senza duplicati.
    :param lst: lista di numeri
    :return: lista senza duplicati
    """
    # return list(set(lst))
    lista2 = []
    for i in lst:
        if i not in lista2: # not controlla se l'elemento è già presente nella lista
            # se non è presente lo aggiunge alla lista
            lista2.append(i)
    return lista2

print(noDuplicati(lst))  # [1, 2, 3, 4, 5, 6]