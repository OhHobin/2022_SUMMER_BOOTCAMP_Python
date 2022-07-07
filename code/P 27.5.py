xfp = None
xlist = []
num = 0
xfp = open('C:/Users/LG/git python/code/words.txt', 'r', encoding='UTF-8')

xlist = xfp.readlines()
for i in range(len(xlist)):
    if len(xlist[i].rstrip('\n')) <= 10:
        num += 1
print(num)

xfp.close()