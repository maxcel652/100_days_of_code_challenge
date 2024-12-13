# fruits = ["mango", "orange", "pear"]
# fruits.append("preach")
# print(fruits)
import random

names_string = input("Give me everybody's name seperated by a comma. ")
names = names_string.split(", ")
# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
payment_person = random.choice(names)

print(f"The person to pay the bills is {payment_person }")
 