def bordas():
    linhas = int(input())
    colunas = int(input())
    l = 1
    while l <= linhas:
        c = 1
        while c <= colunas:
            if l == 1 or c==1 or l == linhas or c == colunas:
                print("*", end= "")
            else:
                print(" ", end= "")
            c += 1
        print()
        l += 1


bordas()