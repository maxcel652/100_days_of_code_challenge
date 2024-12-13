#here i'm writing a program to collect a year and check if the year is a leap year or not

year = int(input('What year do you want to check? '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year.')
        else:
            print('Not a leap year.')
    else:
        print('Leap year.')
else:
    print('Not a leap year.')
