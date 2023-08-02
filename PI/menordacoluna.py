def menor_da_coluna():
    linhas = int(input())
    matriz = list()
    for w in range(0,linhas):
        entrada = input().split(" ")
        entrada = [int(x) for x in entrada]
        matriz.append(entrada)
    soma = 0
    for j in range(0, len(matriz[0])):
        menor = matriz[0][j]
        for i in range(0, len(matriz)):
            if menor > matriz[i][j]:
                menor = matriz[i][j]
        soma += menor
    return print(soma)


menor_da_coluna()
