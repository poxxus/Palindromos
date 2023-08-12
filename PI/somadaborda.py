def somadaborda():
    entrada = input().split(" ")
    linhas = int(entrada[0])
    matriz = list()
    for i in range(0, linhas):
        linha = input().split(" ")
        linha = [float(x) for x in linha]
        matriz.append(linha)
    colunas = len(matriz[0])
    resposta = 0
    for i in range(0, linhas):
        for j in range(0, colunas):
            if i in [0, linhas-1] or j in [0, colunas - 1]:
                resposta += matriz[i][j]
    return print(f"Borda = {resposta:.2f}")

somadaborda()
