# conceito
def conceito():
    nota = float(input())
    if 9 <= nota <= 10:
        return print(f"A")
    if 7.5 <= nota < 9:
        return print("B")
    if 6 <= nota < 7.5:
        return print("C")
    if 5 <= nota < 6:
        return print("D")
    if 0 <= nota < 5:
        return print("F")
    else:
        return print(f"Valor invalido! Digite um numero entre 0 e 10")


conceito()
