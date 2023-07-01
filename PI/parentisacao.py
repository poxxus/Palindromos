def parentisacao():
    equacao = input()
    parenteses = 0
    for caractere in equacao:
        if caractere == "(":
            parenteses += 1
        if caractere == ")":
            parenteses -= 1
        if parenteses < 0:
            break
    if parenteses == 0:
        print("Parentizacao correta")
    else:
        print("Erro na parentizacao")


parentisacao()
