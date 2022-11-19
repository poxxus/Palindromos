a = 9999
while a != 0:
    a = int (input())
    if (a != 0):
        a1 = a // 1000
        a  = a % 1000
        a2 = a // 100
        a  = a % 100
        a3 = a // 10
        a4 = a % 10
        print ("%d %d %d %d" % (a1, a2, a3, a4))





