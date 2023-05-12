import pygame

from typing import Tuple


class Shape:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color
        self.rect = None
        self.width = None
        self.height = None
        
    def get_x(self):
        return self.pos[0]
    
    def get_y(self):
        return self.pos[1]
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def set_x(self, x):
        self.pos = (x, self.pos[1])
        
    def set_y(self, y):
        self.pos = (self.pos[0], y)
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def draw(self, surface):
        raise NotImplementedError("Subclass must implement abstract method")

    def update_rect(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def clicked(self, mouse_pos):
        raise NotImplementedError("Subclass must implement abstract method")


class Rectangle(Shape):

    def __init__(self, pos: Tuple[int, int], color: Tuple[int, int, int], width: int,
                 height: int):
        super().__init__(pos, color)
        self.width = width
        self.height = height
        self.update_rect()
    
        

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         pygame.Rect(self.pos, (self.width, self.height)))

    def update_rect(self):
        self.rect = pygame.Rect(self.pos, (self.width, self.height))

    def clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.clicked(event.pos)

class Circle(Shape):

    def __init__(self, pos, color, radius):
        super().__init__(pos, color)
        self.radius = radius
        self.update_rect()

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

    def update_rect(self):
        self.rect = pygame.Rect(self.pos[0] - self.radius,
                                self.pos[1] - self.radius, self.radius * 2,
                                self.radius * 2)

    def clicked(self, mouse_pos):
        # euclidian distance between center is less than radius
        return (self.pos[0] - mouse_pos[0])**2 + (
            self.pos[1] - mouse_pos[1])**2 <= self.radius**2

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.clicked(event.pos)


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Shapes Demo")
    clock = pygame.time.Clock()

    # create some shapes
    shapes = [
        Rectangle((100, 100), (255, 0, 0), 50, 100),
        Circle((300, 150), (0, 255, 0), 75),
    ]

    # main game loop
    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            for shape in shapes:
                shape.handle_event(event)

        # draw shapes
        screen.fill((255, 255, 255))
        for shape in shapes:
            shape.draw(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
