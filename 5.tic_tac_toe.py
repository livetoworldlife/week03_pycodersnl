# The Game Rules
print('Welcome to Tic Tac Toe,'
      '\nX’s always go first, letting the user make the first move.'
      '\nto win complete a straight line of your letter'
      '\n(Diagonal, Horizontal, Vertical).'
      '\nThe board has positions 1-9 starting at the top left. Such as this, '
      '\n 1 | 2 | 3 ''\n ----------''\n 4 | 5 | 6 ''\n ----------''\n 7 | 8 | 9 ')
# Creating a Board
# board is now: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
board = [' ' for x in range(10)]


# This function is going to take two parameters: letter & pos.
# It is simply going to insert the given letter at the given position.
def insert_letter(letter, pos):
    board[pos] = letter


# This function simply tell us if the given space is free.
# It has one parameter, pos, which will be an integer from 1-9.
# This function will return a True or False value
def space_is_free(pos):
    return board[pos] == ' '


# This function takes the board as a parameter and will display it to the console.
def print_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


# This function will tell us if the given letter has won based on the current board.
# It has two parameters: bo(board) & le(letter). The letter must be a “X” or an “O”.
# We will simply check each possible winning line on the board and see if it is populated by the given letter.
def is_winner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


move_count = 1


# In this function we will be asking the user to input a move and validating it.
# If the move is valid we will add that letter to the board.
# Otherwise we will continue to ask the user for input.
def player_move():
    global move_count
    run = True
    while run:  # Keep looping until we get a valid move
        move = input('\nPlease select your {}. position to place an \'X\' (1-9): '.format(move_count))
        try:
            move = int(move)
            if 0 < move < 10:  # makes sure we type in a number between 1-9
                if space_is_free(move):  # check if the move we choose is valid (no other letter is there already)
                    run = False
                    move_count += 1
                    insert_letter('X', move)
                else:
                    print('This position is already occupied!')
            else:
                print('Please type a number within the range!')
        except ValueError:
            print('Please type a number!')


"""
 This function will be responsible for making the computers move.
It will examine the board and determine which move is the best to make.
 The algorithm we will follow to do this is listed below.

If the current step cannot be completed proceed to the next.
1. If there is a winning move take it.
2. If the player has a possible winning move on their next turn move into that position.
3. Take any one of the corners. If more than one is available randomly decide.
4. Take the center position.
5. Take one of the edges. If more than one is available randomly decide.
6. If no move is possible the game is a tie.
"""


def comp_move():
    # Create a list of possible moves
    pos_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    # Check for possible winning move to take or to block opponents winning move
    for let in ['O', 'X']:
        for i in pos_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    # Try to take one of the corners
    corners_open = []
    for i in pos_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    # Try to take the center
    if 5 in pos_moves:
        move = 5
        return move

    # Take any edge
    edges_open = []
    for i in pos_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)

    return move


# This function will randomly decide on a move to take given a list of possible positions
def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


# This function takes board as parameter and will simply return True
# if the board is full and False if it is not.
def is_board_full(board):
    if board.count(' ') > 1:  # Since we always have one blank element in board we must use > 1
        return False
    else:
        return True


# This function is what we will call to start the game.
# It will be calling all of the different functions in our program and dictate the flow of the program
def main():
    # Main game loop
    print_board(board)
    while not (is_board_full(board)):
        if not (is_winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not (is_winner(board, 'X')):
            move = comp_move()
            if move == 0:
                print('Game is a Tie! No more spaces left to move.')
            else:
                insert_letter('O', move)
                print('\nComputer placed an \'O\' in position', move, ':')
                print_board(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if is_board_full(board):
        print('Game is a tie! No more spaces left to move.')


# we want the game to keep running until the user doesn’t want to play anymore,
# so we will create a small while loop in the main line.

# this loop is for checking correct y/n input

whl_kon = True
while whl_kon:
    answer = input('Do you want to play? (Y/N) : ')
    if answer in ["Y", "y", "yes", "Yes"]:
        board = [' ' for x in range(10)]
        print('********* NEW GAME IS STARTED **********\n')
        main()
        whl_kon = False
    elif answer in ["N", "n", "no", "No"]:
        print("Thanks for The Game!!!")
        break
    else:
        print("Please! To play again (Y), To quit (N)")
