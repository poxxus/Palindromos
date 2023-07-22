def estrelas():
    area = int(input())
    estrelas = int(input())
    visiveis = 0
    for i in range(0, estrelas):
        luz = int(input())
        if luz*area >= 40000000:
            visiveis += 1
    return print(visiveis)


estrelas()
