def cores():
    r = bool(int(input()))
    g = bool(int(input()))
    b = bool(int(input()))
    if b:
        if r:
            if g:
                print("7")
            else:
                print("2")
        elif g:
            print("6")
        else:
            print("1")
    elif r:
        if g:
            print("4")
        else:
            print("3")
    elif g:
        print("5")
    else:
        print("8")


cores()
