import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
right_score = 0
left_score = 0
pygame.display.set_caption(f"{left_score}                                                   pong                                                   {right_score}")

# Set up the game loop
clock = pygame.time.Clock()

left_y = 249
right_y = 249
ball_x = 250
ball_y = random_number = random.randint(200, 400)
ball_der_x = random_item = random.choice(['left', 'right'])
ball_der_y = 'up'
counter = 0
counter_ = 0
speed = 2

# Set up key states
left_key_up_1 = True
left_key_up_2 = True
right_key_up_1 = True
right_key_up_2 = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_key_up_1 = False
            if event.key == pygame.K_s:
                left_key_up_2 = False
            if event.key == pygame.K_o:
                right_key_up_1 = False
            if event.key == pygame.K_l:
                right_key_up_2 = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                left_key_up_1 = True
            if event.key == pygame.K_s:
                left_key_up_2 = True
            if event.key == pygame.K_o:
                right_key_up_1 = True
            if event.key == pygame.K_l:
                right_key_up_2 = True

    if not left_key_up_1 and left_y > 0:
        left_y -= 4
    if not left_key_up_2 and left_y < height - 50:
        left_y += 4
    if not right_key_up_1 and right_y > 0:
        right_y -= 4
    if not right_key_up_2 and right_y < height - 50:
        right_y += 4
    counter += 1
    counter_ += 1
    if counter == 500 and speed < 3:
        speed += 1
        counter = 0
    if counter_ == 1:
        if ball_der_x == 'left':
            ball_x -= speed
        if ball_der_x == 'right':
            ball_x += speed
        if ball_y == 590 or  ball_y == 591 or ball_y == 589:
            ball_der_y = 'up'
        if ball_y != 0:
            if ball_der_y == 'up':
                ball_y -= speed
        if ball_y == 0 or ball_y ==-1 or ball_y == 1:
            ball_der_y = 'down'
        if ball_der_y == 'down':
            ball_y += speed
        counter_ = 0
    if ball_x == -10 or ball_x == -11 or ball_x == -9:
        right_score += 1
        pygame.display.set_caption(f"{left_score}                                                   pong                                                   {right_score}")
        ball_y = random_number = random.randint(200, 400)
        ball_x = 400
        ball_der_x = random_item = random.choice(['left', 'right'])
    if ball_x == 800:
        left_score += 1
        pygame.display.set_caption(f"{left_score}                                                   pong                                                   {right_score}")
        ball_y = random_number = random.randint(200, 400)
        ball_x == 400
        ball_der_x = random_item = random.choice(['left', 'right'])
    if ball_x == 30 or ball_x == 29 or ball_x == 31 and left_y < ball_y < left_y + 50:
        ball_der_x = 'right'
    if ball_x == 760 or ball_x == 759 or ball_x == 761 and right_y < ball_y < right_y + 50:
        ball_der_x = 'left'

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw rectangles
    pygame.draw.rect(screen, (255, 255, 255), (20, left_y, 10, 50))
    pygame.draw.rect(screen, (255, 255, 255), (770, right_y, 10, 50))
    pygame.draw.rect(screen, (255, 255, 255), (ball_x, ball_y, 10, 10))

    # Update display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

