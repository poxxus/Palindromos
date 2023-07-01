def delvogal():
    entrada = input()
    saida = ""
    for letra in entrada:
        if letra != "A" and letra != "a" and letra != "E" and letra != "e" and letra != "I" and letra != "i" and letra != "U" and letra != "u" and letra != "O" and letra != "o":
            saida += letra
    print(saida)


delvogal()
