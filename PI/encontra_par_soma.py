def encontrar_par():
    lista = input().split(" ")
    soma = int(input())
    acc = 0
    for i in range(0, len(lista)):
        for j in range(i + 1, len(lista)):
            if (int(lista[i]) + int(lista[j])) == soma:
                print(f"X[{i}] + X[{j}] = {soma}")
                acc += 1
    if acc == 0:
        print(f"NENHUM PAR SOMA {soma}")


encontrar_par()
