import pygame

# Initialize Pygame
pygame.init()

# Set up the window
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the colors
background_color = (255, 255, 255)
line_color = (0, 0, 255)

# Set up the line
line_start = (50, 50)
line_end = (50, 10)
line_width = 5

# Draw the line on the screen
pygame.draw.line(screen, line_color, line_start, line_end, line_width)

# Update the screen
pygame.display.update()

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

