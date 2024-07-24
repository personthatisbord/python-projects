import pygame
import random
pygame.init()
right = 0
left = 'yes'
top = 0
level = 1
jump_stop = 0
jump = 'no'
next_level = 0, 200, 255
sub_level = 1
damage = (255, 0, 0)
loc = (0, 255, 0)
damage_yes = 'no'
damage_check = 'no'
pos_x = 1
add = 0
of = 1
dash = 51
grav_check = 1
jumping = 'no'
tp_check = 'no'
def normal_block(pos, pos_x, box_y, box_x, size_y, size_x, first):
    if first == 'yes':
        pygame.draw.rect(canvas, color, pygame.Rect(box_x, box_y, size_x, size_y))
        return 'no'
    if pos == box_y - size_y and pos_x < box_x + size_x and pos_x > box_x or pos == box_y - size_y and pos_x + size_y < box_x + size_x and pos_x + size_y > box_x:
        pygame.draw.rect(canvas, color, pygame.Rect(box_x, box_y, size_x, size_y))
        return 'no'
    else:
        pygame.draw.rect(canvas, color, pygame.Rect(box_x, box_y, size_x, size_y))
        return 'yes'
def next_level_block(pos, pos_x, box_y, box_x, size_y, size_x, first):
    box_y += 10
    if pos == box_y - size_y and pos_x < box_x + size_x and pos_x > box_x or pos == box_y - size_y and pos_x + size_y < box_x + size_x and pos_x + size_y > box_x or pos + size == box_y - size_y and pos_x < box_x + size_x and pos_x > box_x or pos + size == box_y - size_y and pos_x + size_y < box_x + size_x and pos_x + size_y > box_x:
        box_y -= 10
        pygame.draw.rect(canvas, next_level, pygame.Rect(box_x, box_y, size_x, size_y))
        return 'yes'
    else:
        box_y -= 10
        pygame.draw.rect(canvas, next_level, pygame.Rect(box_x, box_y, size_x, size_y))
def damage_block(pos, pos_x, box_y, box_x, size_y, size_x, first):
    box_y += 10
    if first == 'yes':
        box_y -= 10
        pygame.draw.rect(canvas, damage, pygame.Rect(box_x, box_y, size_x, size_y))
        return 'yes'
    if pos == box_y - size_y and pos_x < box_x + size_x and pos_x > box_x or pos == box_y - size_y and pos_x + size_y < box_x + size_x and pos_x + size_y > box_x or pos + size == box_y - size_y and pos_x < box_x + size_x and pos_x > box_x or pos + size == box_y - size_y and pos_x + size_y < box_x + size_x and pos_x + size_y > box_x:
        box_y -= 10
        pygame.draw.rect(canvas, damage, pygame.Rect(box_x, box_y, size_x, size_y))
        return 'yes'
    else:
        box_y -= 10
        pygame.draw.rect(canvas, damage, pygame.Rect(box_x, box_y, size_x, size_y))
def falling_damage_block(pos, pos_x, box_y, box_x, size_y, size_x, first):
    if first == 'yes':
        pygame.draw.rect(canvas, damage, pygame.Rect(box_x, box_y, size_x, size_y))
        return 'yes'
    if pos == box_y - size_y and pos_x < box_x + size_x and pos_x > box_x or pos == box_y - size_y and pos_x + size_y < box_x + size_x and pos_x + size_y > box_x:
        pygame.draw.rect(canvas, damage, pygame.Rect(box_x, box_y, size_x, size_y))
        return 'yes'
    else:
        pygame.draw.rect(canvas, damage, pygame.Rect(box_x, box_y, size_x, size_y))
def tp_block(pos, pos_x, box_y, box_x, size_y, size_x, first):
    box_y += 10
    if first == 'yes':
        box_y -= 10
        pygame.draw.rect(canvas, loc, pygame.Rect(box_x, box_y, size_x, size_y))
        return 'yes'
    if pos == box_y - size_y and pos_x < box_x + size_x and pos_x > box_x or pos == box_y - size_y and pos_x + size_y < box_x + size_x and pos_x + size_y > box_x or pos + size == box_y - size_y and pos_x < box_x + size_x and pos_x > box_x or pos + size == box_y - size_y and pos_x + size_y < box_x + size_x and pos_x + size_y > box_x:
        box_y -= 10
        pygame.draw.rect(canvas, loc, pygame.Rect(box_x, box_y, size_x, size_y))
        return 'yes'
    else:
        box_y -= 10
        pygame.draw.rect(canvas, loc, pygame.Rect(box_x, box_y, size_x, size_y))
def iva_block(pos, pos_x, box_y, box_x, size_y, size_x, first):
    if first == 'yes':
        return 'no'
    if pos == box_y - size_y and pos_x < box_x + size_x and pos_x > box_x or pos == box_y - size_y and pos_x + size_y < box_x + size_x and pos_x + size_y > box_x:
        return 'no'
    else:
        return 'yes'
canvas = pygame.display.set_mode((500, 500))
pygame.display.set_caption("square game")

grav = 'yes'
size = 10
pos = 1
color = (225, 225, 225)
player = 125, 100, 70
exit_game = False
while (True):
    grav = 'yes'
    first = 'no'
    damage_check = 'no'
    keys = pygame.key.get_pressed()
    # Check if the 'W' key is held down
    if keys[pygame.K_d] and pos_x != 490 and left != 'no':
        pos_x += 1
    if keys[pygame.K_a] and pos_x != 0:
        pos_x -= 1
    if keys[pygame.K_w] and jump == 'yes':
        jumping = 'yes'
    canvas.fill((0, 0, 0))
    if grav == 'no':
        grav_check = 1
    if pos == 490:
        if level != 5:
            pos = 1
            pos_x = 1
        else:
            pos = 1
            pos_x = 250
    if level == 1:
        grav = normal_block(pos, pos_x, 250, 0, 10, 100, first)
        if grav == 'no':
            first = 'yes'
        grav = normal_block(pos, pos_x, 250, 100, 10, 100, first)
        next_level_que = next_level_block(pos, pos_x, 240, 190, 10, 10, first)
        if next_level_que == 'yes':
            level += 1
            pos = 1
            pos_x = 1
    if level == 2:
        grav = normal_block(pos, pos_x, 250, 0, 10, 100, first)
        if grav == 'no':
            first = 'yes'
        grav = normal_block(pos, pos_x, 250, 100, 10, 100, first)
        if grav == 'no':
            first = 'yes'
        grav = normal_block(pos, pos_x, 200, 200, 10, 100, first)
        next_level_que = next_level_block(pos, pos_x, 190, 290, 10, 10, first)
        if next_level_que == 'yes':
            level += 1
            pos = 1
            pos_x = 1
    if level == 3:
        grav = normal_block(pos, pos_x, 250, 0, 10, 100, first)
        if grav == 'no':
            first = 'yes'
        grav = normal_block(pos, pos_x, 250, 110, 10, 100, first)
        if grav == 'no':
            first = 'yes'
        grav = normal_block(pos, pos_x, 250, 220, 10, 100, first)
        damage_yes = damage_block(pos, pos_x, 240, 100, 10, 10, damage_check)
        if damage_yes == 'yes':
            damage_check = 'yes'
        damage_yes = damage_block(pos, pos_x, 240, 210, 10, 10, damage_check)
        if damage_yes == 'yes':
            pos = 1
            pos_x = 1
        next_level_que = next_level_block(pos, pos_x, 240, 320, 10, 10, first)
        if next_level_que == 'yes':
            level += 1
            pos = 1
            pos_x = 1
    if level == 4:
        grav = normal_block(pos, pos_x, 250, 0, 10, 100, first)
        if grav == 'no':
            first = 'yes'
        grav = normal_block(pos, pos_x, 250, 400, 10, 100, first)
        tp_yes = tp_block(pos, pos_x, 240, 90, 10, 10, tp_check)
        if tp_yes == 'yes':
            pos = 239
            pos_x = 400
        next_level_que = next_level_block(pos, pos_x, 240, 490, 10, 10, first)
        if next_level_que == 'yes':
            level += 1
            pos = 1
            pos_x = 250
    if level == 5:
        damage_yes = falling_damage_block(pos, pos_x, 50, 0, 10, 200, damage_check)
        if damage_yes == 'yes':
            damage_check = 'yes'
        damage_yes = falling_damage_block(pos, pos_x, 50, 300, 10, 200, damage_check)
        if damage_yes == 'yes':
            damage_check = 'yes'
        damage_yes = falling_damage_block(pos, pos_x, 250, 100, 10, 300, damage_check)
        if damage_yes == 'yes':
            damage_check = 'yes'
        damage_yes = falling_damage_block(pos, pos_x, 490, 0, 10, 500, damage_check)
        next_level_que = next_level_block(pos, pos_x, 450, 255, 10, 10, first)
        if next_level_que == 'yes':
            level += 1
            pos = 1
            pos_x = 1
        if damage_yes == 'yes':
            pos = 1
            pos_x = 250
    if level == 6:
        grav = iva_block(pos, pos_x, 250, 100, 10, 100, first)
        if grav == 'no':
            first = 'yes'
        next_level_que = next_level_block(pos, pos_x, 240, 200, 10, 10, first)
        if next_level_que == 'yes':
            level += 1
            pos = 1
            pos_x = 1
        grav = normal_block(pos, pos_x, 250, 0, 10, 100, first)
        tp_yes = tp_block(pos, pos_x, 300, 150, 10, 10, tp_check)
    if level == 7:
        grav = iva_block(pos, pos_x, 250, 100, 10, 79, first)
        if grav == 'no':
            first = 'yes'
        if True:
            if pos_x == 190:
                left = 'no'
            else:
                left = 'yes'
        next_level_que = next_level_block(pos, pos_x, 240, 200, 10, 10, first)
        if next_level_que == 'yes':
            level += 1
            pos = 1
            pos_x = 1
        grav = normal_block(pos, pos_x, 250, 0, 10, 100, first)
        tp_yes = tp_block(pos, pos_x, 300, 150, 10, 10, tp_check)
        if tp_yes == 'yes':
            pos = 229
            pos_x = 199
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
    jump = 'yes'
    if grav == 'yes':
        pos += 1
        jump = 'no'
    if jumping == 'yes':
        if jump_stop < 50:
            pos -= 2
            jump_stop += 1
        if jump_stop > 49:
            pos -= 1
            jump_stop += 1
        if jump_stop == 70:
            jump_stop = 0
            jumping = 'no'
            grav_check = 1
    pygame.draw.rect(canvas, player, pygame.Rect(pos_x, pos, size, size))
    pygame.display.update()