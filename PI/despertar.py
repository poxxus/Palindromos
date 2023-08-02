def despertar():
    entrada = input().split()
    l = int(entrada[0])
    matriz = list()
    for w in range(0,l):
        linha = list()
        for elemento in input().split(" "):
            linha.append(int(elemento))
        matriz.append(linha)
    n = len(matriz)
    m = len(matriz[0])
    achou = False
    for i in range(1,n-1):
        for j in range(1,m-1):
            if matriz[i][j] == 42 and matriz[i-1][j-1]==7 and matriz[i-1][j]==7 and matriz[i-1][j+1]==7 and matriz[i+1][j-1]==7 and matriz[i+1][j]==7 and matriz[i+1][j+1]==7 and matriz[i][j-1]==7 and matriz[i][j+1]==7:
                print (i+1, j+1)
                achou = True
    if not achou:
        print(0,0)

despertar()                                 