def countdown(n):
    def cd():
        nonlocal n
        n -= 1
        return n
    n += 1
    return cd


n = int(input())
c = countdown(n)
for i in range(n):
    print(c(), end=' ')