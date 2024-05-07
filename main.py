# Welcom to Dice Roll Game
# Register, Login, Exit
# if invalid, print Invalid choice. Please try again.

# Register
# Enter username (4) leave blank to cancel
# Enter password (8) leave blank to cancel

# Login
# ENter username and password

# login menu
# Start, show, log out

# Start
# user rolls, computer rolls, compare rolls
# if user wins, Total Points: (n), Stages Won: (n)
# Continue (1 yes, 0 no)
# if invalid, try again

# Scoring
# win 1 round, 1 point
# win 1 stage, 3 points
# score = 0 at the start

# Show
# show top 10 highest score
# if no games played or first game lose, No games played yet. Play a game to see top scores. (back to menu)
# 1. {user}: points - {points}, Wins - {stage}
import sys
import utils.dice_game
from utils.user_manager import User_Manager

def main():
    print("\nWelcome to Dice Roll Game!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    while True:
        choice = input("What is your input?: ")
        try:
            if choice == "1":
                register = User_Manager()
                register.register()
                break
            elif choice == "2":
                login = User_Manager()
                login.login()
                break
            elif choice == "3":
                sys.exit()
            else:
                print("Invalid Input!")
        except ValueError:
            return
        
if __name__ == "__main__":
    main()