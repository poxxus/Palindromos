def caca_palavras():
    p1 = list(input())
    p2 = list(input())
    p1_reversa = list()
    p2_reversa = list()
    for i in range(len(p1)-1,-1,-1):
        p1_reversa.append(p1[i])
    for i in range(len(p2)-1,-1,-1):
        p2_reversa.append(p2[i])
    matriz = list()
    for i in range(0,16):
        lista = input().split(" ")
        matriz.append(lista)
    acc = 0
    for j in range(0,16):
        for k in range(0, len(matriz[0])-len(p1)+1):
            aux = list()
            for l in range(k,k+len(p1)):
                aux.append(matriz[j][l])
            if aux == p1 or aux == p1_reversa:
                acc += 1
        for k in range(0, len(matriz[0])-len(p2)+1):
            aux = list()
            for l in range(k,k+len(p2)):
                aux.append(matriz[j][l])
            if aux == p2 or aux == p2_reversa:
                acc += 1                           
    if acc >= 2:
        print("SIM")
    else:
        print("NAO")

caca_palavras()
