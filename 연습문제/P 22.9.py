a = ['alpha','bravo','charlie','delta','echo','foxtrot','golf','hotel','india']
b =[]
for i in range(len(a)):
    if len(a[i]) == 5:
        b.append(a[i])
print(b)