def compras():
    espera = float(input())
    juros = float(input())
    total = float(input())
    if espera + (juros/100)*espera >= total:
        return print("compro")
    else:
        return print("passo")


compras()