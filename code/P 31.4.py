def x(w):
    if w[0] != w[-1] and len(w) > 1:
        return False
    elif len(w) > 2:
        return x(w[1:len(w) - 1])
    else:
        return True

print(x('hello'))
print(x('level'))