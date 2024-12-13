#rock, paper, scissors game
import random

game_titles = ["Rock", "Paper", "Scissors"]

user_choice = int(input("Choose either 1, 2, or 0 for your moves. "))

computer_move = random.randint(0, 2)

result = " "
if user_choice == 0 and computer_move == 1:
    result = "computer wins"
     print(f"computer choose {game_titles[computer_move]}\n You choose {game_titles[user_choice]}\n {result}")
     
elif  user_choice == 1 and computer_move == 0:
    result = "You win"
    print(f"computer choose {game_titles[computer_move]}\n You choose {game_titles[user_choice]}\n {result}")
     
elif  user_choice == 1 and computer_move == 2:
    result = "computer wins"
    print(f"computer choose {game_titles[computer_move]}\n You choose {game_titles[user_choice]}\n {result}")
    
elif  user_choice == 2 and computer_move == 1:
    result = "You win"
    print(f"computer choose {game_titles[computer_move]}\n You choose {game_titles[user_choice]}\n {result}")
elif  user_choice == 2 and computer_move == 0:
    result = "computer wins"
    print(f"computer choose {game_titles[computer_move]}\n You choose {game_titles[user_choice]}\n {result}")
    
elif  user_choice == 0 and computer_move == 2:
    result = "You win"
    print(f"computer choose {game_titles[computer_move]}\n You choose {game_titles[user_choice]}\n {result}")
     
else:
    result = "Draw"
    print(f"computer choose {game_titles[computer_move]}\n You choose {game_titles[user_choice]}\n {result}")