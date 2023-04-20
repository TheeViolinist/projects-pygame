import pygame
import constants as const


pygame.font.init()  # Inicializa as fontes
pygame.init()


GAME_FONT = pygame.font.Font("Assets/arial.ttf", 30)

WINDOW = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
pygame.display.set_caption("Lista duplamente encadeada")


def fill_screen():
    WINDOW.fill(const.WHITE)
    pygame.display.update()


class Rect:
    """Classe responsável por desenhar o retangulo
    e desenhar no seu centro um determinado valor"""
    def __init__(self, valor):
        """Inicialização do valor e tamanhos pré-definidos do retangulo"""
        self.valor = valor
        self.width = 100
        self.height = 50
    

    def draw_line(self, rect, di, color):
        """Funcao responsavel por desenhar uma linha, caso queremos apagar
        uma linha so enviar color como white ou cor do background ou
        apenas desennhar uma seta com outra determinada cor.
        A ideia então, é inicializar a seta na lateral extrema, distanciado
        por um valor que determina o espaço entre os retangulos
        Entao vamos animar a seta até enconstar no retangulo"""

        line_speed = 0.1
        run = True
        
        # Desenha a seta que aponta para trás
        if di == 0:
            line_start_back = (rect.centerx-self.width//2)
                line_end_b = line_start_back -(const.SPACE_RECT - ARROW_WIDTH)
            line_end = line_start_back

            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                line = pygame.draw.line(WINDOW, color, (line_start_back, rect.centery),
                        (line_end, rect.centery), const.LINE_WIDTH)
                if line_end <= line_end_b:
                                       
                    run = False
                else:
                    line_end -= line_speed
                pygame.display.update()
            
        if di == 1:
            line_start_next = (rect.centerx+self.width//2) + const.SPACE_RECT
            line_end_n = line_start_next

            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                line = pygame.draw.line(WINDOW, color, (line_start_next, rect.centery),
                        (line_end_n, rect.centery), const.LINE_WIDTH)
                if rect.colliderect(line):
                    run = False
                else:
                    line_end_n -= line_speed

                pygame.display.update()


    def move_rect(self, rect, x, y, r):
        """Funcao responsavel por mover o retangulo de um ponto a outro
        A ideia basica é mover primeiro na posicao x e depois para a posicao y
        Na posicao x, devemos primeiramente desenhar o mesmo retangulo em
        branco depois mudamos sua posicao x e desenhamos novamente em preto
        para simular a animacao, após isso a mesma coisa com o valor de y"""
        run = True
        vel = 1
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            if rect.x <= x:
                if rect.y <= y:
                    run = False
                pygame.draw.rect(WINDOW, const.WHITE, (rect.x, rect.y, self.width, self.height), 2)
                
                rect.y -= vel
                rect = pygame.draw.rect(WINDOW, const.BLACK, (rect.x, rect.y,
                    self.width, self.height), 2)

            else:
                pygame.draw.rect(WINDOW, const.WHITE, (rect.x, rect.y, self.width, self.height), 2)
                rect.x -= vel
                rect = pygame.draw.rect(WINDOW, const.BLACK, (rect.x, rect.y,
                    self.width, self.height), 2)
            pygame.display.update()
        return rect


    def draw(self, node):
        """Funcao responsável por manejar todo o desenho do retangulo"""
        if node.back is None and node.next is None:
            """Caso estejamos adicionando o primeiro retangulo
            da nossa lista, vamos possicionar ele no meio da lista
            e desenhar o retangulo, salva sua imagem no no
            e depois desenhar as linhas e por fim o numero"""
            rect_x = const.RECT_LINE_X - self.width // 2
            rect_y = const.RECT_LINE_Y - self.height // 2
            
            rect = pygame.draw.rect(WINDOW, const.BLACK, (rect_x, rect_y,
                self.width, self.height), 2)
            node.rect = rect
            self.draw_line(node.rect, 0, const.BLACK)
            self.draw_line(node.rect, 1, const.BLACK)
            
            number = GAME_FONT.render(str(self.valor), True, const.BLACK)
            WINDOW.blit(number, (rect.centerx - number.get_width() // 2,
                rect.centery - number.get_height() // 2))

        elif node.next is None:
            "O spaw inicial é o mesmo que nos outros, então podemos fazer"
            rect_x = const.RECT_LINE_X - self.width // 2
            rect_y = (const.RECT_LINE_Y - self.height // 2) + const.CONST_Y
            print("entrou aqui")
            "Vamos agora apagar a linha direita do ultimo elemento anterior"
            self.draw_line(node.back.rect, 1, const.WHITE)
            "Desenhando nosso retangulo"
            rect = pygame.draw.rect(WINDOW, const.BLACK, (rect_x, rect_y,
                    self.width, self.height), 2)
            pygame.display.update()

            # Vamos agora calcular a posicao x que o objeto deve ir
            # A posicao x é referente a posicao do ultimo no
            x = (node.back.rect.x + self.width // 2) + (2 * const.SPACE_RECT)
            node.rect = self.move_rect(rect, x, rect_y - const.CONST_Y, 1)
            number = GAME_FONT.render(str(self.valor), True, const.BLACK)
            # WINDOW.blit(number, )
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

            rect_x = const.RECT_LINE_X - self.width // 2
            rect_y = (const.RECT_LINE_Y - self.height // 2) + const.CONST_Y

            # Envia o deseno do primeiro anterior para apgar sua linha esquerda
            self.draw_line(node.next.rect, 0, const.WHITE)
            # Desenha o retangulo
            rect = pygame.draw.rect(WINDOW, const.BLACK, (rect_x, rect_y,
                self.width, self.height), 2)
            pygame.display.update()
            
            # Posicao x que o objeto deve ir, que é baseado onde o primeiro está
            x = (node.next.rect.x - self.width // 2) - (2 * const.SPACE_RECT)
            node.rect = self.move_rect(rect, x , rect_y - const.CONST_Y, 0)

            number = GAME_FONT.render(str(self.valor), True, const.BLACK)
            WINDOW.blit(number, (node.rect.centerx - number.get_width() // 2,
                node.rect.centery - number.get_height() // 2))

            self.draw_line(node.rect, 0, const.BLACK)
            self.draw_line(node.rect, 1, const.BLACK)
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
        if  pos > 0 and pos <= self.quant:
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


def main():
    
    run = True
    clock = pygame.time.Clock()
    fill_screen()

    number_insert = 0
    number_position = 0
    rectangles = List()
    
    while run:
        clock.tick(const.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        choice = input("Digite 'i' para inserir um valor ou 's' para sair: ")
        if choice.rstrip() == "i":
            number_insert = int(input("Digite o valor para inserir: "))
            number_position = int(input("Digite uma posicao: "))
            rectangles.insert(number_insert, number_position)
            rectangles.list_print()
        elif choice.rstrip() == 's':
            run = False

    pygame.quit()
    
if __name__ == "__main__":
    main()
