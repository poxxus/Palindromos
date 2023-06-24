def verificar():
    numero = int(input())
    divisores = 0
    for i in range(1, numero + 1):
        if (numero % i) == 0:
            divisores += 1
    if (divisores == 2):
        print("PRIMO")
    else:
        print("COMPOSTO")



verificar()
