def quantis():
    entrada = input().split(" ")
    entrada = [int(x) for x in entrada]
    q = int(input())
    numero = int(input())
    indice_anterior = 0
    acc = 0
    for i in range(0, q):
        indice = round(((len(entrada)+1)*i)/q)
        if numero in entrada[indice_anterior:indice]:
            return print(i)
            acc += 1
        indice_anterior = indice
    if acc == 0:
        print(q)


quantis()
