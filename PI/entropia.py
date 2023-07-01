import math
def entropia():
    ums = 0
    entrada = input()
    for i in range(0, len(entrada)):
        ums += int(entrada[i])
    probabilidade = ums / len(entrada)
    if probabilidade == 1:
        return print("0.0000")
    entropia = -(probabilidade * math.log2(probabilidade) + (1 - probabilidade)*(math.log2(1-probabilidade)))
    print(f"{entropia:.4f}")

        
entropia()
