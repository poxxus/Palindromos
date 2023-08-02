def cavalo():
    entrada = input().split(" ")
    p1 = int(entrada[0])
    p2 = int(entrada[1])
    posicoes = list()
    posicoes.append([p1-2,p2-1])
    posicoes.append([p1-2,p2+1])
    posicoes.append([p1-1,p2-2])
    posicoes.append([p1-1,p2+2])
    posicoes.append([p1+1,p2-2])
    posicoes.append([p1+1,p2+2])
    posicoes.append([p1+2,p2-1])
    posicoes.append([p1+2,p2+1])
    for elemento in posicoes:
        if elemento[0] in range(0,8) and elemento [1] in range(0,8):
            print(elemento[0], elemento[1])


cavalo()
