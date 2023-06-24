def edivisivel():
    anterior = 99999999
    numero = int(input())
    while (numero % anterior) != 0:
        print(numero)
        anterior = numero
        numero = int(input())
    print("PUM!")


edivisivel()
        