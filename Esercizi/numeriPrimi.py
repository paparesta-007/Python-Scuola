import math
lista=[x for x in range(1,101)]
# print(lista)

def listaNumeriPrimi(list):
    for i in range (2,11):
        for j in list:
            if j%i==0 and j!=i: # Per controllare se è un multiplo si vede se il resto è 0
                list.remove(j)
    print(list)

    
listaNumeriPrimi(lista)

def trova_primi_fino_a(N):
    lista2 = list(range(2, N + 1))
    for i in range(2, int(math.sqrt(N)) + 1):
        lista2 = [x for x in lista2 if (x == i or x % i != 0)]
    print(lista2)

# print(lista)
# s=int(input("Inserisci un numero: "))
# trova_primi_fino_a(s)