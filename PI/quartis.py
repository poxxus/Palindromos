def quartis():
    numeros = int(input())
    desejado = int(input())
    for i in range(0, numeros):
        numero = int(input())
    if 0 <= desejado <= round(numero / 4):
        print("1")
    elif round(numero / 4) < desejado <= round(numero * 0.5):
        print("2")
    elif round(numero * 0.5) < desejado <= round(numero * 0.75):
        print("3")
    else:
        print("4")
    

quartis()

