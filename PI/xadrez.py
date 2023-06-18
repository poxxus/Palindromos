def xadrez():
    tamanho = int(input())
    universal = 1
    contador = 1
    acc = ""
    while universal <= tamanho:
        if universal % 2 != 0:
            while contador <= tamanho:
                if (contador % 2) != 0:
                    acc = acc + "o"
                else:
                    acc = acc + "*"
                contador += 1
            print(acc)
        elif (universal % 2) == 0:
            while contador <= tamanho:
                if (contador % 2) != 0:
                    acc = acc + "*"
                else:
                    acc = acc + "o"
                contador += 1
            print(acc)
        universal += 1
        contador = 1
        acc = ""


xadrez()