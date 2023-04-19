import pygame

# Inicializa o pygame
pygame.init()

# Define a largura e altura da janela
WINDOW_SIZE = (800, 600)

# Cria a janela
screen = pygame.display.set_mode(WINDOW_SIZE)

# Define a cor da linha e do retângulo
LINE_COLOR = (255, 0, 0)
RECT_COLOR = (0, 255, 0)

# Define a posição e tamanho do retângulo
rect_x = 300
rect_y = 200
rect_width = 100
rect_height = 100

# Define a posição inicial e final da linha
line_start = (100, 100)
line_end = (500, 400)

# Define a velocidade da linha
line_speed = 0.1

# Define a largura da linha
line_width = 5

# Cria um objeto Rect para o retângulo
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Loop principal do jogo
running = True
while running:
    # Verifica se houve um evento do pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move a linha
    line_start = (line_start[0] + line_speed, line_start[1])
    line_end = (line_end[0] + line_speed, line_end[1])

    # Desenha a linha na tela
    pygame.draw.line(screen, LINE_COLOR, line_start, line_end, line_width)

    # Desenha o retângulo na tela
    pygame.draw.rect(screen, RECT_COLOR, (rect_x, rect_y, rect_width, rect_height))

    # Cria um objeto Rect para a linha
    line_rect = pygame.Rect(min(line_start[0], line_end[0]), min(line_start[1], line_end[1]), abs(line_end[0] - line_start[0]), abs(line_end[1] - line_start[1]))

    # Verifica se a linha intersecta o retângulo
    if line_rect.colliderect(rect):
        print("A linha intersectou o retângulo.")
        line_speed = 0

    # Atualiza a janela
    pygame.display.flip()

    # Define o FPS do jogo
    pygame.time.Clock().tick(60)

# Encerra o pygame
pygame.quit()

