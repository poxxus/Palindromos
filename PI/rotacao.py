def rotacaodireita():
    lista = input().split(" ")
    print("Lista :", end=" ")
    for i in range(0, len(lista)):
        print(lista[i], end= " ")
    print("")
    if len(lista) - 1 == 0:
        return print("NENHUMA ROTACAO POSSIVEL")
    for j in range(0, len(lista)-1):
        rotor = lista[0]
        lista.remove(lista[0])
        lista.append(rotor)
        print(f"Rotacao {j+1}:", end="")
        for i in range(0, len(lista)):
            print(lista[i], end= " ")
        print("")


def rotacaoesquerda():
    lista = input().split(" ")
    print("Lista :", end=" ")
    for i in range(0, len(lista)):
        print(lista[i], end= " ")
    print("")
    if len(lista) - 1 == 0:
        return print("NENHUMA ROTACAO POSSIVEL")
    for j in range(0, len(lista)-1):
        rotor = lista[len(lista)-1]
        del lista[-1]
        lista.insert(0, rotor)
        print(f"Rotacao {j+1}:", end="")
        for i in range(0, len(lista)):
            print(lista[i], end= " ")
        print("")

rotacao = input()
if rotacao == "E":
    rotacaoesquerda()
else:
    rotacaodireita()



