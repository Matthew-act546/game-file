from pyfiglet import figlet_format
from random import randint

description = """
Game Mechanics!

Guess the number what matthew thinking in his mind.
NOOB(EASY) LEVEL OR BABY MATTHEW LEVEL HAVE A LIMITATION OF 10 IN HIS MIND IF YOU SOLVED THIS YOU ARE NOOB!
PRO(NORMAL) LEVEL OR TEEN MATTHEW LEVEL HAVE A LIMTAITION OF 30 NUMBERS IN HIS MIND IF YOU SOLVED THIS YOU ARE PRO!
HACKER(HARD) LEVEL OR ADULT MATTHEW LEVEL HAVE A LIMITATION OF 50 NUMVERS IN HIS MIND IF YOU SOLVED THIS YOU ARE HACKER!"""

print(''.center(130, '_'))
print(figlet_format("Guess Number") + description)
print(''.center(130, '_')) 

def main():
    """Main game file of Guessing Game."""
    
    level_text = """Levels:
[1] NOOB
[2] PRO
[3] HACKER
"""
    try:
        level_chosed = int(input(level_text + "Choose Level: "))
    except ValueError:
        print("Please enter an integer ")
        main()
    else:
        if level_chosed == 1:
            attempt = 0
            lives = 3
            answer = randint(1, 10)
            while attempt < lives:
                try:
                    guess_num = int(input("What is your guess number(1-10): "))
                    if 1 <= guess_num <= 10:
                        if guess_num == answer:
                            print("Your Guess is right!!!")
                            play_again = input("Do you want to play again?(Y/N): ")
                            if play_again.lower() == 'y':
                                play()
                            elif play_again.lower() == 'n':
                                print(figlet_format("Thank you for playing", font="slant"))
                                attempt = 4
                            else:
                                print("get loss")
                        elif guess_num < answer:
                            print("Higher")
                            attempt += 1
                        elif guess_num > answer:
                            print("Lower")
                            attempt += 1
                    else:
                        print("Please enter 1 to 10")
                except ValueError:
                    print("Enter a number")
            if attempt == 3:
                print(figlet_format("YOU DIE!!!"))
                
        elif level_chosed == 2:
            attempt = 0
            lives = 3
            answer = randint(1, 30)
            while attempt < lives:
                try:
                    guess_num = int(input("What is your guess number(1-30): "))
                    if 1 <= guess_num <= 30:
                        if guess_num == answer:
                            print("Your Guess is right!!!")
                            play_again = input("Do you want to play again?(Y/N): ")
                            if play_again.lower() == 'y':
                                play()
                            elif play_again.lower() == 'n':
                                print(figlet_format("Thank you for playing", font="slant"))
                                attempt = 4
                            else:
                                print("get loss")
                        elif guess_num < answer:
                            print("Higher")
                            attempt += 1
                        elif guess_num > answer:
                            print("Lower")
                            attempt += 1
                    else:
                        print("Please enter 1 to 30")
                except ValueError:
                    print("Enter a number")
            if attempt == 3:
                print(figlet_format("YOU DIE!!!"))

        elif level_chosed == 3:
            attempt = 0
            lives = 3
            answer = randint(1, 10)
            while attempt < lives:
                try:
                    guess_num = int(input("What is your guess number(1-10): "))
                    if 1 <= guess_num <= 30:
                        if guess_num == answer:
                            print("Your Guess is right!!!")
                            play_again = input("Do you want to play again?(Y/N): ")
                            if play_again.lower() == 'y':
                                play()
                            elif play_again.lower() == 'n':
                                print(figlet_format("Thank you for playing", font="slant"))
                                attempt = 4
                            else:
                                print("get loss")
                        elif guess_num < answer:
                            print("Higher")
                            attempt += 1
                        elif guess_num > answer:
                            print("Lower")
                            attempt += 1
                    else:
                        print("Please enter 1 to 10")
                except ValueError:
                    print("Enter a number")
            if attempt == 3:
                print(figlet_format("YOU DIE!!!"))
        else:
            print("Enter a number corresponding to the levels")
            main()


def play():
    """playing again the game with welcome back!"""
    print(figlet_format("Welcome back!"))
    main()

main()