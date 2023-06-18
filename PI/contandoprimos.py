def contandoprimos():
    qtidade = int(input())
    contador = 1
    contador2 = 1
    acc = 0
    list = []
    while contador <= qtidade:
        num = int(input())
        while contador2 <= num:
            if (num % contador2) == 0:
                list.append(contador2)
                contador2 += 1
            else:
                contador2 += 1
        if len(list) == 2:
            acc += 1
        list = []
        contador += 1
        contador2 = 1
    print(f"dos {qtidade} numeros informados {acc} eram primos")


contandoprimos()
