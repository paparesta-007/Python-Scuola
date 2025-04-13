lista1=[1,4,6,7,10]
lista2=[2,4,5,9,10]

def intersezioneTraListe(lista1, lista2):
    lista3=[]
    for i in lista1:
        if i in lista2:
            lista3.append(i)
    return lista3

print(intersezioneTraListe(lista1,lista2))