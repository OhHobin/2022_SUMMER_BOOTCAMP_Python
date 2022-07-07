x, y = map(int,input().split())
m = []

for i in range(y):
    m.append(list(input()))

for i in range(x):
    for j in range(y):
        if m[i][j] == '.':
            num = 0
            for q in range(-1, 2):
                for w in range(-1, 2):
                    if x > i + q >= 0 and y > j + w >= 0:
                        if m[i+q][j+w] == '*':
                             num += 1
            m[i][j] = num
        else:
            pass
print(m)
