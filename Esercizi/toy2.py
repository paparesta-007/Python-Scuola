def rimuoviDuplicati(lista):
    lista2=[]
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    return lista2

def contaVocali(testo):
    count=0
    for i in testo:
        if i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count+=1
    return count

def filtroMultipli(lista,n):
    lista2=[]
    for i in lista:
        if i%n==0:
            lista2.append(i)
    return lista2

def valoriUniciPari(lista):
    lista2=[]
    for i in lista:
        if i%2==0:
            if i not in lista2:
                lista2.append(i)
    return lista2
    
def mergeList(lista1,lista2):
    lista3=[]
    if len(lista1) < len(lista2):
        corta, lunga = lista1, lista2
    else:
        corta, lunga = lista2, lista1

    j=0
    print("la lista corta è")
    for i in range(len(corta)):
        lista3.append(corta[i])
        lista3.append(lunga[i])
        j=j+1
        
    for i in range(j,len(lunga)):
        lista3.append(lunga[i])
    return lista3


def frequenze(lista):
    lista2 = []
    lista3 = []

    for i in lista:
        if i not in lista2:
            lista2.append(i)

    print(lista2)

    for i in range(len(lista2)):
        lista3.append(lista.count(lista2[i]))

    print(lista3)

    max1 = 0
    max2 = 0
    max3 = 0

    for i in lista3:
        if i > max1:
            max3 = max2
            max2 = max1
            max1 = i
        elif i > max2 and i != max1:
            max3 = max2
            max2 = i
        elif i > max3 and i != max1 and i != max2:
            max3 = i

    print(max1, max2, max3)


print(rimuoviDuplicati([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]))
print("Ci sono:",contaVocali("Ciao come stai?"),"vocali")
print(filtroMultipli([3, 6, 8, 9, 12, 15, 17, 20],2))
print(valoriUniciPari([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]))
print(mergeList([1,2,3],['a','b','c','d']))
print(frequenze("aaaaaaabbbbccdeee"))
lista=[1,2,3,4,5,6,7,8]
print(lista[2:5])

listaProva=[1,11,3,4,4,6,7,8,9,9,]
lista3=[x for x in listaProva if x>3]
print(lista3)