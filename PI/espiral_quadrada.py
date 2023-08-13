def verificar(numero: int) -> bool:
    divisores = 0
    if numero == 0 or numero == 1:
        return False
    for i in range(1, numero + 1):
        if (numero % i) == 0:
            divisores += 1
    if (divisores == 2):
        return True
    else:
        return False


def espiral_quadrada():
    entrada = input().split(" ")
    linhas = int(input())
    matriz = list()
    for i in range(0, linhas):
        lista = input().split(" ")
        lista = [int(x) for x in lista]
        matriz.append(lista)
    resposta = list()
    for w in range(0, linhas):
        linha_resposta = list()
        for e in range(0, 2*linhas):
            linha_resposta.append(0)
        resposta.append(linha_resposta)
    for i in range(0, linhas):
        for j in range(0, linhas):
            if "primos" in entrada:
                if verificar(matriz[i][j]):
                    resposta[i][2*j], resposta[i][2*j+1] = chr(9617), chr(9617)
            else:
                x = int(entrada[len(entrada)-1])
                if matriz[i][j] % x == 0:
                    resposta[i][2*j], resposta[i][2*j+1] = chr(9617), chr(9617)
    for a in range(0, linhas):
        for b in range(0, 2*linhas):
            if resposta[a][b] == 0:
                resposta[a][b] = chr(9608)
            print(resposta[a][b], end="")
        print()


espiral_quadrada()