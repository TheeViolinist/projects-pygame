import pygame
import os

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tiro")

WHITE = (255, 255, 255)
FPS = 60  # Fps que irá rodar nosso main loop
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
VEL = 5
BLACK = (0, 0, 0)
BORDER = pygame.Rect(WIDTH/2 -5, 0, 10, HEIGHT)

# Estamos carregando a imagem que queremos e depois mudando sua escala
# Alem disso, rotacionamos a imagem em 90 graus
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
        os.path.join('Assets', 'spaceship_yellow.png'))

YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
        os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(red, yellow):
    """Função responsável por desenhar na tela e dar update na tela"""
    WINDOW.fill(WHITE)
    pygame.draw.rect(WINDOW, BLACK, BORDER)  # Desenhar a borda na tela
    # A posição 0,0 será no topo esquerdo da janela
    # Estamos adicionando a imagem na tela
    WINDOW.blit(YELLOW_SPACESHIP,(yellow.x, yellow.y))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    """Função responsável dependendo da da tecla pressionada movimentar a nave"""
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # Left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # Right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # Up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT:  # Down
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):

    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # Left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # Right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # Up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT:  # Down
        red.y += VEL

def main():
    # Criação de dois retangulos para auxilarem na movimentacao dos objetos
    # Damos a posição x, y, e medidas
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()  # Definimos o clock do nosso main loop
    run = True
    while run:
        clock.tick(FPS)  # Define o clock para 60 FPS
        # Verifica os eventos e ver se o programa foi fechado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()  # Aqui diz qual key foi utilizada
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
