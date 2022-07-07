x = {'a':1, 'b':2, 'c':3}
x.update(a=10)
print(x)
print(x.pop('a'))
print(x)
del x['b']
print(x)
print(x.get('c'))

y = {'x':10, 'y':20, 'z':30}
print(y.items(), y.keys(), y.values())

z = ['q', 'w', 'e', 'r', 't']
print(dict.fromkeys(z, 1))