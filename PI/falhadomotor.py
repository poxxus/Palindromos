def motor():
    impressoes = 1
    anterior = 0
    testes = int(input())
    for i in range(1, testes + 1):
        rpm = int(input())
        if rpm >= anterior:
            anterior = rpm
        elif impressoes > 0:
            print(i)
            impressoes -= 1
    if impressoes == 1:
        print(0)
    
    

motor()
