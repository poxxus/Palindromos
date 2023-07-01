def senhara():
    entrada = str(input())
    senha = ""
    token = 1
    if entrada[0] == "R" and entrada[1] == "A" and entrada[2] == "0":
        for i in range(0, len(entrada)):
            if token == 0:
                senha += entrada[i]
            elif i > 1 and entrada[i] != "0":
                senha += entrada[i]
                token -= 1
        print(senha)
    else:
        print("RA INVALIDO")
    

senhara()