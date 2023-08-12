def manhattan_matriz():
    linhas = int(input())
    matriz = list()
    for i in range(0,linhas):
        linha = list()
        for j in range(0, linhas):
            linha.append(0)
        matriz.append(linha)
    indices = input().split(" ")
    linha_i = int(indices[0])
    coluna_j = int(indices[1])
    for a in range(0, linhas):
        for b in range(0, linhas):
            if a == linha_i and b == coluna_j:
                print(matriz[a][b], end=" ")
            else:
                matriz[a][b] = abs(linha_i-a) + abs(coluna_j-b)
                print(matriz[a][b], end = " ")
            
        print()
    

manhattan_matriz()
