def trigo():
    trigo = 0
    potes = int(input())
    for i in range(0, potes):
        trigo = trigo + 2**i
    trigo = (trigo / 12) / 1000
    print(f"{trigo:.2f} kg")


trigo()
