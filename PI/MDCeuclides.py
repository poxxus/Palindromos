def mdc(a: int, b: int) -> int:
    if (a % b) == 0:
        return b
    return mdc(b, a % b)