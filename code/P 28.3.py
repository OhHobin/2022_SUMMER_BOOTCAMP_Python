n = int(input())
text = input()
world = text.split()
n_gram = []
if len(text) < n:
    print('wrong')
else:
    for i in range(n):
        n_gram.append(world[i:n+i])

for i in range(len(n_gram)):
    if len(n_gram[i]) == n:
        print(tuple(n_gram[i]))
    else:
        continue