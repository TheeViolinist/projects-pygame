import pygame
#  import pygame_gui

pygame.font.init()  # Inicializa as fontes
pygame.init()
WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
RECT_LINE_X, RECT_LINE_Y = WIDTH / 2, HEIGHT / 2  # Linha principal da lista
SPACE_RECT = 50  # Espaçamento entre retangulos
LINE_WIDTH = 5
CONST_Y = 100  # Constante abaixo do eixo y principal

GAME_FONT = pygame.font.Font("Assets/arial.ttf", 30)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lista duplamente encadeada")


def fill_screen():
    WINDOW.fill(WHITE)
    pygame.display.update()


"""
class GUI:
    def __init__(self, clock):
        self.manager = pygame_gui.UIManager((WIDTH, HEIGHT))
        self.text_input = pygame_gui.elements.UITextEntryLine(relative_rect=
        pygame.Rect((50, 50), (100, 40)), manager=self.manager, object_id="#pos")
        self.rate = clock.tick(FPS) / 1000
        
    def run_events(self, event):
        self.manager.process_events(event)
    
    def run(self):
        self.manager.update(self.rate)
        self.manager.draw_ui(WINDOW)
        pygame.display.update()
    
    def pos_input(event):
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#pos":
            return True
    
    def number_pos(text):
        input_text = pygame.font.SysFont("bahnschrift", 100)
        number = input_text.render(text, True, BLACK)
        WINDOW.blit(number, (100, 100))
        pygame.display.update()
"""

class Rect:
    """Classe responsável por desenhar o retangulo
    e desenhar no seu centro um determinado valor"""
    def __init__(self, valor):
        self.valor = valor
        self.width = 100
        self.height = 50

    def draw_line(self, rect, di, color):
        """Funcao responsavel por desenhar uma linha, caso queremos apagar
        uma linha so enviar color como white ou cor do background e desenhar como preto
        precisamos da correcao pra n pintar errado"""
        line_speed = 0.1
        run = True
        rect_y = RECT_LINE_Y - self.height // 2
        if di == 0:
            line_start_back = (rect.centerx - self.width // 2) - SPACE_RECT
            line_end_b = line_start_back
     
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                line = pygame.draw.line(WINDOW, color, (line_start_back, rect.centery),
                        (line_end_b, rect.centery), LINE_WIDTH)
                if rect.colliderect(line):
                    run = False
                else:
                    line_end_b += line_speed
                pygame.display.update()
            
        if di == 1:
            line_start_next = (rect.centerx + self.width // 2) + SPACE_RECT
            line_end_n = line_start_next

            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                line = pygame.draw.line(WINDOW, color, (line_start_next, rect.centery), 
                        (line_end_n, rect.centery), LINE_WIDTH)
                if rect.colliderect(line):
                    run = False
                else:
                    line_end_n -= line_speed

                pygame.display.update()
    

    def move_rect(self, rect, x, y, valor):
        """Funcao responsavel por mover o retangulo de um ponto a outro"""
        run = True
        vel = 1
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            if rect.x <= x:
                if rect.y <= y:
                    run = False
                pygame.draw.rect(WINDOW, WHITE, (rect.x, rect.y, self.width, self.height), 2)
                rect.y -= vel
                rect = pygame.draw.rect(WINDOW, BLACK, (rect.x, rect.y,
                    self.width, self.height), 2)

            else:
                pygame.draw.rect(WINDOW, WHITE, (rect.x, rect.y, self.width, self.height), 2)
                rect.x -= vel
                rect = pygame.draw.rect(WINDOW, BLACK, (rect.x, rect.y,
                    self.width, self.height), 2)
            pygame.display.update()
            
    
        return rect


    def draw(self, node,  first):
        node_first = first

        if node.back is None and node.next is None:
            rect_x = RECT_LINE_X - self.width // 2
            rect_y = RECT_LINE_Y - self.height // 2
            
            rect = pygame.draw.rect(WINDOW, BLACK, (rect_x, rect_y,
                self.width, self.height), 2)
            node.rect = rect
            self.draw_line(node.rect, 0, BLACK)
            self.draw_line(node.rect, 1, BLACK)
            
            number = GAME_FONT.render(str(self.valor), True, BLACK)
            WINDOW.blit(number, (rect.centerx - number.get_width() // 2,
                rect.centery - number.get_height() // 2))

        elif node.next is None:
            print("ESTAMOS COLOCANDO UM ELEMENTO NO FIM DA LINHA")
            a = input()
        elif node.back is None:
            """Para adicionar no primeiro elemento
            iremos spawnar o objeto abaixo da linha principal
            apaga a linha a esquerda do primeiro elemento, coloca
            o retangulo naquela posicao e depois desenha a linha novamente"""

            rect_x = RECT_LINE_X - self.width // 2
            rect_y = (RECT_LINE_Y - self.height // 2) + CONST_Y

            # Envia o deseno do primeiro anterior para apgar sua linha esquerda
            self.draw_line(node.next.rect, 0, WHITE)
            rect = pygame.draw.rect(WINDOW, BLACK, (rect_x, rect_y,
                self.width, self.height), 2)
            pygame.display.update()
            
            # Posicao x que o objeto deve ir, que é baseado onde o primeiro está
            x = (node.next.rect.x - self.width // 2) - (2 * SPACE_RECT)
            node.rect = self.move_rect(rect, x , rect_y - CONST_Y,
                    self.valor)
            number = GAME_FONT.render(str(self.valor), True, BLACK)
            WINDOW.blit(number, (node.rect.centerx - number.get_width() // 2,
                node.rect.centery - number.get_height() // 2))
            self.draw_line(node.rect, 0, BLACK)
            self.draw_line(node.rect, 1, BLACK)
            pygame.display.update()


        pygame.display.update()
        return True

class Node:
    """Classe que representa o No da lista"""
    def __init__(self, value):
        """Cada no é representado por um objeto retangulo, seu valor e os ponteiros"""
        self.value = value
        self.rect = None # Desenho do retangulo associado ao no
        self.next = None
        self.back = None


class List:
    "Classe que representa a lista encadeada"
    def __init__(self):
        self.quant  = 0
        self.first = None
    
    def insert(self, value, pos):
        """Função responsável por inserir elemento numa posicao >= 1"""
        node = Node(value)
        if not self.quant:
            if pos == 1:
                pass
            else:
                print("Digite um valor validod e posicao\n")
                return -1
        elif pos < 0 or pos > self.quant:
            print(f'Digite um valor valido de posicao\n')
            return -1
        
        pos -= 1 # Ajeita a posicao para ficar de 0 ate n - 1 
        i = 0
        aux = self.first
        while i < pos:
            aux  = aux.next
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
            print("adicionou no primeiro")
        else:
            node.next = aux
            node.back = aux.back
            aux.back.next = node
            aux.back = node
        
        self.quant += 1
        rect = Rect(value)
        # Caso não tenhamos Nó, então escrevemos o primeiro nó
        if aux == None:
           rect.draw(node, self.first)
        else:
           rect.draw(node, self.first)
    

    def list_print(self):
        aux = self.first
        while aux is not None:
            print(f'{aux.value} ')
            aux = aux.next


def main():
    
    run = True
    draw_circle = False
    clock = pygame.time.Clock()
    fill_screen()

    number_insert = 0
    number_position = 0
    rectangles = List()
    
    while run:
        clock.tick(FPS)
        draw_rect = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        choice = input("Digite 'i' para inserir um valor ou 's' para sair: ")
        if choice.rstrip() == "i":
            number_insert = int(input("Digite o valor para inserir: "))
            number_position = int(input("Digite uma posicao: "))
            rectangles.insert(number_insert, number_position)
        elif choice.rstrip() == 's':
            run = False

    pygame.quit()
    
if __name__ == "__main__":
    main()
