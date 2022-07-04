x, y = map(int, input().split())
a = []
for i in range(x, y + 1):
    a.append(2**i)
print(a)