import time
import pygame
pygame.init()

color = (0,0,0)
rect_color = (255,0,0)
rect_color_1 = (0,0,0)
rect_color_2 = (50,225,0)
    # CREATING CANVAS
exit = False
snake_lanth = 0
score = 0
ave_list = [0, 0, 0, 0, 0]
NUMBER = (-1)
best = 0
while (True):
    import time
    if snake_lanth > score:
        score = snake_lanth
    ave_list.insert(0, snake_lanth)
    ave_list.pop()
    ave_1 = ave_list[0]
    ave_2 = ave_list[1]
    ave_3 = ave_list[2]
    ave_4 = ave_list[3]
    ave_5 = ave_list[4]
    ave = ave_1 + ave_2 + ave_3 + ave_4 + ave_5
    ave = ave / 5
    NUMBER = NUMBER + 1
    if ave > best:
        best = ave
    blank = (0, 0, 0)
    snake = (50, 125, 0)
    head = '52'
    add = 1
    snake_lanth = 1
    apple = (225, 0, 0)
    snake_tails = (50, 225, 0)
    
    tail_1 = blank 
    tail_2 = blank 
    tail_3 = blank 
    tail_4 = blank 
    tail_5 = blank                                    
    tail_6 = blank
    tail_7 = blank 
    tail_8 = blank 
    tail_9 = blank 
    tail_10 = blank 
    tail_11 = blank 
    tail_12 = blank 
    tail_13 = blank 
    tail_14 = blank 
    tail_15 = blank 
    tail_16 = blank 
    tail_17 = blank 
    tail_18 = blank 
    tail_19 = blank 
    tail_20 = blank 
    tail_21 = blank 
    tail_22 = blank 
    tail_23 = blank 
    tail_24 = blank 
    tail_25 = blank 
    tail_26 = blank 
    tail_27 = blank 
    tail_28 = blank 
    tail_29 = blank 
    tail_30 = blank 
    tail_31 = blank 
    tail_32 = blank 
    tail_33 = blank 
    tail_34 = blank 
    tail_35 = blank 
    tail_36 = blank 
    tail_37 = blank 
    tail_38 = blank 
    tail_39 = blank 
    tail_40 = blank 
    tail_41 = blank 
    tail_42 = blank 
    tail_43 = blank 
    tail_44 = blank 
    tail_45 = blank 
    tail_46 = blank 
    tail_47 = blank 
    tail_48 = blank 
    tail_49 = blank 
    tail_50 = blank 
    tail_51 = blank 
    tail_52 = blank 
    tail_53 = blank 
    tail_54 = blank 
    tail_55 = blank 
    tail_56 = blank 
    tail_57 = blank 
    tail_58 = blank 
    tail_59 = blank 
    tail_60 = blank 
    tail_61 = blank 
    tail_62 = blank 
    tail_63 = blank 
    tail_64 = blank 
    tail_65 = blank 
    tail_66 = blank 
    tail_67 = blank 
    tail_68 = blank 
    tail_69 = blank 
    tail_70 = blank 
    tail_71 = blank 
    tail_72 = blank 
    tail_73 = blank 
    tail_74 = blank 
    tail_75 = blank 
    tail_76 = blank 
    tail_77 = blank 
    tail_78 = blank 
    tail_79 = blank 
    tail_80 = blank 
    tail_81 = blank 
    tail_82 = blank 
    tail_83 = blank 
    tail_84 = blank 
    tail_85 = blank 
    tail_86 = blank 
    tail_87 = blank 
    tail_88 = blank 
    tail_89 = blank 
    tail_90 = blank 
    tail_91 = blank 
    tail_92 = blank 
    tail_93 = blank 
    tail_94 = blank 
    tail_95 = blank 
    tail_96 = blank 
    tail_97 = blank 
    tail_98 = blank 
    tail_99 = blank
    tail_100 = blank
    end = 'end'
    print ('--------------------------------------------------------------------------------')
    print ('1  2  3  4  5  6  7  8  9  10')
    print ('11 12 13 14 15 16 17 18 19 20')
    print ('21 22 23 24 25 26 27 28 29 30')
    print ('31 32 33 34 35 36 37 38 39 40')
    print ('41 42 43 44 45 46 47 48 49 50')
    print ('51 52 53 54 55 56 57 58 59 60')
    print ('61 62 63 64 65 66 67 68 69 70')
    print ('71 72 73 74 75 76 77 78 79 80')
    print ('81 82 83 84 85 86 87 88 89 90')
    print ('91 92 93 94 95 96 97 98 99 100')
    number_of_tails = input ('tails ')
    test = 'start'
    add = 1
    number_of_tails = int(number_of_tails)
    while (test == 'start'):
                        for tail in (tail_1, tail_2, tail_3, tail_4, tail_5, tail_6, tail_7, tail_8, tail_9, tail_10, tail_11, tail_12, tail_13, tail_14, tail_15, tail_16, tail_17, tail_18, tail_19, tail_20, tail_21, tail_22, tail_23, tail_24, tail_25, tail_26, tail_27, tail_28, tail_29, tail_30, tail_31, tail_32, tail_33, tail_34, tail_35, tail_36, tail_37, tail_38, tail_39, tail_40, tail_41, tail_42,tail_43,tail_44,tail_45, tail_46, tail_47, tail_48, tail_49, tail_50, tail_51, tail_52, tail_53, tail_54, tail_55, tail_56, tail_57, tail_58, tail_59, tail_60, tail_61, tail_62, tail_63, tail_64, tail_65, tail_66, tail_67, tail_68, tail_69, tail_70, tail_71, tail_72, tail_73, tail_74, tail_75, tail_76, tail_77, tail_78, tail_79, tail_80, tail_81, tail_82, tail_83, tail_84, tail_85, tail_86, tail_87, tail_88, tail_89, tail_90, tail_91, tail_92, tail_93, tail_94, tail_95, tail_96, tail_97, tail_98, tail_99, tail_100, end):
                            if add <= number_of_tails:
                                snake_tail = input (f'{add} ')
                                if add == 1:
                                    tail_1 = snake_tail
                                if add == 2:
                                    tail_2 = snake_tail
                                if add == 3:
                                    tail_3 = snake_tail
                                if add == 4:
                                    tail_4 = snake_tail
                                if add == 5:
                                    tail_5 = snake_tail
                                if add == 6:
                                    tail_6 = snake_tail
                                if add == 7:
                                    tail_7 = snake_tail
                                if add == 8:
                                    tail_8 = snake_tail
                                if add == 9:
                                    tail_9 = snake_tail
                                if add == 10:
                                    tail_10 = snake_tail
                                if add == 11:
                                    tail_11 = snake_tail
                                if add == 12:
                                    tail_12 = snake_tail
                                if add == 13:
                                    tail_13 = snake_tail
                                if add == 14:
                                    tail_14 = snake_tail
                                if add == 15:
                                    tail_15 = snake_tail
                                if add == 16:
                                    tail_16 = snake_tail
                                if add == 17:
                                    tail_17 = snake_tail
                                if add == 18:
                                    tail_18 = snake_tail
                                if add == 19:
                                    tail_19 = snake_tail
                                if add == 20:
                                    tail_20 = snake_tail
                                if add == 21:
                                    tail_21 = snake_tail
                                if add == 22:
                                    tail_22 = snake_tail
                                if add == 23:
                                    tail_23 = snake_tail
                                if add == 24:
                                    tail_24 = snake_tail
                                if add == 25:
                                    tail_25 = snake_tail
                                if add == 26:
                                    tail_26 = snake_tail
                                if add == 27:
                                    tail_27 = snake_tail
                                if add == 28:
                                    tail_28 = snake_tail
                                if add == 29:
                                    tail_29 = snake_tail
                                if add == 30:
                                    tail_30 = snake_tail
                                if add == 31:
                                    tail_31 = snake_tail
                                if add == 32:
                                    tail_32 = snake_tail
                                if add == 33:
                                    tail_33 = snake_tail
                                if add == 34:
                                    tail_34 = snake_tail
                                if add == 35:
                                    tail_35 = snake_tail
                                if add == 36:
                                    tail_36 = snake_tail
                                if add == 37:
                                    tail_37 = snake_tail
                                if add == 38:
                                    tail_38 = snake_tail
                                if add == 39:
                                    tail_39 = snake_tail
                                if add == 40:
                                    tail_40 = snake_tail
                                if add == 41:
                                    tail_41 = snake_tail
                                if add == 42:
                                    tail_42 = snake_tail
                                if add == 43:
                                    tail_43 = snake_tail
                                if add == 44:
                                    tail_44 = snake_tail
                                if add == 45:
                                    tail_45 = snake_tail
                                if add == 46:
                                    tail_46 = snake_tail
                                if add == 47:
                                    tail_47 = snake_tail
                                if add == 48:
                                    tail_48 = snake_tail
                                if add == 49:
                                    tail_49 = snake_tail
                                if add == 50:
                                    tail_50 = snake_tail
                                if add == 51:
                                    tail_51 = snake_tail
                                if add == 52:
                                    tail_52 = snake_tail
                                if add == 53:
                                    tail_53 = snake_tail
                                if add == 54:
                                    tail_54 = snake_tail
                                if add == 55:
                                    tail_55 = snake_tail
                                if add == 56:
                                    tail_56 = snake_tail
                                if add == 57:
                                    tail_57 = snake_tail
                                if add == 58:
                                    tail_58 = snake_tail
                                if add == 59:
                                    tail_59 = snake_tail
                                if add == 60:
                                    tail_60 = snake_tail
                                if add == 61:
                                    tail_61 = snake_tail
                                if add == 62:
                                    tail_62 = snake_tail
                                if add == 63:
                                    tail_63 = snake_tail
                                if add == 64:
                                    tail_64 = snake_tail
                                if add == 65:
                                    tail_65 = snake_tail
                                if add == 66:
                                    tail_66 = snake_tail
                                if add == 67:
                                    tail_67 = snake_tail
                                if add == 68:
                                    tail_68 = snake_tail
                                if add == 69:
                                    tail_69 = snake_tail
                                if add == 70:
                                    tail_70 = snake_tail
                                if add == 71:
                                    tail_71 = snake_tail
                                if add == 72:
                                    tail_72 = snake_tail
                                if add == 73:
                                    tail_73 = snake_tail
                                if add == 74:
                                    tail_74 = snake_tail
                                if add == 75:
                                    tail_75 = snake_tail
                                if add == 76:
                                    tail_76 = snake_tail
                                if add == 77:
                                    tail_77 = snake_tail
                                if add == 78:
                                    tail_78 = snake_tail
                                if add == 79:
                                    tail_79 = snake_tail
                                if add == 80:
                                    tail_80 = snake_tail
                                if add == 81:
                                    tail_81 = snake_tail
                                if add == 82:
                                    tail_82 = snake_tail
                                if add == 83:
                                    tail_83 = snake_tail
                                if add == 84:
                                    tail_84 = snake_tail
                                if add == 85:
                                    tail_85 = snake_tail
                                if add == 86:
                                    tail_86 = snake_tail
                                if add == 87:
                                    tail_87 = snake_tail
                                if add == 88:
                                    tail_88 = snake_tail
                                if add == 89:
                                    tail_89 = snake_tail
                                if add == 90:
                                    tail_90 = snake_tail
                                if add == 91:
                                    tail_91 = snake_tail
                                if add == 92:
                                    tail_92 = snake_tail
                                if add == 93:
                                    tail_93 = snake_tail
                                if add == 94:
                                    tail_94 = snake_tail
                                if add == 95:
                                    tail_95 = snake_tail
                                if add == 96:
                                    tail_96 = snake_tail
                                if add == 97:
                                    tail_97 = snake_tail
                                if add == 98:
                                    tail_98 = snake_tail
                                if add == 99:
                                    tail_99 = snake_tail
                                if add == 100:
                                    tail_100 = snake_tail
                            if tail == end:
                                test = 'stop'
                            add = (add) + 1
    head = input ('head')
    apple_move = input ('apple')
    moving = 'no'
    death_ok = 'no'
    add = 1
    snake_lanth = number_of_tails
    import random
    movement = 'right'
    x = 'yes'
    y = 'yes'
    canvas = pygame.display.set_mode((500, 500))
  
    # TITLE OF CANVAS
    pygame.display.set_caption("My Board")
    while (x == 'yes'):
        if moving == 'yes':
            tail_100 = tail_99
            tail_99 = tail_98
            tail_98 = tail_97
            tail_97 = tail_96
            tail_96 = tail_95
            tail_95 = tail_94
            tail_94 = tail_93
            tail_93 = tail_92
            tail_92 = tail_91
            tail_91 = tail_90
            tail_90 = tail_89
            tail_89 = tail_88
            tail_88 = tail_87
            tail_87 = tail_86
            tail_86 = tail_85
            tail_85 = tail_84
            tail_83 = tail_82
            tail_84 = tail_83
            tail_82 = tail_81
            tail_81 = tail_80
            tail_80 = tail_79
            tail_79 = tail_78
            tail_78 = tail_77
            tail_78 = tail_77
            tail_77 = tail_76
            tail_76 = tail_75
            tail_75 = tail_74
            tail_74 = tail_73
            tail_73 = tail_72
            tail_72 = tail_71
            tail_71 = tail_70
            tail_70 = tail_69
            tail_69 = tail_68
            tail_68 = tail_67
            tail_67 = tail_66
            tail_66 = tail_65
            tail_65 = tail_64
            tail_64 = tail_63
            tail_63 = tail_62
            tail_62 = tail_61
            tail_61 = tail_60
            tail_60 = tail_59
            tail_59 = tail_58
            tail_58 = tail_57
            tail_57 = tail_56
            tail_56 = tail_55
            tail_55 = tail_54
            tail_54 = tail_53
            tail_53 = tail_52
            tail_52 = tail_51
            tail_51 = tail_50
            tail_50 = tail_49
            tail_49 = tail_48
            tail_48 = tail_47
            tail_47 = tail_46
            tail_46 = tail_45
            tail_45 = tail_44
            tail_44 = tail_43
            tail_43 = tail_42
            tail_42 = tail_41
            tail_41 = tail_40
            tail_40 = tail_39
            tail_39 = tail_38
            tail_38 = tail_37
            tail_37 = tail_36
            tail_36 = tail_35
            tail_35 = tail_34
            tail_34 = tail_33
            tail_33 = tail_32
            tail_32 = tail_31
            tail_31 = tail_30
            tail_30 = tail_29
            tail_29 = tail_28
            tail_28 = tail_27
            tail_27 = tail_26
            tail_26 = tail_25
            tail_25 = tail_24
            tail_24 = tail_23
            tail_23 = tail_22
            tail_22 = tail_21
            tail_21 = tail_20
            tail_20 = tail_19
            tail_19 = tail_18
            tail_18 = tail_17
            tail_17 = tail_16
            tail_16 = tail_15
            tail_15 = tail_14
            tail_14 = tail_13
            tail_13 = tail_12
            tail_12 = tail_11
            tail_11 = tail_10
            tail_10 = tail_9
            tail_9 = tail_8
            tail_8 = tail_7
            tail_7 = tail_6
            tail_6 = tail_5
            tail_5 = tail_4
            tail_4 = tail_3
            tail_3 = tail_2
            tail_2 = tail_1
            tail_1 = head
        spot_1 = blank 
        spot_2 = blank 
        spot_3 = blank 
        spot_4 = blank 
        spot_5 = blank 
        spot_6 = blank 
        spot_7 = blank 
        spot_8 = blank 
        spot_9 = blank 
        spot_10 = blank 
        spot_11 = blank 
        spot_12 = blank 
        spot_13 = blank 
        spot_14 = blank 
        spot_15 = blank 
        spot_16 = blank 
        spot_17 = blank 
        spot_18 = blank 
        spot_19 = blank 
        spot_20 = blank 
        spot_21 = blank 
        spot_22 = blank 
        spot_23 = blank 
        spot_24 = blank 
        spot_25 = blank 
        spot_26 = blank 
        spot_27 = blank 
        spot_28 = blank 
        spot_29 = blank 
        spot_30 = blank 
        spot_31 = blank 
        spot_32 = blank 
        spot_33 = blank 
        spot_34 = blank 
        spot_35 = blank 
        spot_36 = blank 
        spot_37 = blank 
        spot_38 = blank 
        spot_39 = blank 
        spot_40 = blank 
        spot_41 = blank 
        spot_42 = blank 
        spot_43 = blank 
        spot_44 = blank 
        spot_45 = blank 
        spot_46 = blank 
        spot_47 = blank 
        spot_48 = blank 
        spot_49 = blank 
        spot_50 = blank 
        spot_51 = blank 
        spot_52 = blank 
        spot_53 = blank 
        spot_54 = blank 
        spot_55 = blank 
        spot_56 = blank 
        spot_57 = blank 
        spot_58 = blank 
        spot_59 = blank 
        spot_60 = blank 
        spot_61 = blank 
        spot_62 = blank 
        spot_63 = blank 
        spot_64 = blank 
        spot_65 = blank 
        spot_66 = blank 
        spot_67 = blank 
        spot_68 = blank 
        spot_69 = blank 
        spot_70 = blank 
        spot_71 = blank 
        spot_72 = blank 
        spot_73 = blank 
        spot_74 = blank 
        spot_75 = blank 
        spot_76 = blank 
        spot_77 = blank 
        spot_78 = blank 
        spot_79 = blank 
        spot_80 = blank 
        spot_81 = blank 
        spot_82 = blank 
        spot_83 = blank 
        spot_84 = blank 
        spot_85 = blank 
        spot_86 = blank 
        spot_87 = blank 
        spot_88 = blank 
        spot_89 = blank 
        spot_90 = blank 
        spot_91 = blank 
        spot_92 = blank 
        spot_93 = blank 
        spot_94 = blank 
        spot_95 = blank 
        spot_96 = blank 
        spot_97 = blank 
        spot_98 = blank 
        spot_99 = blank
        spot_100 = blank
        w = 'yes'
        if movement == 'left':
            if head == '1':
                w = 'no'
            if head == '11':
                w = 'no'
            if head == '21':
                w = 'no'
            if head == '31':
                w = 'no'
            if head == '41':
                w = 'no'
            if head == '51':
                w = 'no'
            if head == '61':
                w = 'no'
            if head == '71':
                w = 'no'
            if head == '81':
                w = 'no'
            if head == '91':
                w = 'no'
            if w == 'no':
                nuber = int(head) + 9
                head = str(nuber)
        if movement == 'right':
            if head == '10':
                w = 'no'
            if head == '20':
                w = 'no'
            if head == '30':
                w = 'no'
            if head == '40':
                w = 'no'
            if head == '50':
                w = 'no'
            if head == '60':
                w = 'no'
            if head == '70':
                w = 'no'
            if head == '80':
                w = 'no'
            if head == '90':
                w = 'no'
            if head == '100':
                w = 'no'
            if w == 'no':
                nuber = int(head) - 9
                head = str(nuber)
        if w == 'yes' and moving == 'yes':
            if movement == 'left':
                nuber = int(head) - 1
                head = str(nuber)
            if movement == 'right':
                nuber = int(head) + 1
                head = str(nuber)
            if movement == 'up':
                nuber = int(head) - 10
                head = str(nuber)
            if movement == 'down':
                nuber = int(head) + 10
                head = str(nuber)
        if head == '101':
            head = '1'
        if head == '102':
            head = '2'
        if head == '103':
            head = '3'
        if head == '104':
            head = '4'
        if head == '105':
            head = '5'
        if head == '106':
            head = '6'
        if head == '107':
            head = '7'
        if head == '108':
            head = '8'
        if head == '109':
            head = '9'
        if head == '110':
            head = '10'
        if head == '-1':
            head = '99'
        if head == '-2':
            head = '98'
        if head == '-3':
            head = '97'
        if head == '-4':
            head = '96'
        if head == '-5':
            head = '95'
        if head == '-6':
            head = '94'
        if head == '-7':
            head = '93'
        if head == '-8':
            head = '92'
        if head == '-9':
            head = '91'
        if head == '0':
            head = '100'
        ghost_right = '91'
        ghost_left = '100'
        ghost_up = int(head) - 10
        ghost_down = int(head) + 10
        ghost_right = int(head) + 1    
        ghost_left = int(head) - 1
        ghost_top_left = int(ghost_left) - 10
        ghost_top_right = int(ghost_right) - 10
        ghost_top_up = int(ghost_up) - 10
        ghost_left_left = int(ghost_left) - 1
        ghost_right_right = int(ghost_right) +1
        ghost_down_right = int(ghost_right) + 10
        ghost_down_left = int(ghost_left) + 10
        ghost_down_down = int(ghost_down) + 10
        ghost_top_left = str(ghost_top_left)
        ghost_top_right = str(ghost_top_right)
        ghost_top_up = str(ghost_top_up)
        ghost_left_left = str(ghost_left_left)
        ghost_right_right = str(ghost_right_right)
        ghost_down_left  = str(ghost_down_left)
        ghost_down_right = str(ghost_down_right)
        ghost_down_down = str(ghost_down_down)
        ghost_up = str(ghost_up)
        ghost_down = str(ghost_down)
        ghost_right = str(ghost_right)
        ghost_left = str(ghost_left)
        tail_end = 'no'
        for tail in (tail_1, tail_2, tail_3, tail_4, tail_5, tail_6, tail_7, tail_8, tail_9, tail_10, tail_11, tail_12, tail_13, tail_14, tail_15, tail_16, tail_17, tail_18, tail_19, tail_20, tail_21, tail_22, tail_23, tail_24, tail_25, tail_26, tail_27, tail_28, tail_29, tail_30, tail_31, tail_32, tail_33, tail_34, tail_35, tail_36, tail_37, tail_38, tail_39, tail_40, tail_41, tail_42,tail_43,tail_44,tail_45, tail_46, tail_47, tail_48, tail_49, tail_50, tail_51, tail_52, tail_53, tail_54, tail_55, tail_56, tail_57, tail_58, tail_59, tail_60, tail_61, tail_62, tail_63, tail_64, tail_65, tail_66, tail_67, tail_68, tail_69, tail_70, tail_71, tail_72, tail_73, tail_74, tail_75, tail_76, tail_77, tail_78, tail_79, tail_80, tail_81, tail_82, tail_83, tail_84, tail_85, tail_86, tail_87, tail_88, tail_89, tail_90, tail_91, tail_92, tail_93, tail_94, tail_95, tail_96, tail_97, tail_98, tail_99, tail_100):
            if add <= snake_lanth:
                if tail == '1':
                    spot_1 = snake_tails
                if tail == '2':
                    spot_2 = snake_tails
                if tail == '3':
                    spot_3 = snake_tails
                if tail == '4':
                    spot_4 = snake_tails 
                if tail == '5':
                    spot_5 = snake_tails 
                if tail == '6':
                    spot_6 = snake_tails 
                if tail == '7':
                    spot_7 = snake_tails 
                if tail == '8':
                    spot_8 = snake_tails 
                if tail == '9':
                    spot_9 = snake_tails 
                if tail == '10':
                    spot_10 = snake_tails 
                if tail == '11':
                    spot_11 = snake_tails 
                if tail == '12':
                    spot_12 = snake_tails 
                if tail == '13':
                    spot_13 = snake_tails 
                if tail == '14':
                    spot_14 = snake_tails 
                if tail == '15':
                    spot_15 = snake_tails 
                if tail == '16':
                    spot_16 = snake_tails 
                if tail == '17':
                    spot_17 = snake_tails 
                if tail == '18':
                    spot_18 = snake_tails 
                if tail == '19':
                    spot_19 = snake_tails 
                if tail == '20':
                    spot_20 = snake_tails 
                if tail == '21':
                    spot_21 = snake_tails 
                if tail == '22':
                    spot_22 = snake_tails 
                if tail == '23':
                    spot_23 = snake_tails 
                if tail == '24':
                    spot_24 = snake_tails 
                if tail == '25':
                    spot_25 = snake_tails 
                if tail == '26':
                    spot_26 = snake_tails 
                if tail == '27':
                    spot_27 = snake_tails 
                if tail == '28':
                    spot_28 = snake_tails 
                if tail == '29':
                    spot_29 = snake_tails 
                if tail == '30':
                    spot_30 = snake_tails 
                if tail == '31':
                    spot_31 = snake_tails 
                if tail == '32':
                    spot_32 = snake_tails 
                if tail == '33':
                    spot_33 = snake_tails 
                if tail == '34':
                    spot_34 = snake_tails 
                if tail == '35':
                    spot_35 = snake_tails 
                if tail == '36':
                    spot_36 = snake_tails 
                if tail == '37':
                    spot_37 = snake_tails 
                if tail == '38':
                    spot_38 = snake_tails 
                if tail == '39':
                    spot_39 = snake_tails 
                if tail == '40':
                    spot_40 = snake_tails 
                if tail == '41':
                    spot_41 = snake_tails
                if tail == '42':
                    spot_42 = snake_tails 
                if tail == '43':
                    spot_43 = snake_tails 
                if tail == '44':
                    spot_44 = snake_tails 
                if tail == '45':
                    spot_45 = snake_tails 
                if tail == '46':
                    spot_46 = snake_tails 
                if tail == '47':
                    spot_47 = snake_tails 
                if tail == '48':
                    spot_48 = snake_tails 
                if tail == '49':
                    spot_49 = snake_tails 
                if tail == '50':
                    spot_50 = snake_tails 
                if tail == '51':
                    spot_51 = snake_tails 
                if tail == '52':
                    spot_52 = snake_tails 
                if tail == '53':
                    spot_53 = snake_tails 
                if tail == '54':
                    spot_54 = snake_tails 
                if tail == '55':
                    spot_55 = snake_tails 
                if tail == '56':
                    spot_56 = snake_tails 
                if tail == '57':
                    spot_57 = snake_tails 
                if tail == '58':
                    spot_58 = snake_tails 
                if tail == '59':
                    spot_59 = snake_tails 
                if tail == '60':
                    spot_60 = snake_tails 
                if tail == '61':
                    spot_61 = snake_tails 
                if tail == '62':
                    spot_62 = snake_tails 
                if tail == '63':
                    spot_63 = snake_tails 
                if tail == '64':
                    spot_64 = snake_tails 
                if tail == '65':
                    spot_65 = snake_tails 
                if tail == '66':
                    spot_66 = snake_tails 
                if tail == '67':
                    spot_67 = snake_tails 
                if tail == '68':
                    spot_68 = snake_tails 
                if tail == '69':
                    spot_69 = snake_tails 
                if tail == '70':
                    spot_70 = snake_tails 
                if tail == '71':
                    spot_71 = snake_tails 
                if tail == '72':
                    spot_72 = snake_tails 
                if tail == '73':
                    spot_73 = snake_tails 
                if tail == '74':
                    spot_74 = snake_tails 
                if tail == '75':
                    spot_75 = snake_tails 
                if tail == '76':
                    spot_76 = snake_tails 
                if tail == '77':
                    spot_77 = snake_tails 
                if tail == '78':
                    spot_78 = snake_tails 
                if tail == '79':
                    spot_79 = snake_tails 
                if tail == '80':
                    spot_80 = snake_tails 
                if tail == '81':
                    spot_81 = snake_tails 
                if tail == '82':
                    spot_82 = snake_tails 
                if tail == '83':
                    spot_83 = snake_tails 
                if tail == '84':
                    spot_84 = snake_tails 
                if tail == '85':
                    spot_85 = snake_tails 
                if tail == '86':
                    spot_86 = snake_tails 
                if tail == '87':
                    spot_87 = snake_tails 
                if tail == '88':
                    spot_88 = snake_tails 
                if tail == '89':
                    spot_89 = snake_tails 
                if tail == '90':
                    spot_90 = snake_tails 
                if tail == '91':
                    spot_91 = snake_tails 
                if tail == '92':
                    spot_92 = snake_tails 
                if tail == '93':
                    spot_93 = snake_tails 
                if tail == '94':
                    spot_94 = snake_tails 
                if tail == '95':
                    spot_95 = snake_tails 
                if tail == '96':
                    spot_96 = snake_tails 
                if tail == '97':
                    spot_97 = snake_tails 
                if tail == '98':
                    spot_98 = snake_tails 
                if tail == '99':
                    spot_99 = snake_tails
                if tail == '100':
                    spot_100 = snake_tails
                if add == snake_lanth:
                    tail_end = 'yes'
                if tail_end == 'no':
                    if ghost_up == tail:
                        ghost_up = '100000'
                    if ghost_down == tail:
                        ghost_down = '100000'
                    if ghost_right == tail:
                        ghost_right = '100000'
                    if ghost_left == tail:
                        ghost_left = '100000'
                    if ghost_top_up == tail:
                        ghost_top_up = '400'
                    if ghost_top_right == tail:
                        ghost_top_right = '400'
                    if ghost_top_right == tail:
                        ghost_top_right = '400'
                    if ghost_left_left == tail:
                        ghost_left_left = '400'
                    if ghost_right_right == tail:
                        ghost_right_right = '400'
                    if ghost_down_left == tail:
                        ghost_down_left = '400'
                    if ghost_down_down == tail:
                        ghost_down_down = '400'
                    if ghost_down_right == tail:
                        ghost_down_right = '400'
                if tail == apple_move:
                    apple_moving = random.randrange(1, 100)
                    apple_move = str(apple_moving)
                if head == tail and death_ok == 'ok':
                    x = 'no'
                    y = 'no'
                    break
            nuber = int(add) + 1
            add = nuber
        ghost_top_left = int(ghost_top_left)
        ghost_top_right = int(ghost_top_right)
        ghost_top_up = int(ghost_top_up)
        ghost_left_left = int(ghost_left_left)
        ghost_right_right = int(ghost_right_right)
        ghost_down_left  = int(ghost_down_left)
        ghost_down_right = int(ghost_down_right)
        ghost_down_down = int(ghost_down_down)
        if ghost_top_left > 100:
            if ghost_top_up > 100:
                if ghost_top_right > 100:
                    ghost_up = 40000
        if ghost_top_left > 100:
            if ghost_left_left >100:
                if ghost_down_left > 100:
                    ghost_left = 40000
        if ghost_down_left > 100:
            if ghost_down_down > 100:
                if ghost_down_right > 100:
                    ghost_down = 40000
        if ghost_down_right > 100:
            if ghost_right_right > 100:
                if ghost_top_right > 100:
                    ghost_right = 40000
        if ghost_top_left > 200 and ghost_top_right > 200:
            ghost_up = ghost_up = 150
        if ghost_top_left > 200 and ghost_down_left > 200:
            ghost_left = ghost_left = 150
        if ghost_down_left > 200 and ghost_down_right > 200:
            ghost_down = ghost_down = 150
        if ghost_top_right > 200 and ghost_down_right > 200:
            ghost_left = ghost_right = 150
        add = 1
        end = 'end'
        q = 'start'
        while (q == 'start'):
                        for tail in (tail_1, tail_2, tail_3, tail_4, tail_5, tail_6, tail_7, tail_8, tail_9, tail_10, tail_11, tail_12, tail_13, tail_14, tail_15, tail_16, tail_17, tail_18, tail_19, tail_20, tail_21, tail_22, tail_23, tail_24, tail_25, tail_26, tail_27, tail_28, tail_29, tail_30, tail_31, tail_32, tail_33, tail_34, tail_35, tail_36, tail_37, tail_38, tail_39, tail_40, tail_41, tail_42,tail_43,tail_44,tail_45, tail_46, tail_47, tail_48, tail_49, tail_50, tail_51, tail_52, tail_53, tail_54, tail_55, tail_56, tail_57, tail_58, tail_59, tail_60, tail_61, tail_62, tail_63, tail_64, tail_65, tail_66, tail_67, tail_68, tail_69, tail_70, tail_71, tail_72, tail_73, tail_74, tail_75, tail_76, tail_77, tail_78, tail_79, tail_80, tail_81, tail_82, tail_83, tail_84, tail_85, tail_86, tail_87, tail_88, tail_89, tail_90, tail_91, tail_92, tail_93, tail_94, tail_95, tail_96, tail_97, tail_98, tail_99, tail_100, end):
                            if add <= snake_lanth:
                                if tail == apple_move:
                                    rect_color_moving = random.randrange(1, 100)
                                    apple_move = str(rect_color_moving)
                                    add = 0
                                    break
                            if tail == end:
                                q = 'stop'
                            nuber = (add) + 1
                            add = nuber
        add = 1
        if ghost_down == '101':
            ghost_down = '1'
        if ghost_down == '102':
            ghost_down = '2'
        if ghost_down == '103':
            ghost_down = '3'
        if ghost_down == '104':
            ghost_down = '4'
        if ghost_down == '105':
            ghost_down = '5'
        if ghost_down == '106':
            ghost_down = '6'
        if ghost_down == '107':
            ghost_down = '7'
        if ghost_down == '108':
            ghost_down = '8'
        if ghost_down == '109':
            ghost_down = '9'
        if ghost_down == '110':
            ghost_down == '10'
        if ghost_up == '-1':
            ghost_up = '99'
        if ghost_up == '-2':
            ghost_up = '98'
        if ghost_up == '-3':
            ghost_up = '97'
        if ghost_up == '-4':
            ghost_up = '96'
        if ghost_up == '-5':
            ghost_up = '95'
        if ghost_up == '-6':
            ghost_up = '94'
        if ghost_up == '-7':
            ghost_up = '93'
        if ghost_up == '-8':
            ghost_up = '92'
        if ghost_up == '-9':
            ghost_up = '91'
        if ghost_up == '0':
            ghost_up = '100'
        if int(ghost_up) < int(apple_move):
            ghost_up = int(apple_move) - int(ghost_up)
        if int(ghost_down) < int(apple_move):
            ghost_down = int(apple_move) - int(ghost_down)
        if int(ghost_right) < int(apple_move):
            ghost_right = int(apple_move) - int(ghost_right)
        if int(ghost_left) < int(apple_move):
            ghost_left = int(apple_move) - int(ghost_left)
        if int(ghost_up) > int(apple_move):
            ghost_up = int(ghost_up) - int(apple_move)
        if int(ghost_down) > int(apple_move):
            ghost_down = int(ghost_down) - int(apple_move)
        if int(ghost_right) > int(apple_move):
            ghost_right = int(ghost_right) - int(apple_move)
        if int(ghost_left) > int(apple_move):
            ghost_left = int(ghost_left) - int(apple_move)
        if ghost_up == apple_move:
            ghost_up = '0'
        if ghost_down == apple_move:
            ghost_down = '0'
        if ghost_right == apple_move:
            ghost_right = '0'
        if ghost_left == apple_move:
            ghost_left = '0'
        adding = 1
        lowest = 1000
        for ghost in (ghost_up, ghost_down, ghost_right, ghost_left):
            if int(ghost) < int(lowest):
                lowest = ghost
                move = adding
            adding = adding + 1
        if apple_move == '1':
            spot_1 = apple
        if apple_move == '2':
            spot_2 = apple
        if apple_move == '3':
            spot_3 = apple
        if apple_move == '4':
            spot_4 = apple 
        if apple_move == '5':
            spot_5 = apple 
        if apple_move == '6':
            spot_6 = apple 
        if apple_move == '7':
            spot_7 = apple 
        if apple_move == '8':
            spot_8 = apple 
        if apple_move == '9':
            spot_9 = apple 
        if apple_move == '10':
            spot_10 = apple 
        if apple_move == '11':
            spot_11 = apple 
        if apple_move == '12':
            spot_12 = apple 
        if apple_move == '13':
            spot_13 = apple 
        if apple_move == '14':
            spot_14 = apple 
        if apple_move == '15':
            spot_15 = apple 
        if apple_move == '16':
            spot_16 = apple 
        if apple_move == '17':
            spot_17 = apple 
        if apple_move == '18':
            spot_18 = apple 
        if apple_move == '19':
            spot_19 = apple 
        if apple_move == '20':
            spot_20 = apple 
        if apple_move == '21':
            spot_21 = apple 
        if apple_move == '22':
            spot_22 = apple 
        if apple_move == '23':
            spot_23 = apple 
        if apple_move == '24':
            spot_24 = apple 
        if apple_move == '25':
            spot_25 = apple 
        if apple_move == '26':
            spot_26 = apple 
        if apple_move == '27':
            spot_27 = apple 
        if apple_move == '28':
            spot_28 = apple 
        if apple_move == '29':
            spot_29 = apple 
        if apple_move == '30':
            spot_30 = apple 
        if apple_move == '31':
            spot_31 = apple 
        if apple_move == '32':
            spot_32 = apple 
        if apple_move == '33':
            spot_33 = apple 
        if apple_move == '34':
            spot_34 = apple 
        if apple_move == '35':
            spot_35 = apple 
        if apple_move == '36':
            spot_36 = apple 
        if apple_move == '37':
            spot_37 = apple 
        if apple_move == '38':
            spot_38 = apple 
        if apple_move == '39':
            spot_39 = apple 
        if apple_move == '40':
            spot_40 = apple 
        if apple_move == '41':
            spot_41 = apple
        if apple_move == '42':
            spot_42 = apple 
        if apple_move == '43':
            spot_43 = apple 
        if apple_move == '44':
            spot_44 = apple 
        if apple_move == '45':
            spot_45 = apple 
        if apple_move == '46':
            spot_46 = apple 
        if apple_move == '47':
            spot_47 = apple 
        if apple_move == '48':
            spot_48 = apple 
        if apple_move == '49':
            spot_49 = apple 
        if apple_move == '50':
            spot_50 = apple 
        if apple_move == '51':
            spot_51 = apple 
        if apple_move == '52':
            spot_52 = apple 
        if apple_move == '53':
            spot_53 = apple 
        if apple_move == '54':
            spot_54 = apple 
        if apple_move == '55':
            spot_55 = apple 
        if apple_move == '56':
            spot_56 = apple 
        if apple_move == '57':
            spot_57 = apple 
        if apple_move == '58':
            spot_58 = apple 
        if apple_move == '59':
            spot_59 = apple 
        if apple_move == '60':
            spot_60 = apple 
        if apple_move == '61':
            spot_61 = apple 
        if apple_move == '62':
            spot_62 = apple 
        if apple_move == '63':
            spot_63 = apple 
        if apple_move == '64':
            spot_64 = apple 
        if apple_move == '65':
            spot_65 = apple 
        if apple_move == '66':
            spot_66 = apple 
        if apple_move == '67':
            spot_67 = apple 
        if apple_move == '68':
            spot_68 = apple 
        if apple_move == '69':
            spot_69 = apple 
        if apple_move == '70':
            spot_70 = apple 
        if apple_move == '71':
            spot_71 = apple 
        if apple_move == '72':
            spot_72 = apple 
        if apple_move == '73':
            spot_73 = apple 
        if apple_move == '74':
            spot_74 = apple 
        if apple_move == '75':
            spot_75 = apple 
        if apple_move == '76':
            spot_76 = apple 
        if apple_move == '77':
            spot_77 = apple 
        if apple_move == '78':
            spot_78 = apple 
        if apple_move == '79':
            spot_79 = apple 
        if apple_move == '80':
            spot_80 = apple 
        if apple_move == '81':
            spot_81 = apple 
        if apple_move == '82':
            spot_82 = apple 
        if apple_move == '83':
            spot_83 = apple 
        if apple_move == '84':
            spot_84 = apple 
        if apple_move == '85':
            spot_85 = apple 
        if apple_move == '86':
            spot_86 = apple 
        if apple_move == '87':
            spot_87 = apple 
        if apple_move == '88':
            spot_88 = apple 
        if apple_move == '89':
            spot_89 = apple 
        if apple_move == '90':
            spot_90 = apple 
        if apple_move == '91':
            spot_91 = apple 
        if apple_move == '92':
            spot_92 = apple 
        if apple_move == '93':
            spot_93 = apple 
        if apple_move == '94':
            spot_94 = apple 
        if apple_move == '95':
            spot_95 = apple 
        if apple_move == '96':
            spot_96 = apple 
        if apple_move == '97':
            spot_97 = apple 
        if apple_move == '98':
            spot_98 = apple 
        if apple_move == '99':
            spot_99 = apple 
        if apple_move == '100':
            spot_100 = apple
        if head == '1':
            spot_1 = snake 
        if head == '2':
            spot_2 = snake 
        if head == '3':
            spot_3 = snake 
        if head == '4':
            spot_4 = snake 
        if head == '5':
            spot_5 = snake 
        if head == '6':
            spot_6 = snake 
        if head == '7':
            spot_7 = snake 
        if head == '8':
            spot_8 = snake 
        if head == '9':
            spot_9 = snake 
        if head == '10':
            spot_10 = snake 
        if head == '11':
            spot_11 = snake 
        if head == '12':
            spot_12 = snake 
        if head == '13':
            spot_13 = snake 
        if head == '14':
            spot_14 = snake 
        if head == '15':
            spot_15 = snake 
        if head == '16':
            spot_16 = snake 
        if head == '17':
            spot_17 = snake 
        if head == '18':
            spot_18 = snake 
        if head == '19':
            spot_19 = snake 
        if head == '20':
            spot_20 = snake 
        if head == '21':
            spot_21 = snake 
        if head == '22':
            spot_22 = snake 
        if head == '23':
            spot_23 = snake 
        if head == '24':
            spot_24 = snake 
        if head == '25':
            spot_25 = snake 
        if head == '26':
            spot_26 = snake 
        if head == '27':
            spot_27 = snake 
        if head == '28':
            spot_28 = snake 
        if head == '29':
            spot_29 = snake 
        if head == '30':
            spot_30 = snake 
        if head == '31':
            spot_31 = snake 
        if head == '32':
            spot_32 = snake 
        if head == '33':
            spot_33 = snake 
        if head == '34':
            spot_34 = snake 
        if head == '35':
            spot_35 = snake 
        if head == '36':
            spot_36 = snake 
        if head == '37':
            spot_37 = snake 
        if head == '38':
            spot_38 = snake 
        if head == '39':
            spot_39 = snake 
        if head == '40':
            spot_40 = snake 
        if head == '41':
            spot_41 = snake 
        if head == '42':
            spot_42 = snake 
        if head == '43':
            spot_43 = snake 
        if head == '44':
            spot_44 = snake 
        if head == '45':
            spot_45 = snake 
        if head == '46':
            spot_46 = snake 
        if head == '47':
            spot_47 = snake 
        if head == '48':
            spot_48 = snake 
        if head == '49':
            spot_49 = snake 
        if head == '50':
            spot_50 = snake 
        if head == '51':
            spot_51 = snake 
        if head == '52':
            spot_52 = snake 
        if head == '53':
            spot_53 = snake 
        if head == '54':
            spot_54 = snake 
        if head == '55':
            spot_55 = snake 
        if head == '56':
            spot_56 = snake 
        if head == '57':
            spot_57 = snake 
        if head == '58':
            spot_58 = snake 
        if head == '59':
            spot_59 = snake 
        if head == '60':
            spot_60 = snake 
        if head == '61':
            spot_61 = snake 
        if head == '62':
            spot_62 = snake 
        if head == '63':
            spot_63 = snake 
        if head == '64':
            spot_64 = snake 
        if head == '65':
            spot_65 = snake 
        if head == '66':
            spot_66 = snake 
        if head == '67':
            spot_67 = snake 
        if head == '68':
            spot_68 = snake 
        if head == '69':
            spot_69 = snake 
        if head == '70':
            spot_70 = snake 
        if head == '71':
            spot_71 = snake 
        if head == '72':
            spot_72 = snake 
        if head == '73':
            spot_73 = snake 
        if head == '74':
            spot_74 = snake 
        if head == '75':
            spot_75 = snake 
        if head == '76':
            spot_76 = snake 
        if head == '77':
            spot_77 = snake 
        if head == '78':
            spot_78 = snake 
        if head == '79':
            spot_79 = snake 
        if head == '80':
            spot_80 = snake 
        if head == '81':
            spot_81 = snake 
        if head == '82':
            spot_82 = snake 
        if head == '83':
            spot_83 = snake 
        if head == '84':
            spot_84 = snake 
        if head == '85':
            spot_85 = snake 
        if head == '86':
            spot_86 = snake 
        if head == '87':
            spot_87 = snake 
        if head == '88':
            spot_88 = snake 
        if head == '89':
            spot_89 = snake 
        if head == '90':
            spot_90 = snake 
        if head == '91':
            spot_91 = snake 
        if head == '92':
            spot_92 = snake 
        if head == '93':
            spot_93 = snake 
        if head == '94':
            spot_94 = snake 
        if head == '95':
            spot_95 = snake 
        if head == '96':
            spot_96 = snake 
        if head == '97':
            spot_97 = snake 
        if head == '98':
            spot_98 = snake 
        if head == '99':
            spot_99 = snake 
        if head == '100':
            spot_100 = snake
        if apple_move == head:
            apple_moving = random.randrange(1, 100)
            apple_move = str(apple_moving)
            nuber = int(snake_lanth) + 1
            snake_lanth = nuber
        if str(move) == '1': 
            movement = 'up'
        if str(move) == '3':
            movement = 'right'
        if str(move) == '4':
            movement = 'left'
        if str(move) == '2':
            movement = 'down'
        size = 49
        while (True):
            while (True):
                while (True):
                    while not exit:
                        canvas.fill(color)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit = True
                        pygame.draw.rect(canvas, spot_1,
                            pygame.Rect(0,0,size,size)) 
                        pygame.draw.rect(canvas, spot_2,
                            pygame.Rect(50,0,size,size)) 
                        pygame.draw.rect(canvas, spot_3,
                            pygame.Rect(100,0,size,size)) 
                        pygame.draw.rect(canvas, spot_4,
                            pygame.Rect(150,0,size,size)) 
                        pygame.draw.rect(canvas, spot_5,
                            pygame.Rect(200,0,size,size)) 
                        pygame.draw.rect(canvas, spot_6,
                            pygame.Rect(250,0,size,size)) 
                        pygame.draw.rect(canvas, spot_7,
                            pygame.Rect(300,0,size,size)) 
                        pygame.draw.rect(canvas, spot_8,
                            pygame.Rect(350,0,size,size)) 
                        pygame.draw.rect(canvas, spot_9,
                            pygame.Rect(400,0,size,size)) 
                        pygame.draw.rect(canvas, spot_10,
                            pygame.Rect(450,0,size,size)) 
                        pygame.draw.rect(canvas, spot_11,
                            pygame.Rect(0,50,size,size)) 
                        pygame.draw.rect(canvas, spot_12,
                            pygame.Rect(50,50,size,size)) 
                        pygame.draw.rect(canvas, spot_13,
                            pygame.Rect(100,50,size,size)) 
                        pygame.draw.rect(canvas, spot_14,
                            pygame.Rect(150,50,size,size)) 
                        pygame.draw.rect(canvas, spot_15,
                            pygame.Rect(200,50,size,size)) 
                        pygame.draw.rect(canvas, spot_16,
                            pygame.Rect(250,50,size,size)) 
                        pygame.draw.rect(canvas, spot_17,
                            pygame.Rect(300,50,size,size)) 
                        pygame.draw.rect(canvas, spot_18,
                            pygame.Rect(350,50,size,size)) 
                        pygame.draw.rect(canvas, spot_19,
                            pygame.Rect(400,50,size,size))
                        pygame.draw.rect(canvas, spot_20,
                            pygame.Rect(450,50,size,size)) 
                        pygame.draw.rect(canvas, spot_21,
                            pygame.Rect(0,100,size,size)) 
                        pygame.draw.rect(canvas, spot_22,
                            pygame.Rect(50,100,size,size)) 
                        pygame.draw.rect(canvas, spot_23,
                            pygame.Rect(100,100,size,size)) 
                        pygame.draw.rect(canvas, spot_24,
                            pygame.Rect(150,100,size,size)) 
                        pygame.draw.rect(canvas, spot_25,
                            pygame.Rect(200,100,size,size)) 
                        pygame.draw.rect(canvas, spot_26,
                            pygame.Rect(250,100,size,size)) 
                        pygame.draw.rect(canvas, spot_27,
                            pygame.Rect(300,100,size,size)) 
                        pygame.draw.rect(canvas, spot_28,
                            pygame.Rect(350,100,size,size)) 
                        pygame.draw.rect(canvas, spot_29,
                            pygame.Rect(400,100,size,size)) 
                        pygame.draw.rect(canvas, spot_30,
                            pygame.Rect(450,100,size,size)) 
                        pygame.draw.rect(canvas, spot_31,
                            pygame.Rect(0,150,size,size)) 
                        pygame.draw.rect(canvas, spot_32,
                            pygame.Rect(50,150,size,size)) 
                        pygame.draw.rect(canvas, spot_33,
                            pygame.Rect(100,150,size,size)) 
                        pygame.draw.rect(canvas, spot_34,
                            pygame.Rect(150,150,size,size)) 
                        pygame.draw.rect(canvas, spot_35,
                            pygame.Rect(200,150,size,size)) 
                        pygame.draw.rect(canvas, spot_36,
                            pygame.Rect(250,150,size,size)) 
                        pygame.draw.rect(canvas, spot_37,
                            pygame.Rect(300,150,size,size)) 
                        pygame.draw.rect(canvas, spot_38,
                            pygame.Rect(350,150,size,size)) 
                        pygame.draw.rect(canvas, spot_39,
                            pygame.Rect(400,150,size,size)) 
                        pygame.draw.rect(canvas, spot_40,
                            pygame.Rect(450,150,size,size)) 
                        pygame.draw.rect(canvas, spot_41,
                            pygame.Rect(0,200,size,size)) 
                        pygame.draw.rect(canvas, spot_42,
                            pygame.Rect(50,200,size,size)) 
                        pygame.draw.rect(canvas, spot_43,
                            pygame.Rect(100,200,size,size))
                        pygame.draw.rect(canvas, spot_44,
                            pygame.Rect(150,200,size,size)) 
                        pygame.draw.rect(canvas, spot_45,
                            pygame.Rect(200,200,size,size)) 
                        pygame.draw.rect(canvas, spot_46,
                            pygame.Rect(250,200,size,size)) 
                        pygame.draw.rect(canvas, spot_47,
                            pygame.Rect(300,200,size,size)) 
                        pygame.draw.rect(canvas, spot_48,
                            pygame.Rect(350,200,size,size)) 
                        pygame.draw.rect(canvas, spot_49,
                            pygame.Rect(400,200,size,size)) 
                        pygame.draw.rect(canvas, spot_50,
                            pygame.Rect(450,200,size,size)) 
                        pygame.draw.rect(canvas, spot_51,
                            pygame.Rect(0,250,size,size)) 
                        pygame.draw.rect(canvas, spot_52,
                            pygame.Rect(50,250,size,size)) 
                        pygame.draw.rect(canvas, spot_53,
                            pygame.Rect(100,250,size,size)) 
                        pygame.draw.rect(canvas, spot_54,
                            pygame.Rect(150,250,size,size)) 
                        pygame.draw.rect(canvas, spot_55,
                            pygame.Rect(200,250,size,size)) 
                        pygame.draw.rect(canvas, spot_56,
                            pygame.Rect(250,250,size,size)) 
                        pygame.draw.rect(canvas, spot_57,
                            pygame.Rect(300,250,size,size)) 
                        pygame.draw.rect(canvas, spot_58,
                            pygame.Rect(350,250,size,size)) 
                        pygame.draw.rect(canvas, spot_59,
                            pygame.Rect(400,250,size,size)) 
                        pygame.draw.rect(canvas, spot_60,
                            pygame.Rect(450,250,size,size)) 
                        pygame.draw.rect(canvas, spot_61,
                            pygame.Rect(0,300,size,size)) 
                        pygame.draw.rect(canvas, spot_62,
                            pygame.Rect(50,300,size,size)) 
                        pygame.draw.rect(canvas, spot_63,
                            pygame.Rect(100,300,size,size)) 
                        pygame.draw.rect(canvas, spot_64,
                            pygame.Rect(150,300,size,size)) 
                        pygame.draw.rect(canvas, spot_65,
                            pygame.Rect(200,300,size,size)) 
                        pygame.draw.rect(canvas, spot_66,
                            pygame.Rect(250,300,size,size)) 
                        pygame.draw.rect(canvas, spot_67,
                            pygame.Rect(300,300,size,size)) 
                        pygame.draw.rect(canvas, spot_68,
                            pygame.Rect(350,300,size,size)) 
                        pygame.draw.rect(canvas, spot_69,
                            pygame.Rect(400,300,size,size)) 
                        pygame.draw.rect(canvas, spot_70,
                            pygame.Rect(450,300,size,size)) 
                        pygame.draw.rect(canvas, spot_71,
                            pygame.Rect(0,350,size,size)) 
                        pygame.draw.rect(canvas, spot_72,
                            pygame.Rect(50,350,size,size)) 
                        pygame.draw.rect(canvas, spot_73,
                            pygame.Rect(100,350,size,size)) 
                        pygame.draw.rect(canvas, spot_74,
                            pygame.Rect(150,350,size,size)) 
                        pygame.draw.rect(canvas, spot_75,
                            pygame.Rect(200,350,size,size)) 
                        pygame.draw.rect(canvas, spot_76,
                            pygame.Rect(250,350,size,size)) 
                        pygame.draw.rect(canvas, spot_77,
                            pygame.Rect(300,350,size,size)) 
                        pygame.draw.rect(canvas, spot_78,
                            pygame.Rect(350,350,size,size)) 
                        pygame.draw.rect(canvas, spot_79,
                            pygame.Rect(400,350,size,size)) 
                        pygame.draw.rect(canvas, spot_80,
                            pygame.Rect(450,350,size,size)) 
                        pygame.draw.rect(canvas, spot_81,
                            pygame.Rect(0,400,size,size)) 
                        pygame.draw.rect(canvas, spot_82,
                            pygame.Rect(50,400,size,size)) 
                        pygame.draw.rect(canvas, spot_83,
                            pygame.Rect(100,400,size,size)) 
                        pygame.draw.rect(canvas, spot_84,
                            pygame.Rect(150,400,size,size)) 
                        pygame.draw.rect(canvas, spot_85,
                            pygame.Rect(200,400,size,size)) 
                        pygame.draw.rect(canvas, spot_86,
                            pygame.Rect(250,400,size,size)) 
                        pygame.draw.rect(canvas, spot_87,
                            pygame.Rect(300,400,size,size)) 
                        pygame.draw.rect(canvas, spot_88,
                            pygame.Rect(350,400,size,size)) 
                        pygame.draw.rect(canvas, spot_89,
                            pygame.Rect(400,400,size,size)) 
                        pygame.draw.rect(canvas, spot_90,
                            pygame.Rect(450,400,size,size)) 
                        pygame.draw.rect(canvas, spot_91,
                            pygame.Rect(0,450,size,size)) 
                        pygame.draw.rect(canvas, spot_92,
                            pygame.Rect(50,450,size,size)) 
                        pygame.draw.rect(canvas, spot_93,
                            pygame.Rect(100,450,size,size)) 
                        pygame.draw.rect(canvas, spot_94,
                            pygame.Rect(150,450,size,size)) 
                        pygame.draw.rect(canvas, spot_95,
                            pygame.Rect(200,450,size,size)) 
                        pygame.draw.rect(canvas, spot_96,
                            pygame.Rect(250,450,size,size)) 
                        pygame.draw.rect(canvas, spot_97,
                            pygame.Rect(300,450,size,size)) 
                        pygame.draw.rect(canvas, spot_98,
                            pygame.Rect(350,450,size,size)) 
                        pygame.draw.rect(canvas, spot_99,
                            pygame.Rect(400,450,size,size)) 
                        pygame.draw.rect(canvas, spot_100,
                            pygame.Rect(450,450,size,size))
                        pygame.display.update()
                        break
                    break
                break
            break
        if moving == 'yes':
            death_ok = 'ok'
        moving = 'yes'
        time.sleep(1)
