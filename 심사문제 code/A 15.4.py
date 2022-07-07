age = int(input())
balance = 9000
x = 0
if age >= 7 and age <= 12:
    x = 650
elif age >= 13 and age <= 18:
    x = 1050
elif age >= 19:
    x = 1250
balance -= x
print(balance)