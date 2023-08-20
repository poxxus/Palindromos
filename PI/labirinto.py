def labirinto():
    linhas = int(input())
    matriz = list()
    for i in range(0, linhas):
        linha = list(input())
        matriz.append(linha)
    i, j = 0, 0
    print("0 0")
    anterior = (i, j)
    for w in range(linhas*linhas):
        if (i-1 >= 0) and (matriz[i-1][j] == ".") and ((i-1, j) != anterior):
            print(f"{i-1} {j}")
            anterior = (i, j)
            i, j = i-1, j
        elif (i+1 <= linhas-1) and (matriz[i+1][j] == ".") and ((i+1, j) != anterior):
            print(f"{i+1} {j}")
            anterior = (i,j)
            i, j = i+1, j
        elif (j-1 >= 0) and (matriz[i][j-1] == ".") and ((i, j-1) != anterior):
            print(f"{i} {j-1}")
            anterior = (i, j)
            i, j = i, j-1
        elif (j+1 <= linhas-1) and (matriz[i][j+1] == ".") and ((i,j+1) != anterior):
            print(f"{i} {j+1}")
            anterior = (i, j)
            i, j = i, j+1


labirinto()