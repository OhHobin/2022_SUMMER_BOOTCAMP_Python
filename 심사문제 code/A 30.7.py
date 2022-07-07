korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*x):
    l = []
    for i in x:
        l.append(i)
    l = sorted(l)
    return l[0], l[len(l)-1]

def get_average(**x):
    sum = 0
    for i, j in x.items():
        sum += int(j)
    return sum/len(x)

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}' .format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}' .format(min_score, max_score, average_score))