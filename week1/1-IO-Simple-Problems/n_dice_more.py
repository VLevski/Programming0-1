from random import randint

N = input("Enter the Number of Dice Sides: ")
N = int(N)

dice_0 = randint(1, N)
print("First roll is: {}".format(dice_0))
dice_1 = randint(1, N)
print("Second roll is: {}".format(dice_1))
dice_2 = randint(1, N)
print("Third roll is: {}".format(dice_2))

print("Sum of all rolls is: {}".format(dice_0 + dice_1 + dice_2))
