import math
def entropia(entrada: input) -> int:
    ums = 0
    for i in range(0, len(entrada)):
        ums += int(entrada[i])
    probabilidade = ums / len(entrada)
    if probabilidade == 1:
        return 0.0000
    entropia = -(probabilidade * math.log2(probabilidade) + (1 - probabilidade)*(math.log2(1-probabilidade)))
    return entropia

        
primeiro = input()
segundo = input()
if entropia(primeiro) > entropia(segundo):
    print("2")
else:
    print("1")