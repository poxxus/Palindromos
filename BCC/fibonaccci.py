N = int(input())
list1 = [0, 1, 1]
if N == 1:
    print(0)
elif N == 2 or N == 3:
    print(1)
for i in range(3, N):
    Fib = list1[-1] + list1[-2]
    list1.append(Fib)
print(Fib)
