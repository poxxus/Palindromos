def casasdecimais():
    numero = int(input())
    centena = numero // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10
    if centena > 0:
        print(f"{centena} centenas")
        if dezena > 0:
            print("")
            print("e")
            print("")
            print(f"{dezena} dezenas")
        if unidade > 0:
            print("")
            print("e")
            print("")
            print(f"{unidade} unidades")
    elif dezena > 0:
        print(f"{dezena} dezenas")
        if unidade > 0:
            print("")
            print("e")
            print("")
            print(f"{unidade} unidades")
    elif unidade > 0:
        print(f"{unidade} unidades")


casasdecimais()
