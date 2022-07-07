def get_quotient_remainder(x, y):
    return int(x / y), int(x % y)

x = 10
y = 3
quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))
