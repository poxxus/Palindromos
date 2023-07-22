def iccanobif():
    a, fibbonacci = 1, 1
    numero = int(input())
    acc = 2
    lista = [1, 1]
    while numero > acc:
        a, fibbonacci = fibbonacci, a + fibbonacci
        lista.append(fibbonacci)
        acc += 1
    for i in range(len(lista)-1, -1, -1):
        print(lista[i], end= " ")


iccanobif()
