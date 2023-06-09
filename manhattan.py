def distancia():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    dis = (abs(x1 - x2)) + (abs(y1 - y2))
    return print(f"{dis}")


distancia()
