'''Main code operation'''
import time
from game_describe import game_description
from game_options import game_choice
from roll_operations import roll_dice
from roll_operations import roll_with_extra_dice
from roll_operations import check_dice_rolled

def main():
    '''dice game main'''
    game_description()
    game_choice()
    name = input("Please, enter your name: ")
    print('Welcome to Dice Game !', name)
    choice = 0
    choice = int(input('Select your choice (1 - 3): '))
    if choice == 1:
        number_of_trials = 0
        remaining_trials = 6
        while remaining_trials <= 6:
            if remaining_trials == 0:
                print("Sorry, your time is up")
                print('Game over!')
                play_again = input(f'{name}, Do you want to play again? ')
                if play_again in ["Yes", "yes", "Y", "y"]:
                    main()
                elif play_again not in ["Yes", "yes", "Y", "y"]:
                    break
            number_of_trials += 1
            input("Press ENTER to roll dice: ")
            print(f"\nRound {number_of_trials}, rolling dice ...")
            print('Your dice faces are:  ')
            dice_faces = roll_dice()
            time.sleep(1)
            check_dice_rolled(*dice_faces)
            remaining_trials = 6 - number_of_trials
            print(f'You have {6-number_of_trials} more chance(s)')
    elif choice == 2:
        number_of_trials = 0
        remaining_trials = 6
        while remaining_trials <= 6:
            if remaining_trials == 0:
                print("Sorry, your time is up")
                print('Game over!')
                play_again = input(f'{name}, Do you want to play again? ')
                if play_again in ["Yes", "yes", "Y", "y"]:
                    main()
                elif play_again not in ["Yes", "yes", "Y", "y"]:
                    break
            number_of_trials += 1
            input("Press ENTER to roll dice: ")
            print(f"Round {number_of_trials}, rolling dice ...")
            print('Your dice faces are:  ')
            dice_faces_extra = roll_with_extra_dice()
            time.sleep(1)
            check_dice_rolled(*dice_faces_extra)
            remaining_trials = 6 - number_of_trials
            print(f'You have {6-number_of_trials} more chance(s)')
    elif choice == 3:
            print('Game over')

if __name__ == '__main__':
    main()
   