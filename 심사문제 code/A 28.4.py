xlist = []
xfp = open('C:/Users/LG/git python/심사문제 code/words.txt', 'r', encoding='UTF-8')
xlist = xfp.readlines()

for i in range(len(xlist)):
    xlist[i] = xlist[i].rstrip('\n')

for i in range(len(xlist)):
    if list(xlist[i]) == list(reversed(xlist[i])):
        print(xlist[i])