def cade_wally():
    entrada = input().split(" ")
    linhas = int(entrada[0])
    matriz = list()
    for i in range(0, linhas):
        lista = input().split(" ")
        lista = [int(x) for x in lista]
        matriz.append(lista)
    zeros = 0
    quatro = 0
    oito = 0
    for j in range(0, linhas):
        for k in range(0, len(matriz[0])):
            if matriz[j][k] == 1111:
                for w in range(j-1, j+2):
                    for z in range(k-1, k+2):
                        if w < 0:
                            w = linhas - 1
                        if w > linhas - 1:
                            w = 0
                        if z < 0:
                            z = len(matriz[0])-1
                        if z > len(matriz[0])-1:
                            z = 0
                        if matriz[w][z] == 0:
                            zeros += 1
                        if matriz[w][z] == 4:
                            quatro += 1
                        if matriz[w][z] == 8:
                            oito += 1
            if zeros >= 2 and quatro >= 1 and oito >= 1:
                return print(f"{j} {k}")
    print("WALLY NAO ESTA!")

cade_wally()                     
