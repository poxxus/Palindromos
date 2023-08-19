def tempo_jogo():
    horaI = int(input())
    minI = int(input())
    horaF = int(input())
    minF = int(input())
    minutos = 0
    if horaI == horaF and minI == minF:
        minutos = 1440
    while horaI != horaF or minI != minF:
        minI += 1
        if minI >= 60:
            horaI += 1
            minI = 0
        if horaI >= 24:
            horaI = 0
        minutos += 1
    return print(f"{minutos//60}h{minutos%60}m")
        
        
tempo_jogo()