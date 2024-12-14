import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'A', 'B', 'C', 'T', 'H', 'K']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your  password? "))

nr_symbols = int(input("How many symbols would you like? "))

nr_numbers = int(input("How many numbers would you like? "))

# group_password = [nr_letters, nr_symbols, nr_numbers]
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
    


for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
  


for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
   
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(password)
