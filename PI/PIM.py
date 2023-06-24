def pim():
    vezes = int(input())
    soma = 0
    for i in range(0, vezes):
        for i in range(0, 3):
            soma += 1
            print(soma, end=" ")
        print("PIM", end= " ")
        soma += 1
        print("")


pim()
        