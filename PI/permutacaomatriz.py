def permutacaomatriz():
    linhas = int(input())
    matriz = list()
    for w in range(0,linhas):
        entrada = input().split(" ")
        entrada = [int(x) for x in entrada]
        matriz.append(entrada)
    if linhas == 1:
        return print("NAO")
    for i in range(0, len(matriz)):
        acc = 0
        for j in range(0, len(matriz)):
            if matriz[i][j] not in [0,1]:
                return print("NAO")
            if matriz[i][j] == 1:
                acc += 1
        if acc != 1:
            return print("NAO")
    for j in range(0, len(matriz)):
        acc = 0
        for i in range(0, len(matriz)):
            if matriz [i][j] not in [0,1]:
                return print("NAO")
            if matriz[i][j] == 1:
                acc += 1
        if acc != 1:
            return print("NAO")
    print("SIM")


permutacaomatriz()
