def tri_tetra_nacci(n: int, nome:str) -> int:
    if nome == "Tribonacci":
        return Tribonacci(n)
    elif nome == "Tetranacci":
        return Tetranacci(n)
    else:
        return print("SEQUENCIA DESCONHECIDA")
        

def Tribonacci(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1
    return Tribonacci(n-1) + Tribonacci(n-2) + Tribonacci(n-3)

def Tetranacci(n: int) -> int:
    if n in [0,1,2]:
        return 0
    if n == 3:
        return 1
    return Tetranacci(n-1) + Tetranacci(n-2) + Tetranacci(n-3) + Tetranacci(n-4)


tri_tetra_nacci(20, Tribonacci)