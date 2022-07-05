x, y = map(int,input().split())

def clac(x, y):
    return x+y, x-y, x*y, x/y

a, s, m, d = clac(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셉: {2}, 나눗셈: {3}'.format(a, s, m, d))