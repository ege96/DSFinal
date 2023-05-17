from dataclasses import dataclass

from .COLORS import *
from .shapes import Rectangle, Circle


@dataclass(order=True)
class Node:
    value: any


@dataclass(order=True)
class VisualNode(Node):
    def __init__(self, value, shape: Rectangle | Circle):
        super().__init__(value)
        self.shape: Rectangle | Circle = shape

    def draw(self, surface):
        """Draws the shape of the node on the surface specified"""
        self.shape.draw(surface)

    def draw_text(self, surface, text, font, color=BLACK):
        """Draws text in the middle of the node"""
        self.shape.draw_text(surface, text, font, color)

    def draw_outline(self, surface, color=BLACK):
        """Draws an outline around the node"""
        self.shape.draw_outline(surface, color)

    def update_shape(self):
        self.shape.update_rect()

    def handle_event(self, event):
        """"""
        return self.shape.handle_event(event)

    def resize(self, width, height):
        self.shape.set_width(width)
        self.shape.set_height(height)
        self.update_shape()

    def move(self, x, y):
        self.shape.set_x(x)
        self.shape.set_y(y)
        self.update_shape()
