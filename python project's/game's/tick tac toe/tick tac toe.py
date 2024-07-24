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
        while (True):
            if move_1 == 'o':
                if move_2 == 'o':
                    if move_3 == 'o':
                        x = 'no'
                        o_wins = 'yes'
            if move_1 == 'o':
                if move_4 == 'o':
                    if move_7 == 'o':
                        x = 'no'
                        o_wins = 'yes'
            if move_1 == 'o':
                if move_5 == 'o':
                    if move_9 == 'o':
                        x = 'no'
                        o_wins = 'yes'
            if move_2 == 'o':
                if move_5 == 'o':
                    if move_8 == 'o':
                        x = 'no'
                        o_wins = 'yes'
            if move_3 == 'o':
                if move_6 == 'o':
                    if move_9 == 'o':
                        x = 'no'
                        o_wins = 'yes'
            if move_3 == 'o':
                if move_5 == 'o':
                    if move_7 == 'o':
                        x = 'no'
                        o_wins = 'yes'
            if move_4 == 'o':
                if move_5 == 'o':
                    if move_6 == 'o':
                        x = 'no'
                        o_wins = 'yes'
            if move_7 == 'o':
                if move_8 == 'o':
                    if move_9 == 'o':
                        x = 'no'
                        o_wins = 'yes'
            if move_1 == 'x':
                if move_2 == 'x':
                    if move_3 == 'x':
                        x = 'no'
                        x_wins = 'yes'
            if move_1 == 'x':
                if move_4 == 'x':
                    if move_7 == 'x':
                        x = 'no'
                        x_wins = 'yes'
            if move_1 == 'x':
                if move_5 == 'x':
                    if move_9 == 'x':
                        x = 'no'
                        x_wins = 'yes'
            if move_2 == 'x':
                if move_5 == 'x':
                    if move_8 == 'x':
                        x = 'no'
                        x_wins = 'yes'
            if move_3 == 'x':
                if move_6 == 'x':
                    if move_9 == 'x':
                        x = 'no'
                        x_wins = 'yes'
            if move_3 == 'x':
                if move_5 == 'x':
                    if move_7 == 'x':
                        x = 'no'
                        x_wins = 'yes'
            if move_4 == 'x':
                if move_5 == 'x':
                    if move_6 == 'x':
                        x = 'no'
                        x_wins = 'yes'
            if move_7 == 'x':
                if move_8 == 'x':
                    if move_9 == 'x':
                        x_wins = 'yes'
                        x = 'no'
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
                    if x_wins == 'no':
                        if o_wins == 'no':
                            print ('The game ended in a draw!')
                            break
                if x_wins == 'yes':
                    print ('x wins!')
                    break
                if o_wins == 'yes':
                    print ('o wins!')
                    break
            break
    break