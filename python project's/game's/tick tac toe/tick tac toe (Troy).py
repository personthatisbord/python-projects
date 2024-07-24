Winner = '-'
while (True):
    tie = 'no'
    x_wins = 'no'
    o_wins = 'no'
    ghost_move_1 = 'no' 
    ghost_move_2 = 'no' 
    ghost_move_3 = 'no' 
    ghost_move_4 = 'no' 
    ghost_move_5 = 'no' 
    ghost_move_6 = 'no' 
    ghost_move_7 = 'no' 
    ghost_move_8 = 'no' 
    ghost_move_9 = 'no' 
    move_1 = '-'
    move_2 = '-'
    move_3 = '-'
    move_4 = '-'
    move_5 = '-'
    move_6 = '-'
    move_7 = '-'
    move_8 = '-'
    move_9 = '-'
    turn = 'x'
    x = 'yes'
    while (x == 'yes'):
        print (
        (f'''{move_1}    {move_2}    {move_3}

{move_4}    {move_5}    {move_6}

{move_7}    {move_8}    {move_9}
it is {turn}'s turn
    '''))
        move = input ('>')
        allow = 'yes'
        if turn == 'x':
            if move == '1':
                if ghost_move_1 == 'yes':
                    dead = input ('this spot is alredy taken')
                else:
                    move_1 = 'x'
                    turn = 'o'
                    allow = 'no'
                    ghost_move_1 = 'yes'
            elif move == '2':
                if ghost_move_2 == 'yes':
                    dead = input ('this spot is alredy taken')
                else:
                    move_2 = 'x'
                    turn = 'o'
                    allow = 'no'
                    ghost_move_2 = 'yes' 
            elif move == '3':
                if ghost_move_3 == 'yes':
                    dead = input ('this spot is alredy taken')
                else:
                    move_3 = 'x'
                    turn = 'o'
                    allow = 'no'
                    ghost_move_3 = 'yes' 
            elif move == '4':
                if ghost_move_4 == 'yes':
                    dead = input ('this spot is alredy taken')
                else:
                    move_4 = 'x'
                    turn = 'o'
                    allow = 'no'
                    ghost_move_4 = 'yes' 
            elif move == '5':
                if ghost_move_5 == 'yes':
                    dead = input ('this spot is alredy taken')
                else:
                    move_5 = 'x'
                    turn = 'o'
                    allow = 'no'
                    ghost_move_5 = 'yes' 
            elif move == '6':
                if ghost_move_6 == 'yes':
                    dead = input ('this spot is alredy taken')
                else:
                    move_6 = 'x'
                    turn = 'o'
                    allow = 'no'
                    ghost_move_6 = 'yes' 
            elif move == '7':
                if ghost_move_7 == 'yes':
                    dead = input ('this spot is alredy taken')
                else:
                    move_7 = 'x'
                    turn = 'o'
                    allow = 'no'
                    ghost_move_7 = 'yes' 
            elif move == '8':
                if ghost_move_8 == 'yes':
                    dead = input ('this spot is alredy taken')
                else:
                    move_8 = 'x'
                    turn = 'o'
                    allow = 'no'
                    ghost_move_8 = 'yes' 
            elif move == '9':
                if ghost_move_9 == 'yes':
                    dead = input ('this spot is alredy taken')
                else:
                    move_9 = 'x'
                    turn = 'o'
                    allow = 'no'
                    ghost_move_9 = 'yes'
            elif move == 'stop':
                    break
        if allow == 'yes':
            if turn == 'o':
                if move == '1':
                    if ghost_move_1 == 'yes':
                        dead = input ('this spot is alredy taken')
                    else:
                        move_1 = 'o'
                        turn = 'x'
                        ghost_move_1 = 'yes' 
                elif move == '2':
                    if ghost_move_2 == 'yes':
                        dead = input ('this spot is alredy taken')
                    else:
                        move_2 = 'o'
                        turn = 'x'
                        ghost_move_2 = 'yes' 
                elif move == '3':
                    if ghost_move_3 == 'yes':
                        dead = input ('this spot is alredy taken')
                    else:
                        move_3 = 'o'
                        turn = 'x'
                        ghost_move_3 = 'yes' 
                elif move == '4':
                    if ghost_move_4 == 'yes':
                        dead = input ('this spot is alredy taken')
                    else:
                        move_4 = 'o'
                        turn = 'x'
                        ghost_move_4 = 'yes' 
                elif move == '5':
                    if ghost_move_5 == 'yes':
                        dead = input ('this spot is alredy taken')
                    else:
                        move_5 = 'o'
                        turn = 'x'
                        ghost_move_5 = 'yes' 
                elif move == '6':
                    if ghost_move_6 == 'yes':
                        dead = input ('this spot is alredy taken')
                    else:
                        move_6 = 'o'
                        turn = 'x'
                        ghost_move_6 = 'yes' 
                elif move == '7':
                    if ghost_move_7 == 'yes':
                        dead = input ('this spot is alredy taken')
                    else:
                        move_7 = 'o'
                        turn = 'x'
                        ghost_move_7 = 'yes' 
                elif move == '8':
                    if ghost_move_8 == 'yes':
                        dead = input ('this spot is alredy taken')
                    else:
                        move_8 = 'o'
                        turn = 'x'
                        ghost_move_8 = 'yes' 
                elif move == '9':
                    if ghost_move_9 == 'yes':
                        dead = input ('this spot is alredy taken')
                    else:
                        move_9 = 'o'
                        turn = 'x'
                        ghost_move_9 = 'yes'
                elif move == 'stop':
                    break
        if move_1 != '-' and move_1 == move_2 and move_1 == move_3:
                    RunGame = 'no'
                    Winner = move_1
        if move_1 != '-' and move_1 == move_4 and move_1 == move_7:
                    RunGame = 'no'
                    Winner = move_1
        if move_1 != '-' and move_1 == move_5 and move_1 == move_9:
                    RunGame = 'no'
                    Winner = move_1
        if move_2 != '-' and move_2 == move_5 and move_2 == move_8:
                    RunGame = 'no'
                    Winner = move_2
        if move_3 != '-' and move_3 == move_6 and move_3 == move_9:
                    RunGame = 'no'
                    Winner = move_3
        if move_3 != '-' and move_3 == move_5 and move_3 == move_7:
                    RunGame = 'no'
                    Winner = move_3
        if move_4 != '-' and move_4 == move_5 and move_4 == move_6:
                    RunGame = 'no'
                    Winner = move_4
        if move_7 != '-' and move_7 == move_8 and move_7 == move_9:
                    RunGame = 'no'
                    Winner = move_7
        if ghost_move_1 == 'yes':
            if ghost_move_2 == 'yes':
                if ghost_move_3 == 'yes':
                    if ghost_move_4 == 'yes':
                        if ghost_move_5 == 'yes':
                            if ghost_move_6 == 'yes':
                                if ghost_move_7 == 'yes':
                                    if ghost_move_8 == 'yes':
                                        if ghost_move_9 == 'yes':
                                            x = 'no'
                                            tie = 'yes'
                                                
        if x == 'no':
            print (
        (f'''{move_1}    {move_2}    {move_3}

{move_4}    {move_5}    {move_6}

{move_7}    {move_8}    {move_9}'''))
        if tie == 'yes':
            if Winner != True:
                    print ('The game ended in a draw!')
                    break
        if Winner == '0' or Winner == 'x':
            print (f'''{Winner} win's''')
            break
    break
