def iguais():
    lista1 = input().split(" ")
    lista2 = input().split(" ")
    soma = 0
    for i in lista1:
        if i in lista2:
            print(i)
            soma += 1
    if soma == 0:
        print("NENHUM ELEMENTO EM COMUM")
    
            
iguais()

