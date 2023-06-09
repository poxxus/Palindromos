def xorgate():
    a = bool(int(input()))
    b = bool(int(input()))
    c = False
    d = False
    if a and not b:
        c = True
    if b and not a:
        d = True
    if c or d:
        return print("1")
    else:
        return print("0")


xorgate()



