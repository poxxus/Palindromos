def risadas():
    risada = list(input())
    direita = list()
    esquerda = list()
    for i in range(0,len(risada)):
        if risada[i] in ["a", "e", "i", "o", "u"]:
            esquerda.append(risada[i])
    for i in range(len(risada)-1,-1,-1):
        if risada[i] in ["a", "e", "i", "o", "u"]:
            direita.append(risada[i])
    if esquerda == direita:
        print("S")
    else:
        print("N")

risadas()
