def UnioneListeOrdinate(a, b):
    if len(a) < len(b):
        corta, lunga = a, b
    else:
        corta, lunga = b, a

    i = 0
    c = []

    while i < len(corta):
        if corta[i] < lunga[i]:  
            c.append(corta[i])
            c.append(lunga[i])
        else:
            c.append(lunga[i])
            c.append(corta[i])
        i += 1 

    while i < len(lunga):
        c.append(lunga[i])
        i += 1

    return c

# Esempio di utilizzo
a = [2, 3, 5, 6, 7, 9]
b = [1, 4, 5, 8, 10, 15, 22]
unione = UnioneListeOrdinate(a, b)
print("Lista unita ordinata:", unione)