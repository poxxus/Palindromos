def cores():
    r = bool(int(input()))      # vermelho
    g = bool(int(input()))      # verde
    b = bool(int(input()))      # azul
    if b:
        if r:
            if g:
                print("7")      # branco
            else:
                print("2")      # roxo
        elif g:
            print("6")      # ciano
        else:
            print("1")      # azul
    elif r:
        if g:
            print("4")      # amarelo
        else:
            print("3")      #vermelho
    elif g:
        print("5")      # verde
    else:
        print("8")      # preto


cores()

