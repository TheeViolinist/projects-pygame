import pygame
pygame.init()

# Definir as dimensões da janela
screen_width = 800
screen_height = 600

# Criar a janela
screen = pygame.display.set_mode((screen_width, screen_height))

# Definir as coordenadas do retângulo
rect_x = -90
rect_y = 100
rect_width = 50
rect_height = 50
position_rect_x =  rect_x
# Loop principal do jogo
running = True
clock = pygame.time.Clock()
while running:
    # Desenhar o retângulo na tela
    rect = pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height), 2)
    print(rect.x)
    # Atualizar a tela
    pygame.display.flip()

    # Mover a tela em direção ao retângulo
    # A minha screen deve mover o mesmo que meu retangulo aumenta
    if rect_x < 0:
        rect_x += 1
        screen.scroll(-1, 0)

    # Limitar a taxa de atualização do jogo
    clock.tick(60)

    # Checar se o usuário clicou no botão fechar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Finalizar o Pygame
pygame.quit()

