def maior3():
    a = int(input())
    b = int(input())
    c = int(input())
    maior = a
    if b > maior:
        b = maior
    if c > maior:
        c = maior
    return print(f"O maior inteiro: {maior}")


maior3()
