a = input().split()
b = input().split()
for i in range(len(b)):
    b[i] = float(b[i])
c = dict(zip(a,b))
print(c)