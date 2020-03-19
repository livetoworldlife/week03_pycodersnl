"""
Winning Rules as follows :
Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins.
"""

# This module implements pseudo-random number generators for various distributions.
import random

comp_wins, player_wins = 0, 0

rules_for_print = "Winning Rules as follows :" \
        "\nRock vs Paper-> Paper wins" \
        "\nRock vs Scissor-> Rock wins" \
        "\nPaper vs Scissor-> Scissor wins.\n"

print(rules_for_print)

# functions is the subject of next week. it is a good option to use them in this code
# This function has no parameter, returns user choices value
def user_opt_fon():
    whl_run = True
    while whl_run:  # Keep looping until we get a valid move
        user_opt = input("1.Rock"
                         "\n2.Paper"
                         "\n3.Scissor"
                         "\nEnter choice: ")

        user_cho = ""
        try:
            user_opt = int(user_opt)
            # loop for checking invalid input number
            while user_opt > 3 or user_opt < 1:
                user_opt = int(input("Please Enter 1, 2 or 3. Try again: "))

            # equalize options to user input
            if user_opt == 1:
                user_cho = "Rock"
            elif user_opt == 2:
                user_cho = "Paper"
            elif user_opt == 3:
                user_cho = "Scissor"
            print("\nUser turn: {} "
                  "\nUser choice is: {}".format(user_opt, user_cho))
            return user_cho
        except ValueError:
            print('Please type a number!')



# random.randint(a, b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
# This function has no parameter, returns random value of the computer

def computer_opt_fon():
    comp_cho = random.randint(1, 3)
    if comp_cho == 1:
        comp_cho = "Rock"
    elif comp_cho == 2:
        comp_cho = "Paper"
    else:
        comp_cho = "Scissor"
    print("Computer choice is: ", comp_cho)
    return comp_cho

# loop to make continue the game until user pres no
whl_kont = True
while whl_kont:
    win_print = ""
    print("***********************")

    user_choice = user_opt_fon()
    print("\nNow its computer turn.......\n")
    comp_choice = computer_opt_fon()

    print("************************")
    if user_choice == comp_choice:
        win_print = "Tie. No Winner"

    if user_choice == "Rock":
        if comp_choice == "Paper":
            win_print = "You lose."
            comp_wins += 1

        elif comp_choice == "Scissor":
            win_print = " You win."
            player_wins += 1

    elif user_choice == "Paper":
        if comp_choice == "Rock":
            win_print = " You win."
            player_wins += 1

        elif comp_choice == "Scissor":
            win_print = "You lose."
            comp_wins += 1

    elif user_choice == "Scissor":
        if comp_choice == "Rock":
            win_print = "You lose."
            comp_wins += 1
        elif comp_choice == "Paper":
            win_print = " You win."
            player_wins += 1

    print("{} V/s {}. {} !!! \n".format(user_choice, comp_choice, win_print))

    # this loop is for checking correct y/n input
    whl_kont2 = True
    while whl_kont2:
        user_yn = input("Do you want to play again? (y/n) : ")
        if user_yn in ["Y", "y", "yes", "Yes"]:
            whl_kont2 = False
        elif user_yn in ["N", "n", "no", "No"]:
            print("------Game Result------")
            print("User wins: " + str(player_wins))
            print("Computer wins: " + str(comp_wins))
            print("")
            whl_kont = False
            break
        else:
            print("Please! To play again (Y), To quit (N)")


