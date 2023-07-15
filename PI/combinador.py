def combinador():
    frase = input().split(" ")
    linha = frase[0]
    linha2 = frase[1]
    linha = [x for x in linha]
    linha2 = [y for y in linha2]
    saida = ""
    acc = 1
    while linha != [] and linha2 != []:
        if acc%2 != 0:
            saida += linha.pop(0)
        else:
            saida += linha2.pop(0)
        acc += 1
    if len(linha) != 0:
        for i in range(0, len(linha)):
            saida += linha.pop(0)
    if len(linha2) != 0:
        for j in range(0, len(linha2)):
            saida += linha2.pop(0)
    print(saida)


combinador()

