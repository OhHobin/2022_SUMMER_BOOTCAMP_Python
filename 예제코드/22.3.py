a = [3,12,421,41214242,124]
for i in a:
    print(i)

print(sum(a))

a = [i for i in range(10) if i % 2 ==0]
print(a)

a = list(map(float, a))
print(a)