import math
def elementos():
    laranja = input().split(" ")
    banana = input().split(" ")
    laranja = [float(x) for x in laranja]
    banana = [float(x) for x in banana]
    if len(laranja) != len(banana):
        return print("ERRO")
    soma = 0
    for i in range(0, len(laranja)):
        soma += (laranja[i] - banana[i])**2
    soma = math.sqrt(soma)
    return print(f"{soma:.2f}")


elementos()