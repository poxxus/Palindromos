def maior3():
    a = int(input())
    b = int(input())
    c = int(input())
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return print(f"O maior inteiro: {maior}")


maior3()
