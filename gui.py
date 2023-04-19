
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

