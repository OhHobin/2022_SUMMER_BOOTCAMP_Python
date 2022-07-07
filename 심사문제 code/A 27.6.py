xlist, nlist, nnlist = [], [], []
xfp = open('C:/Users/LG/git python/심사문제 code/words.txt', 'r', encoding='UTF-8')
xlist = xfp.readlines()

for i in range(len(xlist)):
    nlist.append(xlist[i].split())
for i in range(len(nlist)):
    for j in range(len(nlist[i])):
        for t in range(len(nlist[i][j])):
            if nlist[i][j][t] == 'c' and nlist[i][j][t+1] == 'c':
                continue
            elif nlist[i][j][t] == 'c':
                nnlist.append(nlist[i][j])
for i in range(len(nnlist)):
    nnlist[i] = nnlist[i].rstrip(',')
    nnlist[i] = nnlist[i].rstrip('.')
    print(nnlist[i])