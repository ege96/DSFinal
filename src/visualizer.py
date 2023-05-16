from abc import ABC, abstractmethod

import pygame
import pygame.event
import pygame.font

from .COLORS import *
from .shapes import Rectangle


class BaseVisualizer(ABC):
	def __init__(self, surface: pygame.Surface, font: pygame.font.Font, node_type=None,
				 button_pos=(10, 10),
				 button_height=40,
				 button_width=150,
				 button_spacing=5):

		self.node_type = node_type
		self.surface: pygame.Surface = surface
		self.font: pygame.font.Font = font
		self.button_pos: tuple[int, int] = button_pos
		self.button_height: int = button_height
		self.button_width: int = button_width
		self.button_spacing: int = button_spacing
		self.btns: dict[str, Rectangle] = {}

	@abstractmethod
	def setup(self):
		pass

	def add_buttons(self, names) -> None:
		"""Adds buttons to the visualizer

		Args:
			names (list[str]): list of names of the buttons

		"""
		start_x, start_y = self.button_pos
		button_positions = [(start_x + i * (self.button_width + self.button_spacing), start_y) for i in range(len(names))]
		for name, position in zip(names, button_positions):
			rect = Rectangle(position, BLACK, self.button_width, self.button_height)
			rect.draw_text(self.surface, name.title(), self.font, BLACK)
			self.btns[name] = rect

	@abstractmethod
	def _buttonMenu(self, event):
		pass

	def visualize(self):
		self.setup()
		while True:
			for event in pygame.event.get():
				if self._visualize(event) == "exit":
					return

	@abstractmethod
	def _visualize(self, event):
		pass
