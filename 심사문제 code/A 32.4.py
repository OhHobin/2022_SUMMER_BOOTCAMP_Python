files = input().split()
print(list(map(lambda x: x.split('.')[0].zfill(3) + '.' + x.split('.')[1],files)))