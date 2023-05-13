from typing import Union
import pygame

from .llist import LList, LLNode
from .COLORS import BLUE, BROWN, BLACK
from .shapes import Shape, Rectangle


class Stack(LList):
    def __init__(self, surface, font, nodeType=LLNode):
        super().__init__(surface, font, nodeType)
        self.rect_width = 120
        self.rect_height = 40
        self.rect_spacing = 5
        surface_x, surface_y = surface.get_size()
        self.stack_pos = (surface_x//2 - self.rect_width//2, surface_y - self.rect_height*2)
        self.button_pos = (10, 10)
        self.button_height = 40
        self.button_width = 150
        self.button_spacing = 5

    def push(self, val):
        """Adds an element to the top of the stack.

        Args:
            val (any): Value to add to the stack.

        """
        self.add(val)

    def pop(self) -> Union[bool, any]:
        """Removes and returns the element at the top of the stack.

        Returns:
            Union[bool, any]: False if the stack is empty, otherwise the value at the top of the stack.

        """
        return self.remove_tail()

    def top(self):
        """Returns the element at the top of the stack without removing it.

        Returns:
            Union[bool, any]: False if the stack is empty, otherwise the value at the top of the stack.

        """
        if self.tail is None:
            return False
        return self.tail.value
    
    def setup(self):
        start_x, start_y = self.button_pos
        
        self.add_btn = Rectangle((start_x, start_y), BLACK, self.button_width, self.button_height)
        self.add_btn.draw_text(self.surface, "Push", self.font, BLACK)
        
        start_x += self.button_width + self.button_spacing
        
        self.insert_btn = Rectangle((start_x, start_y), BLACK, self.button_width, self.button_height)
        self.insert_btn.draw_text(self.surface, "Pop", self.font, BLACK)

        start_x += self.button_width + self.button_spacing

        self.exit_btn = Rectangle((start_x, start_y), BLACK, self.button_width, self.button_height)
        self.exit_btn.draw_text(self.surface, "Exit", self.font, BLACK)
        
        self.btns = {"push": self.add_btn, "pop": self.insert_btn, "exit": self.exit_btn}
        

    def visualize(self):
        self.setup()
        while True:
            for event in pygame.event.get():
                if self._visualize(event) == "exit":
                    return
                
    def _buttonMenu(self, event):
        for btn in self.btns:
            btn_obj = self.btns[btn]
            btn_obj.draw(self.surface, width=2)
            btn_obj.draw_text(self.surface, btn.capitalize(), self.font, BLACK)

            if btn_obj.handle_event(event):
                if btn == "push":
                    self.push(self.node_count + 1)
                elif btn == "pop":
                    self.pop()
                elif btn == "exit":
                    return "exit"

    def _visualize(self, event):
        self.surface.fill(BLUE)

        if self._buttonMenu(event) == "exit":
            return "exit"

        curr = self.head

        x, y = self.stack_pos

        while curr is not None:
            rect = Rectangle((x, y), BROWN, self.rect_width, self.rect_height)
            curr.shape = rect
            curr.update_shape()
            curr.draw(self.surface)
            curr.draw_text(self.surface, str(curr.value), self.font, BLACK)

            if curr.shape.handle_event(event):
                self.remove_tail()

            curr = curr.next
            y -= self.rect_height + self.rect_spacing

        pygame.display.update()
