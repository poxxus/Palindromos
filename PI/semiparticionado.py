def semiparticionado():
    lista = []
    elementos = int(input())
    for i in range(0, elementos):
        lista.append(int(input()))
    for j in range(0, len(lista)//2):
        if lista[j] > lista[-j-1]:
            lista[j], lista[-j-1] = lista[-j-1], lista[j]
    print(lista)

    
semiparticionado()
