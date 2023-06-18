def tabuada():
    numero = int(input())
    vezes = int(input())
    contador = 0
    acc = 1
    while contador <= vezes:
        acc = numero * contador
        print(f"{numero} x {contador} = {acc}")
        contador += 1


tabuada()
