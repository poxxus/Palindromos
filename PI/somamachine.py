def somamachine():
    qtidade = int(input())
    acc = 0
    contador = 1
    while contador <= qtidade:
        numero = float(input())
        acc += numero
        contador += 1
    print(f"Total: {acc:.2f}")


somamachine()
