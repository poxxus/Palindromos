def catalan(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    soma = 0
    for i in range(0, n):
        soma += catalan(i)*catalan(n-i-1)
    return soma
    
    