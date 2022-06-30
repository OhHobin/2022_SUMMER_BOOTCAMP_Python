a = list(map(int, input().split()))
b = a[0] + a[1] + a[2] + a[3]

if a[0] < 0 or a[0] > 100 or a[1] < 0 or a[1] > 100 or a[2] < 0 or a[2] > 100 or a[3] < 0 or a[3] > 100:
        print('잘못된 점수')
else:
    if b / 4 >= 80:
        print('합격')
    elif b / 4 < 80:
        print('불합격')