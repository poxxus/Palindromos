def matriz_simetrica():
    linhas = int(input())
    matriz = list()
    for i in range(0, linhas):
        linha = input().split(" ")
        linha = [float(x) for x in linha]
        matriz.append(linha)
    simetrica = True
    for i in range(0, linhas):
        for j in range(0, linhas):
            if matriz[i][j] != matriz[j][i]:
                simetrica = False
    if simetrica:
        return print("S")
    print("N")


matriz_simetrica()
