"""
Name: Brett Widholm
lab9.py

Description: This program creates a virtual tic-tac-toe board for the
user to play with one other player.

This work is entirely my own.
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    build_board()
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)



def is_legal(board, position):
    counter = 0
    if board[position] == 'x' or board[position] == 'o':
        return False

    else:
        if counter % 2 == 0:
            counter = counter + 1
            return True
        elif counter % 2 != 0:
            counter = counter + 1
            return True


def fill_spot(board, position, character):
    if is_legal(board, position) == True:
        board[position] = character

    else:
        pass


def winning_game(board):
    if board[0] == board[1] == board[2]:
        return True
    if board[3] == board[4] == board[5]:
        return True
    if board[6] == board[7] == board[8]:
        return True
    if board[0] == board[3] == board[6]:
        return True
    if board[1] == board[4] == board[7]:
        return True
    if board[2] == board[5] == board[8]:
        return True
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    else:
        return False


def game_over(board):
    if winning_game(board) == True:
        return True
    else:
        return False

def get_winner(board):
    if game_over(board) == True:
        if board[0] == board[1] == board[2]:
            return board[0]
        if board[3] == board[4] == board[5]:
            return board[3]
        if board[6] == board[7] == board[8]:
            return board[6]
        if board[0] == board[3] == board[6]:
            return board[0]
        if board[1] == board[4] == board[7]:
            return board[1]
        if board[2] == board[5] == board[8]:
            return board[2]
        if board[0] == board[4] == board[8]:
            return board[0]
        if board[2] == board[4] == board[6]:
            return board[2]
    else:
        return None


def play(board):
    print('Instructions:')
    print('You must match your symbol three times in a line to win.')
    print('You may not place your symbol over an existing symbol.')
    print('Use the number keys to pick that section.')
    turn = 0
    turn_counter = 0

    while turn == 0:
        if turn_counter >= 9:
            print("Nobody! Cat's game.")
            print_board(board)
            user_input = input('Do you want to play again?')
            if user_input[0] == 'y' or user_input[0] == 'Y':
                main()
            else:
                pass
        else:
            pass
        print_board(board)
        print("It's x's turn")
        character = 'x'
        position = eval(input('What position do you want? '))
        position = position - 1
        is_legal(board, position)
        if is_legal(board, position) == False:
            print('Pick a spot that is unoccupied.')
        else:
            fill_spot(board, position, character)
            winning_game(board)
            if winning_game(board) == True:
                game_over(board)
                if game_over(board) == True:
                    get_winner(board)
                    if get_winner(board) == 'x':
                        print_board(board)
                        print("x's win!")
                        user_input = input('Do you want to play again?')
                        if user_input[0] == 'y' or user_input[0] == 'Y':
                            main()
                        else:
                            turn = 2
                    if get_winner(board) == 'o':
                        print_board(board)
                        print("o's win!")
                        user_input = input('Do you want to play again?')
                        if user_input[0] == 'y' or user_input[0] == 'Y':
                            main()
                        else:
                            turn = 2
                if turn == 2:
                    print('Good game!')
                    input('')

            turn = 1
            turn_counter = turn_counter + 1
        while turn == 1:
            if turn_counter >= 9:
                print("Nobody! Cat's game.")
                print_board(board)
                user_input = input('Do you want to play again?')
                if user_input[0] == 'y' or user_input[0] == 'Y':
                    main()
                else:
                    turn = 2
            else:
                pass
            print_board(board)
            print("It's o's turn")
            character = 'o'
            position = eval(input('What position do you want? '))
            position = position - 1
            is_legal(board, position)
            if is_legal(board, position) == False:
                print('Pick a spot that is unoccupied.')
            else:
                fill_spot(board, position, character)
                winning_game(board)
                if winning_game(board) == True:
                    game_over(board)
                    if game_over(board) == True:
                        get_winner(board)
                        if get_winner(board) == 'x':
                            print_board(board)
                            print("x's win!")
                            user_input = input('Do you want to play again?')
                            if user_input[0] == 'y' or user_input[0] == 'Y':
                                main()
                            else:
                                turn = 2
                        if get_winner(board) == 'o':
                            print_board(board)
                            print("o's win!")
                            user_input = input('Do you want to play again?')
                            if user_input[0] == 'y' or user_input[0] == 'Y':
                                main()
                            else:
                                turn = 2
                    if turn == 2:
                        print('Good game!')
                        input('')



                turn = 0
                turn_counter = turn_counter + 1



def main():
    play(build_board())


if __name__ == '__main__':
    main()

