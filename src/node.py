from dataclasses import dataclass

from .COLORS import *
from .shapes import Rectangle, Circle


@dataclass(order=True)
class Node:
    value: any


@dataclass(order=True)
class VisualNode(Node):
    """A generic node that acts as wrapper for shapes

    Args:
        value (any): The value of the node
        shape (Rectangle | Circle): The shape of the node

    Attributes:
        value (any): The value of the node
        shape (Rectangle | Circle): The shape of the node
    """

    def __init__(self, value, shape: Rectangle | Circle):
        super().__init__(value)
        self.shape: Rectangle | Circle = shape

    def draw(self, surface) -> None:
        """Draws the shape of the node on the surface specified

        Args:
            surface (pygame.Surface): The surface to draw the shape on
            """
        self.shape.draw(surface)

    def draw_text(self, surface, text, font, color=BLACK) -> None:
        """Draws text in the middle of the node

        Args:
            surface (pygame.Surface): The surface to draw the text on
            text (str): The text to draw
            font (pygame.font.Font): The font to use
            color (tuple[int, int, int], optional): The color of the text. Defaults to BLACK.

        """
        self.shape.draw_text(surface, text, font, color)

    def draw_outline(self, surface, color=BLACK) -> None:
        """Draws an outline around the node

        Args:
            surface (pygame.Surface): The surface to draw the outline on
            color (tuple[int, int, int], optional): The color of the outline. Defaults to BLACK.

        """
        self.shape.draw_outline(surface, color)

    def handle_event(self, event):
        """Checks if a click was within the shape"""
        return self.shape.handle_event(event)

    def resize(self, width: int, height: int) -> None:
        """Resizes the shape of the node

        Args:
            width (int): The new width of the shape
            height (int): The new height of the shape

        """
        self.shape.set_width(width)
        self.shape.set_height(height)
        self.update_shape()

    def move(self, x: int, y: int) -> None:
        """Moves the shape of the node

        Args:
            x (int): The new x position of the shape
            y (int): The new y position of the shape

        """
        self.shape.set_x(x)
        self.shape.set_y(y)
        self.update_shape()
