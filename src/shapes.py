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

    def change_color(self, color):
        self.color = color
        self.update_rect()

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

    def draw_text(self, surface, text, font, color):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.pos[0] + self.width // 2, self.pos[1] + self.height // 2)
        surface.blit(text_surface, text_rect)

    def draw(self, surface, width: int = 2):
        pygame.draw.rect(surface, self.color,
                         self.rect, width)

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
        self.width = radius * 2
        self.height = radius * 2
        self.update_rect()

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

    def draw_outline(self, surface, color):
        pygame.draw.circle(surface, color, self.pos, self.radius, 1)

    def draw_text(self, surface, text, font, color):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = self.pos
        surface.blit(text_surface, text_rect)

    def update_rect(self):
        self.rect = pygame.Rect(self.pos[0] - self.radius,
                                self.pos[1] - self.radius, self.radius * 2,
                                self.radius * 2)

    def clicked(self, mouse_pos):
        # euclidian distance between center is less than radius
        return (self.pos[0] - mouse_pos[0]) ** 2 + (
                self.pos[1] - mouse_pos[1]) ** 2 <= self.radius ** 2

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.clicked(event.pos)
