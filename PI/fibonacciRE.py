def fibonacci(n:int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n < 0:
        if n % 2 == 0:
            return -1**(-n + 1)*fibonacci(-n)
        return 1**(-n + 1)*fibonacci(-n)
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(-24)