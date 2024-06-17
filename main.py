# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen_width = 1260
screen_height = 720
square_size = 30  # pixels 
snake_colour = "green"
running = True
background_colour = "blue"
snake_x = 0
snake_y = 0
fps = 5
direction = "right"
screen_squares_x = screen_width / square_size
screen_squares_y = screen_height / square_size

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if direction != "up":
                   direction = "down"
            elif event.key == pygame.K_UP:
                if direction != "down":
                   direction = "up"
            elif event.key == pygame.K_LEFT:
                if direction != "right":
                   direction = "left"
            elif event.key == pygame.K_RIGHT:
                if direction != "left":
                   direction = "right"
                
    #Movement
    if direction == "down":
        snake_y += square_size
    elif direction == "up":
        snake_y -= square_size
    elif direction == "left":
        snake_x -= square_size
    elif direction == "right":
        snake_x += square_size

    # Calculations
    snake_squares_x = snake_x / square_size
    snake_squares_y = snake_y / square_size
    if snake_squares_x >= screen_squares_x:
        snake_x = 0
    elif snake_squares_x == 0:
        snake_x = 1260
    elif snake_squares_y >= screen_squares_y:
        snake_y = 0
    elif snake_squares_y == 0:
        snake_y = 720 
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background_colour)

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, snake_colour, (snake_x, snake_y, square_size, square_size))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(fps)  # limits FPS to 60

pygame.quit()