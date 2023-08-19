def potencia(base: int, expoente: int) -> float:
    if expoente == 0:
        return 1
    if expoente == 1:
        return base
    return base * potencia(base, expoente-1)


potencia(1/2,-3)