def torre():
    linhas = int(input())
    matriz = list()
    for w in range(0,linhas):
        entrada = input().split(" ")
        entrada = [int(x) for x in entrada]
        matriz.append(entrada)
    soma = list(int())
    aux = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            for z in range(0,len(matriz)):
                aux += matriz[z][j]
            soma.append(sum(matriz[i])+aux-2*matriz[i][j])
            aux = 0
    return print(max(soma))


torre()