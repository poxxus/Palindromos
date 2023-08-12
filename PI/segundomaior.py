def segundomaior():
    linhas = int(input())
    matriz = list()
    for i in range(0, linhas):
        linha = input().split(" ")
        linha = [int(x) for x in linha]
        matriz.append(linha)
    maior = matriz[0][0]
    for i in range(0, linhas):
        for j in range(len(matriz[0])):
            if maior < matriz[i][j]:
                maior = matriz[i][j]
    segundomaior = -99999
    for i in range(0, linhas):
        for j in range(len(matriz[0])):
            if segundomaior < matriz[i][j] and matriz[i][j] != maior:
                segundomaior = matriz[i][j]
    if segundomaior == -99999:
        return print("NOT FOUND")
    else:
        return print(segundomaior)

segundomaior()
