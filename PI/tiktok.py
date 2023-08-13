def percorrer_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            num = matriz[i][j]
            if not verificar_distancia(matriz, i, j, num):
                return False
    return True


def verificar_distancia(matriz, i, j, num) -> bool:
    for a in range(len(matriz)):
        for b in range(len(matriz[a])):
            if matriz[a][b] == num:
                distancia = abs(i - a) + abs(j - b)
                if (distancia <= num and distancia != 0) or num > 8:
                    return False
    return True


def main():
    matriz = list()
    for i in range(0, 6):
        linha = input().split(" ")
        linha = [int(x) for x in linha]
        matriz.append(linha)
    
    if percorrer_matriz(matriz):
        print("Válido")
    else:
        print("Inválido")


main()

