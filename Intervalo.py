# intervalo
def intervalo():
    num = float(input())
    if 0 <= num <= 25:
        return print(f"Intervalo [0,25]")
    if 25 < num <= 50:
        return print(f"Intervalo (25,50]")
    if 50 < num <= 75:
        return print(f"Intervalo (50,75]")
    if 75 < num <= 100:
        return print(f"Intervalo (75,100]")
    else:
        return print(f"Fora de intervalo")


intervalo()
