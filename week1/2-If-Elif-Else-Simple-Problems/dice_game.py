n = input("Enter dice sides: ")
n = int(n)
player_1 = input("Enter the Name of First Player: ")
player_2 = input("Enter the Name of Second Player: ")
from random import randint
dice_p1 = randint(1, n)
print("{} rolls {}".format(player_1, dice_p1))
dice_p2 = randint(1, n)
print("{} rolls {}".format(player_2, dice_p2))

if dice_p1 > dice_p2:
    print(player_1 + " wins!")
elif dice_p1 < dice_p2:
    print(player_2 + " wins!")
else:
    print("Tie! Roll again!")
