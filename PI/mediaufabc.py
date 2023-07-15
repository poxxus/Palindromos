def mediaufabc():
    lista = input().split(" ")
    lista_inteiros = list(map(float, lista))
    lista_inteiros.remove(min(lista_inteiros))
    lista_inteiros.remove(max(lista_inteiros))
    media = sum(lista_inteiros) / len(lista_inteiros)
    print(f"MEDIA FINAL: {media:.4f}")


mediaufabc()