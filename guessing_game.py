from pyfiglet import figlet_format
from random import randint

def main():
    """Main game file of Guessing Game."""
    print(''.center(100, '_'))
    print(figlet_format("Guessing Game"))
    print(''.center(100, '_')) 
    level_text = """    
Choose a level:
    [1] Easy
    [2] Normal
    [3] Hard
"""
    try:
        level_chosed = int(input(level_text + "---> "))
    except ValueError:
        print("Please enter an integer ")
        main()
    else:
        if level_chosed == 1:
            answer = randint(1, 10)
            guess_num = int(input("What is your guess number(1-10): "))
            while guess_num != answer:
                if guess_num < answer:
                    print("Higher")
                    guess_num = int(input("What is your guess number(1-10): "))
                elif guess_num > answer:
                    print("lower")
                    guess_num = int(input("What is your guess number(1-10): "))
                else:
                    print("level exceeded\nYou die!")
            if guess_num == answer:
                    print("Your Guess is right!!!")
                    play_again = input("Do you want to play again?(Y/N): ")
                    if play_again.lower() == 'y':
                        main()
                    elif play_again.lower() == 'n':
                        print(figlet_format("Thank you for playing", font="slant"))
                    else:
                        print("get loss")

        elif level_chosed == 2:
            answer = randint(1, 30)
            guess_num = int(input("What is your guess number(1-30): "))
            while guess_num != answer:
                if guess_num < answer:
                    print("Higher")
                    guess_num = int(input("What is your guess number(1-30): "))
                elif guess_num > answer:
                    print("lower")
                    guess_num = int(input("What is your guess number(1-30): "))
                else:
                    print("level exceeded\nYou die!")
            if guess_num == answer:
                    print("Your Guess is right!!!")
                    play_again = input("Do you want to play again?(Y/N): ")
                    if play_again.lower() == 'y':
                        main()
                    elif play_again.lower() == 'n':
                        print(figlet_format("Thank you for playing", font="slant"))
                    else:
                        print("get loss")
        elif level_chosed == 3:
            answer = randint(1, 50)
            print("This is a one time only go be a magician guess that number!")
            guess_num = int(input("What is your guess number(1-50): "))
            if guess_num == answer:
                print("Your Guess is right!!!")
        else:
            print("maintenance")

    
main()