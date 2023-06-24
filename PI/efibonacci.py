def efibonacci():
    numero = int(input())  
    a, fibonacci = 0, 1
    if numero == 0 or numero == 1:
        return print("Verdadeiro")
    while numero >= fibonacci:
            a, fibonacci = fibonacci, a + fibonacci
            if numero == fibonacci:
                 return print("Verdadeiro")
    return print("Falso")              


efibonacci()
