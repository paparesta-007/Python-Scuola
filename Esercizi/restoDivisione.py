a=4
b=3

def restoDivisione(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(restoDivisione(a,b))
    