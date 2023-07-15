def encontrar_elementos_repetidos(lista):   
    elementos_repetidos = {}

    for i, elemento in enumerate(lista):
        if elemento in elementos_repetidos:
            elementos_repetidos[elemento][1] = i
        else:
            elementos_repetidos[elemento] = [i, None]

    elementos_repetidos = {k: v for k, v in elementos_repetidos.items() if v[1] is not None}

    return elementos_repetidos

digitos = int(input())
lista = []
for i in range(0, digitos):
    lista.append(int(input()))

elementos_repetidos = encontrar_elementos_repetidos(lista)

for elemento, posicoes in elementos_repetidos.items():
    posicao_inicial, posicao_repetida = posicoes
    print(f"Elemento repetido: {elemento} - Posições: {posicao_inicial}, {posicao_repetida}")
if len(elementos_repetidos) == 0:
    print("NAO HA NUMEROS REPETIDOS")        

        