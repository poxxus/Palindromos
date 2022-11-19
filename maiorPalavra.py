from sys import stdin
list1 = []
for i in stdin:
    if i == "EOF":
        break
    list1.append(i)
if not list1:
    print("Nenhuma palavra foi informada")
else:
    list1.sort(key=len, reverse=True)
    print("A maior palavra informada foi", list1[0])
