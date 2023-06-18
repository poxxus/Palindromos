a = str(1)
list_result = []
n = int(input())

for i in range(0, n - 1):
    a = "-" + a + "-"
list_result.append(a)
a = "1"

for i in range(0, n - 1):
    a = "1" + a + "1"
    while len(a) < (2 * n)-2:
        a = "-" + a + "-"
    list_result.append(a)
    a = a.replace("-", '')

print('\n'.join(list_result))
