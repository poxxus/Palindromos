def dobra_matriz():
    linhas = int(input())
    matriz = list()
    for w in range(0,linhas):
        entrada = input().split(" ")
        entrada = [int(x) for x in entrada]
        matriz.append(entrada)
    if len(matriz[0])%2 != 0:
        return print("numero impar de colunas")
    resposta = list()
    for i in range(0, linhas):
       linha = list()
       for j in range(0, len(matriz[0])//2):
            linha.append(0)
       resposta.append(linha)
    for a in range(0, len(matriz)):
        for b in range(0, len(matriz[0])//2):
            resposta[a][b] = matriz[a][b] + matriz[a][len(matriz[0])-b-1]
    for c in range(0, len(resposta)):
        for d in range(0, len(resposta[0])):
            print(f"{resposta[c][d]:.1f}", end=" ")
        print("")


dobra_matriz()
