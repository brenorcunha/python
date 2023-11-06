import random

def player_input():
    global players, marker, position, board
    name = input('Type player name: ')
    marker = input('Type your simbol (X/O):').upper()
    position = int(input('Type the position you want to play:'))
    players[name]=marker
    space_check(board, position)
    print('Players dict: ', players)

def display_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def place_marker(board, marker, position):
    board[position] = marker
    
def win_check(board, marker):
    if(board[1]==marker and board[2]==marker and board[3]==marker or
    board[4]==marker and board[5]==marker and board[6]==marker or
    board[7]==marker and board[8]==marker and board[9]==marker or
    board[1]==marker and board[4]==marker and board[4]==marker or
    board[2]==marker and board[5]==marker and board[8]==marker or
    board[3]==marker and board[6]==marker and board[9]==marker or
    board[1]==marker and board[5]==marker and board[9]==marker or
    board[3]==marker and board[5]==marker and board[7]==marker):
        print('Player ' + marker + ' won!')
        replay()
    else:
        print('Nobody won! Velha...')
        replay()

def choose_first():
    if random.randint(0,2)==0:
        return print('The first player is going to be player 1')
    else:
        return print('The first player is going to be player 2')

def space_check(board, position):
    if (board[position]=='X' or board[position]=='O'):
        return print('Position busy, choose another.')
    else:
        place_marker(board, marker, position)

def full_board_check(board):
    if(board[1]!='1' and board[2]!='2' and board[3]!='3' and
    board[4]!='4' and board[5]!='5' and board[6]!='6' and
    board[7]!='7' and board[8]!='8' and board[9]!='9'):
        win_check(board, marker)
        return True
    else:
        return False
        
def replay():
    global board, playing
    answ = input('Do you want to play again? (y/n)')
    if answ.lower()=='y':
        return True
        board=['','1','2','3','4','5','6','7','8','9']
        display_board(board)
    else:
        playing=False
        return False
""" Check if it resets the board and checks for winner in every appliable situation """
while True:
    board=['','1','2','3','4','5','6','7','8','9']
    players={}
    marker = ''
    position=0
    playing=True
    player_input()
    player_input()
    choose_first()
    display_board(board)
    while playing:
        marker = input('Type your simbol (X/O):').upper()
        position = int(input('Type the position you want to play:'))
        space_check(board, position)
        full_board_check(board)
        display_board(board)
    if not replay():
        break