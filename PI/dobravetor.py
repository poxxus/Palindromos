def dobravetor():
    lista = []
    numero = int(input())
    while (numero % 2) != 0:
        numero = int(input())
    for i in range(0, numero):
        entrada = int(input())
        lista.append(entrada)
    final = []
    for j in range(0, len(lista)//2):
        final.append(lista[j]+lista[-j-1])
    print(final)


dobravetor()

