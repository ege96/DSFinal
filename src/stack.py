import pygame

from .COLORS import BLUE, BROWN, BLACK

from .shapes import Shape, Rectangle, Circle


# Define the Stack class
class Stack:
    def __init__(self, size, surface, font):
        self.size = size
        self.data = []
        self.top = -1
        self.surface = surface
        self.font = font
        self.setup()
        
    def push(self, value):
        if self.top < self.size-1:
            self.top += 1
            self.data.append(value)
        
    def pop(self):
        if self.top >= 0:
            self.top -= 1
            return self.data.pop()
        
    def is_empty(self):
        return self.top == -1
        
    def is_full(self):
        return self.top == self.size-1

    # Draw the stack
    def draw_stack():
        pygame.draw.rect(surface, BLACK, (stack_x, stack_y, stack_width, stack_height), 2)
        for i in range(stack_size):
            x = stack_x + 2
            y = stack_y + stack_height - ((i+1) * (stack_height//stack_size))
            if i <= stack.top:
                pygame.draw.rect(surface, GREEN, (x, y, stack_width-4, stack_height//stack_size-2))
                text = font.render(str(stack.data[i]), True, BLACK)
                text_rect = text.get_rect(center=(stack_x + stack_width//2, y + (stack_height//stack_size)//2))
                surface.blit(text, text_rect)
            else:
                pygame.draw.rect(surface, RED, (x, y, stack_width-4, stack_height//stack_size-2))
        
    # Draw the buttons
    def setup(self):
        add_button = Rectangle((WIDTH/2 - 400,425), BLACK, 200, 80)
        add_button.draw_text(self.surface, "Add", self.font, BLACK)

        pop_button = Rectangle((WIDTH/2 - 400,575), BLACK, 200, 80)
        pop_button.draw_text(self.surface, "Pop", self.font, BLACK)

        exit_button = Rectangle((WIDTH/2 + 200,500), BLACK, 200, 80)
        exit_button.draw_text(self.surface, "Exit", self.font, BLACK)

        self.btns = {"add": add_button, "pop": pop_button, "exit": exit_button}

    def _buttonMenu(self, event):
        for btn in self.btns:
            btn_obj = self.btns[btn]
            btn_obj.draw(self.surface, width=2)
            btn_obj.draw_text(self.surface, btn.capitalize(), self.font, BLACK)
            
            if btn_obj.handle_event(event):
                match btn:
                    case "add":
                        self.push()
                    case "pop":
                        self.pop()
                    case "exit":
                        return "exit"
        
    def visualize(self):
        while True:
            for event in pygame.event.get():
                if self._visualize(event) == "exit":
                    return
                    
    def _visualize(self, event):
        self.surface.fill(BLUE)
            
        if self._buttonMenu(event) == "exit":
            return "exit"
            
        # Draw the initial surface
        draw_stack()
        draw_buttons()
        pygame.display.flip()
    
        stack_size = 20 
        stack = Stack(stack_size, self.surface, self.font)
        stack_width = 300
        stack_height = 1000     
        stack_x = (WIDTH - stack_width) // 2
        stack_y = (HEIGHT - stack_height) // 2
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # Left click
                        pos = pygame.mouse.get_pos()
                        print(pos)
                        left = WIDTH/2 - 400
                        if ((pos[0] >= left) and (pos[0] <= left + 200)) and (pos[1] >= 425 and pos[1] <= 505):  # Adjusted button position
                            # Add to stack
                            if not stack.is_full():
                                value = stack.top + 1
                                stack.push(value)
                        elif ((pos[0] >= left) and (pos[0] <= left + 200)) and (pos[1] >= 575 and pos[1] <= 655):  # Adjusted button position
                            # Remove a value from the stack
                            if not stack.is_empty():
                                stack.pop()
                        print(WIDTH/2 + 200, WIDTH/2 + 400)
                        if ((WIDTH/2 + 200) <= pos[0] <= (WIDTH/2 + 400)) and (500 <= pos[1] <= 580):
                            running = False
                    
            # Redraw the surface
            surface.fill(BLUE)
            draw_stack()
            draw_buttons()
            pygame.display.flip()

