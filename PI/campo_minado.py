def campo_minado():
    entrada = input().split(" ")
    linhas = int(entrada[0])
    matriz = list()
    for i in range(0, linhas):
        lista = input()
        lista = list(lista)
        matriz.append(lista)
    resposta = list()
    for i in range(0, linhas):
       linha = list()
       for j in range(0, len(matriz[0])):
            linha.append(0)
       resposta.append(linha)
    for a in range(0, len(matriz)):
        for b in range(0, len(matriz[0])):
            if matriz[a][b] == "*":
                resposta[a][b] = "*"
            else:
                soma = 0
                for w in range(a-1,a+2):
                    for z in range(b-1,b+2):
                        if 0 <= w < len(matriz) and 0 <= z < len(matriz[0]) and matriz[w][z]:
                            soma += 1
                resposta[a][b] = soma
    for c in range(0, len(resposta)):
        for d in range(0, len(resposta[0])):
            print(f"{resposta[c][d]}", end="")
        print("")
    

campo_minado()
