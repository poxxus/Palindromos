def divisorpar():
    numero = int(input())
    acc = 0
    contador = 1
    while contador <= numero:
        if (numero % contador) == 0 and contador % 2 == 0:
            acc += 1 
        contador += 1
    print(f"{acc}")


divisorpar()

