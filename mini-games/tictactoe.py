import random

#function to display game board_layout
def board_layout(board):
    print(board[1]+'|'+board[2]+"|"+board[3])
    print(board[4]+'|'+board[5]+"|"+board[6])
    print(board[7]+'|'+board[8]+"|"+board[9])

#test_board = ['X','O','X','O','X','O','X','O','X','O']
#board_layout(test_board)

#function to take player input
def player_input():
    plyrinput = ''
    while not (plyrinput == 'X' or plyrinput == 'O'):
        plyrinput = input('Player 1 input X or O :').upper()

        if plyrinput == 'X':

            return ('X','O')
        elif plyrinput == 'O':
            return ('O','x')
        else:
            print('Please Input Only \'X\' OR \'Y\'')


#function to to place user input on game board
def place_input(board,plyrinput,position):
    board[position] = plyrinput

#place_input(test_board,'$',4)
#board_layout(test_board)

#function to check if a player has won
def win_check(board,plyrinput):
    return((board[1] == plyrinput and board[2] == plyrinput and board[3] == plyrinput) or
    (board[4] == plyrinput and board[5] == plyrinput and board[6] == plyrinput) or
    (board[7] == plyrinput and board[8] == plyrinput and board[9] == plyrinput) or
    (board[9] == plyrinput and board[5] == plyrinput and board[1] == plyrinput) or
    (board[7] == plyrinput and board[5] == plyrinput and board[3] == plyrinput) or
    (board[2] == plyrinput and board[5] == plyrinput and board[8] == plyrinput))

#win_check(test_board,'X')

#function to decide player to go first
def first_to_play():
    sync = random.randint(0,1)
    if sync == 0:
        return('Player1')
    else:
        return('Player2')


#function that checks for space on board
def board_space_check(board, position):

    return board[position] == " "

#function to check if board is full
def board_full_check(board):
    for i in range(1,10):
        if board_space_check(board,i):
            return False
        else:
            return True


#function TO TAKE IN PLAYERS Position
def player_position(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not board_space_check(board,position):
        try:
           val = int(input('Input Position :'))
        except ValueError:
           print('Input Only numbers from 1-9 pls')
           continue
        return val

#function to replay the game
def replay():
     option = input('Do You want to replay: (y/n) ')
     return option == 'y'


print('Welcome to TIC TOE Game')

while True:
    game_board = [' ']*10
    play_turn = first_to_play()
    print(play_turn + " Goes First")
    player1,player2 = player_input()

    play_game = input('Are you ready to play: (y/n) ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if play_turn == 'player1':
           board_layout(game_board)
           position = player_position(game_board)
           place_input(game_board,player1,position)

           if win_check(game_board,player1):
               board_layout(game_board)
               print('Player 1 has won')
               game_on = False
           else:
               if board_full_check(game_board):
                   board_layout(game_board)
                   print('GAME TIE')
                   game_on = False
               else:
                   play_turn = 'player2'
        else:
               board_layout(game_board)
               position = player_position(game_board)
               place_input(game_board,player2,position)

               if win_check(game_board,player2):
                   board_layout(game_board)
                   print('Player 2 has won')
                   game_on = False
               else:
                   if board_full_check(game_board):
                       board_layout(game_board)
                       print('GAME TIE')
                       game_on = False
                   else:
                       play_turn = 'player1'
    if not replay():
        break
