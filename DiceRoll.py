import  random

print('This is a multiple side dice rolling simulator ;)')

def main():
    dice_sides = int(input('Please set your number of sides (2-100)'))

    rolling_the_dice = True
    while rolling_the_dice:
        roll_try = input('Ready to roll ? If you are press anything but (N)')
        if roll_try != 'n'.lower():
            rolled_number = random.randrange(1, dice_sides)

            print('you rolled: ', rolled_number)
        else:
            rolling_the_dice = False
            print('Thanks for rolling ;)')
main()