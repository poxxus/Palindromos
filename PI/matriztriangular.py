def matriztriangular():
    linhas = int(input())
    matriz = list()
    for i in range(0, linhas):
        linha = input().split(" ")
        linha = [float(x) for x in linha]
        matriz.append(linha)
    superior = 0
    inferior = 0
    for i in range(0, linhas):
        for j in range(0, linhas):
            if (i + j > i + i) and matriz[i][j] != 0:
                superior += 1
            if (i + j < i + i) and matriz[i][j] != 0:
                inferior += 1
    if superior>0 and inferior>0:
        return print("nao triangular")
    if superior == 0 and inferior > 0:
        return print("triangular inferior")
    if inferior == 0 and superior > 0:
        return print("triangular superior")
    if superior == 0 and inferior == 0:
        return print("diagonal")


matriztriangular()

