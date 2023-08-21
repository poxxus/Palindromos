def espiral(tamanho):
    matriz = list()
    for i in range(0, tamanho):
        linha = list()
        for j in range(0, tamanho):
            linha.append(0)
        matriz.append(linha)            
    acc = -1
    topo, fundo, esquerda, direita = 0, tamanho - 1, 0, tamanho - 1
    direcao = 0
    while topo <= fundo and esquerda <= direita:
        if direcao == 0:
            for i in range(esquerda, direita + 1):
                acc += 1
                matriz[topo][i] = acc
            topo += 1
        elif direcao == 1:
            for i in range(topo, fundo + 1):
                acc += 1
                matriz[i][direita] = acc
            direita -= 1
        elif direcao == 2:
            for i in range(direita, esquerda - 1, -1):
                acc += 1
                matriz[fundo][i] = acc
            fundo -= 1
        elif direcao == 3:
            for i in range(fundo, topo - 1, -1):
                acc += 1
                matriz[i][esquerda] = acc
            esquerda += 1

        direcao = (direcao + 1) % 4

    return matriz

def main():
    tamanho = int(input())
    resposta = espiral(tamanho)
    for i in range(0, tamanho):
        for j in range(0, tamanho):
            print(resposta[i][j], end= " ")
        print()


main()

