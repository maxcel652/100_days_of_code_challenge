#assuming some friends went to eat, i want to write a program to determine how much each of them should pay depending on their number and percentage choosen
print("Welcome to the tip calculator!")
#first we're going to collect the inputs

total_bill = float(input('What was the total bill? '))
percentage_tip = int(input('What percentage tip would you like to give? '))
bill_splitting = int(input('How many people to slpit the bill? '))

#now we want to do some calculations

percentage = percentage_tip / 100
new_bill = ((total_bill * percentage ) + total_bill)/bill_splitting

print(f"Each person should pay ${round(new_bill, 2)}")