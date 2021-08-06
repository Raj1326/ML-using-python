theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print ('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
def winner(board):
    if board['top-L'] == board['top-M'] and board['top-M'] ==  board['top-R'] and board['top-L'] != " ":
        return board['top-L']
    elif board['mid-L'] == board['mid-M'] and board['mid-M'] ==  board['mid-R'] and board['mid-L'] != " ":
        return board['mid-L']
    elif board['low-L'] == board['low-M'] and board['low-M'] == board['low-R'] and board['low-L'] != " ":
        return board['low-L']
    elif board['top-L'] == board['mid-L'] and board['mid-L'] == board['low-L'] and board['low-L'] != " ":
        return  board['low-L']
    elif board['top-M'] == board['mid-M'] and board['mid-M'] == board['low-M'] and board['low-M'] != " ": 
        return board['low-M'] 
    elif board['top-R'] == board['mid-R'] and board['mid-R'] == board['low-R'] and board['mid-R'] != " ":
        return board['mid-R']
    elif board['top-L'] == board['mid-M'] and board['mid-M'] == board['low-R'] and board['low-R'] != " ":
        return board['low-R']
    elif board['top-R'] ==board['mid-M'] and board['mid-M'] == board['low-L'] and board['low-L'] != " " :
        return board['low-L']
    else:
        return -1
def validate_move(board , move) :
    if board[move] == " ":
        return 1
    else :
        return 0

turn = 'X'
for i in range(9):
    result = winner(theBoard)
    if(result == -1):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        valid  = validate_move(theBoard , move)
        if(valid):

            theBoard[move] = turn

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        else:
            print('Invalid Move, try again ...')
            print('Turn for ' + turn + '. Move on which space?')
    else:
        print("winner " + result )
        break
printBoard(theBoard)
