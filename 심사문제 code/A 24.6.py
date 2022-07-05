x = input().split(';')
for i in range(len(x)):
    x[i] = int(x[i])

x = sorted(x, reverse=True)

for i in range(len(x)):
    x[i] = str(format(x[i], ','))
    print('%9s' % x[i])