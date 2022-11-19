A = str(1)
list1 = []
N = int(input())
for i in range(0, N-1):
    A = "-" + A + "-"
list1.append(A)
A = "1"
for i in range(0, N-1):
    A = "1" + A + "1"
    while len(A) < (2*N)-2:
        A = "-" + A + "-"
    list1.append(A)
    A = A.replace("-", '')
print('\n'.join(list1))




