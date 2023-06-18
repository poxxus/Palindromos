def contagemaluca():
    inicio = int(input())
    regresso = 2
    while inicio > 0:
        print(f"Faltam {inicio} segundos")
        inicio -= regresso
        regresso += 2
    print("Acabou")


contagemaluca()
