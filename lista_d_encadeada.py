import pygame
import constants as const
import os

pygame.font.init()  # Inicializa as fontes
pygame.init()

button_width = 50
button_height = 50
rectangle_height = 50

GAME_FONT = pygame.font.Font("Assets/arial.ttf", 30)

WINDOW = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
pygame.display.set_caption("Lista duplamente encadeada")

BACKGROUND_IMAGE = pygame.image.load(
        os.path.join('Assets', 'background.jpeg'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (const.WIDTH, const.HEIGHT))
COLOR_MIDDLE = BACKGROUND.get_at((const.WIDTH // 2, const.HEIGHT // 2)) # Pega a cor do centro

def fill_screen():
    WINDOW.blit(BACKGROUND, (0, 0))
    pygame.display.update()


def draw_arrow(x, y, color, is_back):
    """Funcao responsável por desenhar a seta da flecha"""
    if is_back:
        arrow_points = [(x, y),
                        (x, y + const.ARROW_WIDTH),
                        (x - const.ARROW_WIDTH, y),
                        (x, y - const.ARROW_WIDTH),
                        (x, y)]
    else:
        arrow_points = [(x, y),
                        (x, y + const.ARROW_WIDTH),
                        (x + const.ARROW_WIDTH, y),
                        (x, y - const.ARROW_WIDTH),
                        (x, y)]
        
    pygame.draw.polygon(WINDOW, color, arrow_points)


def draw_line_not_an(x_init, y_init, x_end, y_end, color):
    """Funcao responssavel por desenhar setas sem animação"""
    line = pygame.draw.line(WINDOW, color, (x_init, y_init),
                                        (x_end, y_end), const.LINE_WIDTH)
    return line

class Rect:
    """Classe responsável por desenhar o retangulo
    e desenhar no seu centro um determinado valor"""

    def __init__(self, valor):
        """Inicialização do valor e tamanhos pré-definidos do retangulo"""
        self.valor = valor

    def draw_line(self, rect, is_next, color):
        """Funcao responsavel por desenhar uma linha, caso queremos apagar
        uma linha so enviar color como white ou cor do background ou
        apenas desennhar uma seta com outra determinada cor.
        A ideia então, é inicializar a seta na lateral extrema, distanciado
        por um valor que determina o espaço entre os retangulos
        O espaço entre retangulos é uma constante e temos que considerar o tamanho
        da ponta da flecha"""

        line_speed = 5
        run = True
        line_info = list()
        # Desenha a seta que aponta para o back
        # Quando termina de desenhar a reta, cria a ponta da seta
        if not is_next:
            line_start_back = (rect.centerx-const.WIDTH_RECT//2)
            line_end_b = line_start_back - const.SPACE_RECT - const.ARROW_WIDTH
            line_end = line_start_back

            # Vamos posicionar a seta back
            # no quarto superior
            position_y = rect.centery - (const.HEIGHT_RECT // 4)

            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                line = pygame.draw.line(WINDOW, color, (line_start_back, position_y),
                                        (line_end, position_y), const.LINE_WIDTH)

                if line_end <= line_end_b:
                    draw_arrow(line_end, position_y, color, True)
                    run = False
                else:
                    line_end -= line_speed

                pygame.display.update()

        if is_next:         
            line_start_next = (rect.centerx +const.WIDTH_RECT//2)
            line_end_n = line_start_next + const.SPACE_RECT + const.ARROW_WIDTH
            line_end = line_start_next

            # Vamos posicionar a seta do next
            # no quarto inferior
            position_y = rect.centery + (const.HEIGHT_RECT // 4)
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                line = pygame.draw.line(WINDOW, color, (line_start_next, position_y),
                                        (line_end, position_y), const.LINE_WIDTH)
                

                if line_end >= line_end_n:
                    draw_arrow(line_end, position_y, color, False)
                    run = False

                else:
                    line_end += line_speed

                pygame.display.update()

        

    def move_rect(self, rect, x, y, is_end):
        """Funcao responsavel por mover o retangulo de um ponto a outro
        A ideia basica é mover primeiro na posicao x e depois para a posicao y
        Na posicao x, devemos primeiramente desenhar o mesmo retangulo em
        branco depois mudamos sua posicao x e desenhamos novamente em preto
        para simular a animacao, após isso a mesma coisa com o valor de y"""
        run = True
        vel = 1
        # Adiciona no inicio da lista
        if not is_end:
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                if rect.x <= x:
                    if rect.y <= y:
                        run = False
                    
                    pygame.draw.rect(WINDOW, COLOR_MIDDLE, (rect.x, rect.y,
                                                           const.WIDTH_RECT, const.HEIGHT_RECT), 2) # Apaga o retangulo para dar sensação de movimento
                    
                    rect.y -= vel
                    rect.move(rect.x, rect.y) # Usamos a função de move para mover e não bugar
                    pygame.draw.rect(WINDOW, const.BLACK, (rect.x, rect.y,
                                                                 const.WIDTH_RECT, const.HEIGHT_RECT), 2)
                    
                
                else:

                    pygame.draw.rect(WINDOW, COLOR_MIDDLE, (rect.x, rect.y,
                                                           const.WIDTH_RECT, const.HEIGHT_RECT), 2) # Apaga o retangulo para dar sensação de movimento

                    rect.x -= vel
                    rect.move(rect.x, rect.y)

                    pygame.draw.rect(WINDOW, const.BLACK, (rect.x, rect.y,
                                                           const.WIDTH_RECT, const.HEIGHT_RECT), 2)
                pygame.display.update()

        if is_end:
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                if rect.x >= x:
                    if rect.y <= y:
                        run = False
                    pygame.draw.rect(WINDOW, COLOR_MIDDLE, (rect.x, rect.y,
                                                           const.WIDTH_RECT, const.HEIGHT_RECT), 2) # Apaga o retangulo para dar sensação de movimento

                    rect.y -= vel
                    rect.move(rect.x, rect.y)
                    pygame.draw.rect(WINDOW, const.BLACK, (rect.x, rect.y,
                                                                  const.WIDTH_RECT, const.HEIGHT_RECT), 2)
                else:
                    
                    pygame.draw.rect(WINDOW, COLOR_MIDDLE, (rect.x, rect.y,
                                                           const.WIDTH_RECT, const.HEIGHT_RECT), 2)
                    rect.x += vel
                    rect.move(rect.x, rect.y)
                    pygame.draw.rect(WINDOW, const.BLACK, (rect.x, rect.y,
                                                                  const.WIDTH_RECT, const.HEIGHT_RECT), 2)
                pygame.display.update()

        return rect


    def draw(self, node):
        """Funcao responsável por manejar todo o desenho do retangulo"""
        if node.back is None and node.next is None:
            """Caso estejamos adicionando o primeiro retangulo
            da nossa lista, vamos possicionar ele no meio da lista
            e desenhar o retangulo, salva sua imagem no no
            e depois desenhar as linhas e por fim o numero"""
            rect_x = const.RECT_LINE_X - const.WIDTH_RECT // 2
            rect_y = const.RECT_LINE_Y - const.HEIGHT_RECT // 2 + const.CONST_Y
            

            rect = pygame.draw.rect(WINDOW, const.BLACK, (rect_x, rect_y,
                                                          const.WIDTH_RECT, const.HEIGHT_RECT), 2)
            
            pygame.display.update()
            """Armazena todos os desenhos
            Desenhhamos a seta do next e back"""
            node.rect = rect
            node.rect = self.move_rect(rect, rect_x, rect_y - const.CONST_Y, 1)

            self.draw_line(node.rect, False, const.BLACK)

            self.draw_line(node.rect, True, const.BLACK)


        elif node.next is None:
            "O spaw inicial é o mesmo que nos outros, então podemos fazer"
            rect_x = const.RECT_LINE_X - const.WIDTH_RECT // 2
            rect_y = (const.RECT_LINE_Y - const.HEIGHT_RECT // 2) + const.CONST_Y

            "Vamos agora apagar o next do ultimo elemento anterior"
            self.draw_line(node.back.rect, 1, COLOR_MIDDLE)
            "Desenhando nosso retangulo"
            rect = pygame.draw.rect(WINDOW, const.BLACK, (rect_x, rect_y,
                                                          const.WIDTH_RECT, const.HEIGHT_RECT), 2)
            pygame.display.update()

            # Vamos agora calcular a posicao x que o objeto deve ir
            # A posicao x é referente a posicao do ultimo no
            x = (node.back.rect.x + const.WIDTH_RECT // 2) + \
                (2 * const.SPACE_RECT) + (2 * const.ARROW_WIDTH)
            node.rect = self.move_rect(rect, x, rect_y - const.CONST_Y, 1)
            # Vamos agora desenhar o next do ultimo elemento anterior
            self.draw_line(node.back.rect, True, const.BLACK)

            # Vamos desenhar o back do meu no atual e o next
            self.draw_line(node.rect, False, const.BLACK)

            self.draw_line(node.rect, True, const.BLACK)

        elif node.back is None:
            """Para adicionar no primeiro elemento
            iremos spawnar o objeto abaixo da linha principal
            apaga a linha a esquerda do primeiro elemento, coloca
            o retangulo naquela posicao e depois desenha a linha novamente.
            A posicao x que meu retangulo deve ir se baseia onde o
            primeiro se localiza, vamos posicionar x na ponta
            lateral esquerda do primeiro e multiplicar o espaço
            entre retangulos 2x, em relacao a posicao Y
            devemos apenas subir ele relativo a const_y
            Por fim renderizamos o valor no seu centro"""

            rect_x = const.RECT_LINE_X - const.WIDTH_RECT // 2
            rect_y = (const.RECT_LINE_Y - const.HEIGHT_RECT // 2) + const.CONST_Y

            # Envia o deseno do primeiro anterior para apgar sua linha esquerda
            self.draw_line(node.next.rect, False, COLOR_MIDDLE)
            # Desenha o retangulo
            rect = pygame.draw.rect(WINDOW, const.BLACK, (rect_x, rect_y,
                                                          const.WIDTH_RECT, const.HEIGHT_RECT), 2)
            pygame.display.update()

            # Posicao x que o objeto deve ir, que é baseado onde o primeiro está
            x = (node.next.rect.x - const.WIDTH_RECT // 2) - \
                (2 * const.SPACE_RECT) - (2*const.ARROW_WIDTH)
            print(f'movendo o no com valor: {node.value}')
            node.rect = self.move_rect(rect, x, rect_y - const.CONST_Y, False)
            print(f'valor: {node.value}, posicao x central inicial: {node.rect.centerx}, posicao y central inicial: {node.rect.centery}')
            # Desenhamos o back e o next do meu no atual
            self.draw_line(node.rect, False, const.BLACK)
            self.draw_line(node.rect, True, const.BLACK)

            # Devemos desenhar o back do primeiro anterior
            self.draw_line(node.next.rect, False, const.BLACK)
            pygame.display.update()

        
        number = GAME_FONT.render(str(self.valor), True, const.BLACK)
        WINDOW.blit(number, (node.rect.centerx - number.get_width() // 2,
                    node.rect.centery - number.get_height() // 2))
        
        pygame.display.update()
        return True


class Node:
    """Classe que representa o No da lista"""

    def __init__(self, value):
        """Cada no é representado por um objeto retangulo, seu valor, desenho das arrow e os ponteiros"""
        self.value = value
        self.rect = None  # Desenho do retangulo associado ao no
        self.next = None
        self.back = None


class List:
    "Classe que representa a lista encadeada"

    def __init__(self):
        self.quant = 0
        self.first = None

    def insert_end(self, value):
        """Funcao responsável por inserir o elemento no fim da lista"""
        node = Node(value)

        node.next = None
        # Se não temos elemento então ele será o primeiro
        if self.quant == 0:
            self.first = node
            node.back = None
        else:
            aux = self.first

            while aux.next is not None:
                aux = aux.next
            aux.next = node
            node.back = aux

        self.quant += 1
        rect = Rect(value)
        rect.draw(node)

    def insert_first_mid(self, value, pos):
        """Função responsável por inserir elemento numa posicao >= 1 que nao seja final"""
        node = Node(value)

        pos -= 1  # Ajeita a posicao para ficar de 0 ate n - 1
        i = 0
        aux = self.first
        while i < pos:
            aux = aux.next
            i += 1
        #  Estamos inserindo na primeira posicao
        if aux == self.first:
            node.back = None
            if not self.quant:
                node.next = None
            else:
                node.next = self.first
                self.first.back = node
            self.first = node
        else:
            node.next = aux
            node.back = aux.back
            aux.back.next = node
            aux.back = node

        self.quant += 1
        rect = Rect(value)
        rect.draw(node)

    def insert(self, value, pos):
        """Funcao responsavel por manejar a introducao de nos na lista"""
        if pos > 0 and pos <= self.quant:
            self.insert_first_mid(value, pos)
        elif pos == self.quant + 1:
            self.insert_end(value)
        else:
            print(f'Digite um valor valido de posicao\n')
            return -1

    def list_print(self):
        aux = self.first
        while aux is not None:
            print(f'{aux.value} ')
            aux = aux.next

    def move_nodes(self, x, is_left):
        """Funcao responslave por mover os nos para direita ou esquerda"""
        aux = self.first
        if is_left:
            x *= -1

        while aux is not None:
            print(f'valor: {aux.value}, posicao x central apos mover: {aux.rect.centerx}, posicao y central apos mover: {aux.rect.centery}')
            aux.rect.x += x
            aux = aux.next

    def draw_nodes(self):
        """Função responsável por desenhar todos os nós de uma unica vez"""
        aux = self.first
        position_y_up = aux.rect.centery - (const.HEIGHT_RECT // 4)
        position_y_down = aux.rect.centery + (const.HEIGHT_RECT // 4)


        while aux is not None:
            """Denhamos todos nas novas posições """

            pygame.draw.rect(WINDOW, const.BLACK, aux.rect, 2)
            number = GAME_FONT.render(str(aux.value), True, const.BLACK)
            WINDOW.blit(number, (aux.rect.centerx - number.get_width() // 2,
                                 aux.rect.centery - number.get_height() // 2))
      
            """Desenho das setas back e next"""
            x_init_back = aux.rect.centerx - const.WIDTH_RECT // 2
            x_end_back = x_init_back  - const.SPACE_RECT - const.ARROW_WIDTH
            
            x_init_next = aux.rect.centerx + const.WIDTH_RECT // 2
            x_end_next = x_init_next+ const.SPACE_RECT + const.ARROW_WIDTH

            new_line = draw_line_not_an(x_init_back, position_y_up, x_end_back, position_y_up, const.BLACK)
            draw_arrow(new_line.left, position_y_up, const.BLACK, True)

            new_line = draw_line_not_an(x_init_next, position_y_down, x_end_next, position_y_down, const.BLACK)
            draw_arrow(new_line.right, position_y_down, const.BLACK, False)
            aux = aux.next


def main():

    run = True
    clock = pygame.time.Clock()
    fill_screen()
    rectangles = List()
    

    """Botoes"""
    left_button_rect = pygame.Rect(
        0, const.HEIGHT - button_height, button_width, button_height)
    right_button_rect = pygame.Rect(const.WIDTH - button_width, const.HEIGHT - button_height,
                                    button_width, button_height)

    add = 1
    while run:
        flag_move = False
        vel_window = 10
        clock.tick(const.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                """A ideia é conseguirmos mover a tela par aum lado e os retangulos para o lado contrario"""
                if left_button_rect.collidepoint(mouse_x, mouse_y):
                    rectangles.move_nodes(vel_window, False)
                    flag_move = True
                    vel_window = -10

                elif right_button_rect.collidepoint(mouse_x, mouse_y):
                    rectangles.move_nodes(vel_window, True)
                    flag_move = True
                    vel_window = 10
        if add == 1:
            for i in range(7):
                rectangles.insert(i + 1,  rectangles.quant + 1)
            add = 0

        if flag_move:
            fill_screen()
            rectangles.draw_nodes()
            WINDOW.scroll(vel_window, 0)

        # Desenha os botões
        pygame.draw.rect(WINDOW, const.BLACK, left_button_rect)
        pygame.draw.rect(WINDOW, const.BLACK, right_button_rect)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
