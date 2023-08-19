def percorrer(matriz, lista) -> bool:
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[0])):
            if matriz[i][j] in lista:
                elemento = matriz[i][j]
                lista.remove(elemento)
    if len(lista) == 0:
        return True                             
    return False


def main():
    acc = 0
    entrada = input().split(" ")
    linhas = int(entrada[0])
    colunas = int(entrada[1])
    matriz = list()
    for i in range(0, linhas):
        linha = input().split(" ")
        linha = [int(x) for x in linha]
        matriz.append(linha)
    lista = list()
    for j in range(0, linhas*colunas):
        numero = int(input())
        lista.append(numero)
    if percorrer(matriz,lista):
        return print("yes")
    else:
        return print("no")
    

main()