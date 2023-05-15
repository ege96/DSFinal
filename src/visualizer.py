import pygame.font
import pygame.event
from .shapes import Rectangle
from .COLORS import *
from abc import ABC, abstractmethod


class BaseVisualizer(ABC):
	def __init__(self, surface, font, node_type,
				 button_pos=(10, 10),
				 button_height=40,
				 button_width=150,
				 button_spacing=5):
		self.node_type = node_type
		self.surface = surface
		self.font = font
		self.button_pos = button_pos
		self.button_height = button_height
		self.button_width = button_width
		self.button_spacing = button_spacing
		self.btns = {}

	@abstractmethod
	def setup(self):
		pass

	def add_buttons(self, names):
		start_x, start_y = self.button_pos
		button_positions = [(start_x + i * (self.button_width + self.button_spacing), start_y) for i in
							range(len(names))]
		for name, position in zip(names, button_positions):
			rect = Rectangle(position, BLACK, self.button_width, self.button_height)
			rect.draw_text(self.surface, name.title(), self.font, BLACK)
			self.btns[name] = rect

	@abstractmethod
	def _buttonMenu(self, event):
		pass

	# @abstractmethod
	# def _draw(self):
	# 	pass

	def visualize(self):
		self.setup()
		while True:
			for event in pygame.event.get():
				if self._visualize(event) == "exit":
					return

	@abstractmethod
	def _visualize(self, event):
		pass
