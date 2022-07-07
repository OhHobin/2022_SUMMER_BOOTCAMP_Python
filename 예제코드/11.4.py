a = [1, 2, 3, 4, 5]
print(a[1:3])
print(a[4:-1])
print(a[1:4:2])
print(a[2:])
print(a[::2])
print(a[0:len(a)])
a[1:3] = ['a']
print(a)