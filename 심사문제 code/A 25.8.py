keys = input().split()
values = map(int, input().split())

x = dict(zip(keys,values))

x = {a:b for a, b in x.items() if b != 30}
x = {a:b for a, b in x.items() if a != 'delta'}
print(x)