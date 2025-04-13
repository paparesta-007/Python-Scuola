lista = [1, 2, 3, 4, 5]
n = 2

def listaCiclica(lista, n):
    return lista[n:] + lista[:n]
    #  [n:] ritorna lista dalla posizione n in poi
    #  [:n] ritorna lista dalla posizione 0 alla n-1

print(listaCiclica(lista, n))  # [3, 4, 5, 1, 2]