#this is a pizza app

size = input("What type of pizza do you want? S, M, L ")

add_peperroni = input('do you want pepperroni? Y, N ')

extra_cheese = input('do you need an extra cheese? Y ')

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 30
    
if add_peperroni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is ${bill}")
