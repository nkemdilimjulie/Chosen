import sys

"""Game Operations"""
from create_dice import D4, D6, D8, D10


def roll_dice():
    """rolls dice"""
    d4 = D4()
    d6 = D6()
    d8 = D8()
    print(f"D4, D6, D8: {[d4, d6, d8]}")
    dice_faces = [d4, d6, d8]
    return dice_faces


def roll_with_extra_dice():
    """rolls extra dice"""
    d4 = D4()
    d6 = D6()
    d8 = D8()
    d10 = D10()
    print(f"D4, D6, D8, D10: {[d4, d6, d8, d10]}")
    dice_faces_extra = [d4, d6, d8, d10]
    return dice_faces_extra


def check_dice_rolled(d4, d6, d8, d10=None):
    """checks for a winner"""
    if d4 == d6 and d6 == d8:
        print("Hurray! You've won the game!")
        print("... END OF GAME ...")
        ends_game()
        if d10:
            if d4 == d6 and d6 == d8 and d8 == d10:
                print("Hurray! You've won the game with extra dice!")
                print("... END OF GAME ...")
                ends_game()


def ends_game():
    """ends the game"""
    print("Thanks for playing!")
    sys.exit()
