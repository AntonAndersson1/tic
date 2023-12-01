bradde = [' ' for x in range(10)]

def sattinbokstav(bokstav,pos):
    bradde[pos] = bokstav

def platsenarfri(pos):
    return bradde[pos] == ' '

def printabradde(bradde):
    print('   |   |   ')
    print(' ' + bradde[1] + ' | ' + bradde[2] + ' | ' + bradde[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + bradde[4] + ' | ' + bradde[5] + ' | ' + bradde[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + bradde[7] + ' | ' + bradde[8] + ' | ' + bradde[9])
    print('   |   |   ')

def braddearfullt(bradde):
    if bradde.count(' ') > 1:
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
    starta = True
    while starta:
        flytta = input("Snalla valj en postion att placera x pa inom 1 till 9\n")
        try:
            flytta = int(flytta)
            if flytta > 0 and flytta < 10:
                if platsenarfri(flytta):
                    starta = False
                    sattinbokstav('X' , flytta)
                else:
                    print('Forlat denna platsen är tagen')
            else:
                print('Snalla skriv ett nummer mellan 1 till 9')

        except:
            print('Snalla skriv ett nummer')

def datorflytta():
    möjligflyttning = [x for x , bokstav in enumerate(bradde) if bokstav == ' ' and x != 0  ]
    flytta = 0

    for let in ['O' , 'X']:
        for i in möjligflyttning:
            braddekopia = bradde[:]
            braddekopia[i] = let
            if arvinnare(braddekopia, let):
                flytta = i
                return flytta

    hörnöppna = []
    for i in möjligflyttning:
        if i in [1 , 3 , 7 , 9]:
            hörnöppna.append(i)

    if len(hörnöppna) > 0:
        flytta = valjerandom(hörnöppna)
        return flytta

    if 5 in möjligflyttning:
        flytta = 5
        return flytta

    kanteröppna = []
    for i in möjligflyttning:
        if i in [2,4,6,8]:
            kanteröppna.append(i)

    if len(kanteröppna) > 0:
        flytta = valjerandom(kanteröppna)
        return flytta

def valjerandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Valkommen till spelet")
    printabradde(bradde)

    while not(braddearfullt(bradde)):
        if not(arvinnare(bradde , 'O')):
            spelareflytta()
            printabradde(bradde)
        else:
            print("Du forlorade")
            break

        if not(arvinnare(bradde , 'X')):
            flytta = datorflytta()
            if flytta == 0:
                print(" ")
            else:
                sattinbokstav('O' , flytta)
                print('Datorn placerade ett o pa postionen' , flytta , ':')
                printabradde(bradde)
        else:
            print("Du van")
            break




    if braddearfullt(bradde):
        print("Det blev lika")

while True:
    x = input("Vill du spela? klicka y for ja eller n for nej (y/n)\n")
    if x.lower() == 'y':
        bradde = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
