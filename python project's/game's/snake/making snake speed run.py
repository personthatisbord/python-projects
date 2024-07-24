import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

snake_length = 1

playing = True

runs = True

high_score = 0
# Calculate the starting position to be in the middle of the screen
start_x, start_y = width // 2, height // 2
spots = [(start_x + x * 50, start_y, (0, 0, 0)) for x in range(snake_length)]

# Initial direction (right)
direction = (1, 0)

def pick_random_item(my_list):
    if not my_list:
        return None  # Return None if the list is empty
    else:
        return random.choice(my_list)

# Initial apple position
apple_x, apple_y = 100, 100  # Set a fixed position for the apple

# Main game loop
running = True
while playing:
    playing_ = input('Do you want to play again? (yes/no) ')
    if playing_ == 'no':
        playing = False
    if playing_ == 'yes':
        print('Starting in 5 seconds')
        time.sleep(1)
        print('Starting in 4 seconds')
        time.sleep(1)
        print('Starting in 3 seconds')
        time.sleep(1)
        print('Starting in 2 seconds')
        time.sleep(1)
        print('Starting in 1 second')
        time.sleep(1)
        snake_length = 1
        playing = True
        runs = True
        direction = (1, 0)
        start_x, start_y = width // 2, height // 2
        spots = [(start_x + x * 50, start_y, (0, 0, 0)) for x in range(snake_length)]
        while runs:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if real_direction != (0, 1):
                        if event.key == pygame.K_w:
                            direction = (0, -1)  # Move up
                    if real_direction != (1, 0):
                        if event.key == pygame.K_a:
                            direction = (-1, 0)  # Move left
                    if real_direction != (0, -1) :
                        if event.key == pygame.K_s:
                            direction = (0, 1)  # Move down
                    if real_direction != (-1, 0):
                        if event.key == pygame.K_d:
                            direction = (1, 0)  # Move right

            # Move the entire snake
            new_head = (spots[0][0] + direction[0] * 50, spots[0][1] + direction[1] * 50, (144, 238, 144))
            spots.insert(0, new_head)  # Insert new head at the beginning of the list
            real_direction = direction
            # Check for collisions with the apple
            head_x, head_y, _ = spots[0]
            if head_x == apple_x and head_y == apple_y:
                snake_length += 1
                # Check if the apple is on the snake body
                while (apple_x, apple_y, _) in spots:
                    apple_x, apple_y = pick_random_item([0, 50, 100, 150, 200, 250, 300, 350, 400, 450]), pick_random_item([0, 50, 100, 150, 200, 250, 300, 350, 400, 450])
                # Set a new position for the apple

            if head_x == -50 or head_x == 500 or head_y == -50 or head_y == 500:
                if high_score < snake_length:
                    print(f'You beat the high score! It was {high_score} and now it is {snake_length}')
                    high_score = snake_length
                print(f"Your score was {snake_length}.")
                print(f'The high score is {high_score}')
                runs = False

            # Check for collisions with itself
            if len(set(spots)) < len(spots):
                if high_score < snake_length:
                    print(f'You beat the high score! It was {high_score} and now it is {snake_length}')
                    high_score = snake_length
                print(f"Your score was {snake_length}.")
                print(f'The high score is {high_score}')
                runs = False

            # Trim the snake's tail if its length exceeds snake_length
            spots = spots[:snake_length]

            # Clear the screen
            screen.fill((0, 0, 0))

            # Draw the entire snake
            for x, y, color in spots:
                pygame.draw.rect(screen, (0, 255, 0), (x, y, 50, 50))  # Light Green color
            pygame.draw.rect(screen, (255, 0, 0), (apple_x, apple_y, 50, 50))  # Red apple

            # Update the display
            pygame.display.flip()

            # Control the speed of the snake's movement (adjust as needed)
            pygame.time.delay(200)

# Quit Pygame
pygame.quit()
sys.exit()

