weight = int(input('What is your weight? '))
height = int(input('What is your heigh? '))

bmi_value = weight / height**2

print(f"Your body mass index is {bmi_value}")

if bmi_value <= 18.5:
    print("You are underweight")
elif bmi_value <= 25:
    print('You have a normal weight.')
elif bmi_value <= 30:
    print('You are overwieght.')
elif bmi_value <= 35:
    print('You are obese.')

else:
    print('You are clinically obese.')


