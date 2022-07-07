def get_max_score(*x):
    n = max(x)
    return n

k, e, m, s = 100, 86, 81, 91
max_score = get_max_score(k, e, m, s)
print('높은 점수:', max_score)
max_score = get_max_score(e, s)
print('높은 점수:', max_score)
