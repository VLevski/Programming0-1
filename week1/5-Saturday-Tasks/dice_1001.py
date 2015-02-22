player_1 = input("Enter Player's #1 Name: ")
player_2 = input("Enter Player's #2 Name: ")
dice = input("Enter the number of dices: ")
sides = input("Enter the number of dice sides: ")
goal = input("Enter target number: ")
start = input("Enter starting number: ")
dice = int(dice)
sides = int(sides)
goal = int(goal)
start = int(start)

from random import randint

points_1 = start
points_2 = start
roll_counter = 0

while True:
    roll = 0
    dice_n = 1
    while dice_n <= dice:
        roll += randint(1, sides)
        dice_n += 1
    if points_1 > goal:
        points_1 -= roll
    else:
        points_1 += roll
    roll_counter += 1
    print("After roll #{} player {} has {} points".format(roll_counter, player_1, points_1))
    if points_1 == goal:
        print("Player {} has riched the goal {}. Wins in {} rolls.\nPlayer {} loose with {} points.".format(player_1, goal, roll_counter, player_2, points_2))
        break
    roll = 0
    dice_n = 1
    while dice_n <= dice:
        roll += randint(1, sides)
        dice_n += 1
    if points_2 > goal:
        points_2 -= roll
    else:
        points_2 += roll
    print("After roll# {} player {} has {} points".format(roll_counter, player_2, points_2))
    if points_2 == goal:
        print("Player {} has riched the goal {}. Wins in {} rolls.\nPlayer {} loose with {} points.".format(player_2, goal, roll_counter, player_1, points_1))
        break
    
