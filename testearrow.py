import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the background color of the window
background_color = (255, 255, 255)

# Set the color of the arrow
arrow_color = (255, 0, 0)

#arrow = pygame.draw.polygon(screen, (255, 255, 255), ((200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
arrow = pygame.draw.polygon(screen, (255, 255, 255), ((10, 10), (10, 20), (20, 10), (10, 0), (10, 5)))

# Update the screen
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

