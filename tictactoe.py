board = [' ' for x in range(10)]

def sattinbokstav(letter,pos):
    board[pos] = letter

def platsenarfri(pos):
    return board[pos] == ' '

def printabradde(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def braddearfullt(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def arvinnare(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def spelareflytta():
    run = True
    while run:
        move = input("Snälla välj en postion att placera x på inom 1 till 9\n")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if platsenarfri(move):
                    run = False
                    sattinbokstav('X' , move)
                else:
                    print('Förlåt denna platsen är tagen')
            else:
                print('Snälla skriv ett nummer mellan 1 till 9')

        except:
            print('Snälla skriv ett nummer')

def datorflytta():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if arvinnare(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = valjerandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = valjerandom(edgesOpen)
        return move

def valjerandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Välkommen till spelet")
    printabradde(board)

    while not(braddearfullt(board)):
        if not(arvinnare(board , 'O')):
            spelareflytta()
            printabradde(board)
        else:
            print("Du förlorade")
            break

        if not(arvinnare(board , 'X')):
            move = datorflytta()
            if move == 0:
                print(" ")
            else:
                sattinbokstav('O' , move)
                print('Datorn placerade ett o på postionen' , move , ':')
                printabradde(board)
        else:
            print("Du van")
            break




    if braddearfullt(board):
        print("Det blev lika")

while True:
    x = input("Vill du spela? klicka y för ja eller n för nej (y/n)\n")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
