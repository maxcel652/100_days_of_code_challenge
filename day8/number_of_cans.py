import math
def buy_paint(height, width):
    coverage = 5
    number_of_cans = math.ceil(height * width / coverage) 
    print(f"You need {number_of_cans}  cans of paint.")

wall_height = float(input("Enter the height of the wall. "))
wall_width = float(input("Enter the width of the wall. "))
buy_paint(height = wall_height, width = wall_width)
