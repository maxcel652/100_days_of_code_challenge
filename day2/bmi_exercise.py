#this exercise is to calculate the body mass index of a user
#first, we collect the following inputs

height = float(input('Enter your height: '))
weight = float(input('Enter your weight: '))

#we now do the calculation 

bmi = weight // height**2

print(bmi)


