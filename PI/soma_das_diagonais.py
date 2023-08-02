def menor_da_coluna():
    linhas = int(input())
    matriz = list()
    for w in range(0,linhas):
        entrada = input().split(" ")
        entrada = [int(x) for x in entrada]
        matriz.append(entrada)
    num_linhas = len(matriz)
    soma = 0
    for i in range(0,num_linhas):
        soma += matriz[i][i]
    for j in range(0,num_linhas):
        soma += matriz[j][num_linhas-1-j]
    soma = soma - matriz[num_linhas//2][num_linhas//2]
    return print(f"X = {soma}")


menor_da_coluna()
