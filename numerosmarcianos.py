from sys import stdin
i = str
substitutos = [("8", "4"), ("9", "5"), ("7", "6"), ("2", "9"), ("5", "1"), ("6", "2"), ("4", "3"), ("3", "7"), ("1", "8")]
for i in stdin:
    if i == "0":
        break
    else:
        for num, marc in substitutos:
            if num in i:
                i = i.replace(num, marc)
                print(i)
                break
