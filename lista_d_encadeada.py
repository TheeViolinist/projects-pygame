import pygame
#  import pygame_gui

pygame.font.init()  # Inicializa as fontes
pygame.init()
WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
RECT_LINE_X, RECT_LINE_Y = WIDTH / 2, HEIGHT / 2
SPACE_RECT = 50  # Espaçamento entre retangulos
LINE_WIDTH = 5

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

    def draw_lines_first(self, rect):
        """Funcao responsavel por desenhar as setas do unico elemento 
        e primeiro da lista"""
        line_startx_next = rect.centerx + self.width // 2
        line_end_next = line_startx_next + SPACE_RECT
            
        line_startx_back = rect.centerx - self.width // 2
        line_end_back = line_startx_back - SPACE_RECT
            
        line_speed = 0.2
        line_end_n = line_startx_next
        line_end_b = line_startx_back

        run = True
        while run:
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            if line_end_n < line_end_next:
                pygame.draw.line(WINDOW, BLACK, (line_startx_next, rect.centery),
                    (line_end_n, rect.centery), LINE_WIDTH)
                line_end_n += line_speed
            if line_end_b > line_end_back:
                pygame.draw.line(WINDOW, BLACK, (line_startx_back, rect.centery),
                    (line_end_b, rect.centery), LINE_WIDTH)
                line_end_b -= line_speed

            if line_end_b <= line_end_back and line_end_n >= line_end_next:
                run = False

            pygame.display.update()

    def draw(self, node_back, node_next):

        if node_back is None and node_next is None:
            rect_x = RECT_LINE_X - self.width // 2
            rect_y = RECT_LINE_Y - self.height // 2
        
        elif node_next is None:
            print("ESTAMOS COLOCANDO UM ELEMENTO NO FIM DA LINHA")
            a = input()
        rect = pygame.draw.rect(WINDOW, BLACK, (rect_x, rect_y,
            self.width, self.height), 2)
        
        number = GAME_FONT.render(str(self.valor), True, BLACK)
        WINDOW.blit(number, (rect.centerx - number.get_width() // 2,
            rect.centery - number.get_height() // 2))
        
        # Fazendo as setas para caso ele seja o primeiro elemento adicionado
        # na lista
        if node_back is None and node_next is None:
            self.draw_lines_first(rect)
        pygame.display.update()
        return True

class Node:
    """Classe que representa o No da lista"""
    def __init__(self, value):
        """Cada no é representado por um objeto retangulo, seu valor e os ponteiros"""
        self.value = value
        self.rect = Rect(self.value)
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
        if pos < 0 or pos - 1 > self.quant:
            print(f'Digite um valor valido de posicao\n')
            return -1
        
     
        i = 1
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
        else:
            node.next = aux
            node.back = aux.back
            aux.back.next = node
            aux.back = node
        
        self.quant += 1
        if aux == None:
           # node.rect.draw(None, None)
           print("oi")
        else:
            print("ENTROU AQUI")
           # node.rect.draw(node.back, node.next)
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
    """
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
            rectangles.insert(number_insert, number_position - 1)
        elif choice.rstrip() == 's':
            run = False
    """
    #/rectangles.insert(1, 1)
    #ectangles.insert(2, 2)
    #ectangles.insert(2, 3)
    #ectangles.list_print()
    pygame.quit()
    
if __name__ == "__main__":
    main()
