def numerosamigos():
    num1 = int(input())
    num2 = int(input())
    acc1 = 0
    acc2 = 0
    contador = 1
    while contador < num1:
        if num1 % contador == 0:
            acc1 += contador
        contador +=1
    contador = 1
    while contador < num2:
        if num2 % contador == 0:
            acc2 += contador
        contador +=1
    if acc1 == num2 and acc2 == num1:
        print("amigos")
    else:
        print("nao amigos")


numerosamigos()