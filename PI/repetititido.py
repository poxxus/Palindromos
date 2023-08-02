def repetido():
    lista = input().split(" ")
    for i in range(0, len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                return print("S")
    print("N")


repetido()  
