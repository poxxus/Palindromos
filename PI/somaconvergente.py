def somaconvergente():
    lista = input().split(" ")
    lista = list(map(int, lista))
    acc = 0
    if len(lista) == 2:
        return print("SIM")
    for i in range(0, (len(lista)//2)-1):
        if lista[i] + lista[-i-1] > lista[i+1] + lista[-(i+1)-1]:
                acc += 1
    if acc == (len(lista)/2)-1:
        print("SIM")
    else:
        print("NAO")

somaconvergente()
