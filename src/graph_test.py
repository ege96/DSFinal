import pygame

from .node import Node

from .COLORS import *

from .shapes import Shape, Rectangle, Circle


class GraphNode(Node):
    def __init__(self, value, x: int, y: int, shape: Rectangle | Circle):
        super().__init__(value)
        self.x: int = x
        self.y: int = y
        self.shape: Rectangle | Circle = shape
        self.radius: int = 30
        self.connections = []

    def draw(self, surface, font):
        self.shape.draw(surface)

    def draw_text(self, surface, text, font, color=BLACK):
        self.shape.draw_text(surface, text, font, color)

    def draw_outline(self, surface, color=BLACK):
        self.shape.draw_outline(surface, color)







