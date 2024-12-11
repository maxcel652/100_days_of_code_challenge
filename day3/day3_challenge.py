

print('Welcome to Treasure Island')
print('Your mission is to find the treasure.')

direction = input("Which way do you wanna take? ").capitalize()
if direction == "Left":
    swim_wait = input("swim or wait ").capitalize()
    if swim_wait == "Wait":
        print("Here's your boat, enter to cross.")
        choose_door = input("Which door? Blue, Red, Yellow? ").capitalize()
        if choose_door == "Yellow":
            print("Congratulations, you found the treasure.")
        elif choose_door == "Blue":
            print("Oops, you died in a burning room. Game over")
        else:
            Print("This is a very bad decision. You're eaten up by lions. Game over.")
    else:
        print("You drown. Game over")
else:
    print("Oh no! You've been shot. Game over")
