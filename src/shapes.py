from abc import ABC

import pygame


class Shape(ABC):
    """Abstract class for shapes"""

    def __init__(self, pos, color):
        self.pos: tuple[int, int] = pos
        self.color: tuple[int, int, int] = color
        self.rect = None
        self.width: int = -1
        self.height: int = -1

    def get_x(self) -> int:
        """Returns the x coordinate of the shape"""
        return self.pos[0]

    def get_y(self) -> int:
        """Returns the y coordinate of the shape"""
        return self.pos[1]

    def get_width(self) -> int:
        """Returns the width of the shape"""
        return self.width

    def get_height(self) -> int:
        """Returns the height of the shape"""
        return self.height

    def set_x(self, x):
        """Sets the x coordinate of the shape"""
        self.pos = (x, self.pos[1])

    def set_y(self, y):
        """Sets the y coordinate of the shape"""
        self.pos = (self.pos[0], y)

    def set_width(self, width):
        """Sets the width of the shape"""
        self.width = width

    def set_height(self, height):
        """Sets the height of the shape"""
        self.height = height

    def change_color(self, color):
        """Changes the color of the shape

        Args:
            color (tuple[int, int, int]): new color of the shape

        """
        self.color = color
        self.update_rect()

    def draw(self, surface):
        raise NotImplementedError("Subclass must implement abstract method")

    def update_rect(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def clicked(self, mouse_pos):
        raise NotImplementedError("Subclass must implement abstract method")


class Rectangle(Shape):
    """Rectangle shape class, inherits from Shape

    Args:
        pos (tuple[int, int]): position of the rectangle
        color (tuple[int, int, int]): color of the rectangle
        width (int): width of the rectangle
        height (int): height of the rectangle

    """
    def __init__(self, pos: tuple[int, int], color: tuple[int, int, int], width: int,
                 height: int):
        super().__init__(pos, color)
        self.width = width
        self.height = height
        self.update_rect()

    def draw_text(self, surface, text, font, color):
        """Draws text on center of the rectangle"""
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.pos[0] + self.width // 2, self.pos[1] + self.height // 2)
        surface.blit(text_surface, text_rect)

    def draw(self, surface, width: int = 2):
        """Draws the rectangle on the surface"""
        pygame.draw.rect(surface, self.color,
                         self.rect, width)

    def update_rect(self):
        """Updates the shape by recreating the rectangle"""
        self.rect = pygame.Rect(self.pos, (self.width, self.height))

    def clicked(self, mouse_pos):
        """Checks if the mouse is within the rectangle"""
        return self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        """Checks if the rectangle was clicked"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.clicked(event.pos)


class Circle(Shape):
    """Circle shape class, inherits from Shape

    Args:
        pos (tuple[int, int]): position of the circle
        color (tuple[int, int, int]): color of the circle
        radius (int): radius of the circle

    """
    def __init__(self, pos, color, radius):
        super().__init__(pos, color)
        self.radius = radius
        self.width = radius * 2
        self.height = radius * 2

    def draw(self, surface):
        """Draws the circle on the surface"""
        pygame.draw.circle(surface, self.color, self.pos, self.radius)

    def draw_outline(self, surface, color):
        """Draws the outline of the circle on the surface by drawing a circle with a width of 1 on top of the circle"""
        pygame.draw.circle(surface, color, self.pos, self.radius, 1)

    def draw_text(self, surface, text, font, color):
        """Draws text on center of the circle"""
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = self.pos
        surface.blit(text_surface, text_rect)

    def clicked(self, mouse_pos) -> bool:
        """Checks if the mouse is within the circle"""
        # euclidian distance between center is less than radius
        return (self.pos[0] - mouse_pos[0]) ** 2 + (
                self.pos[1] - mouse_pos[1]) ** 2 <= self.radius ** 2

    def handle_event(self, event) -> bool:
        """Checks if a mouse click is within the circle"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.clicked(event.pos)
