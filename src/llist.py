from typing import Union

from .node import Node, VNode

from .shapes import *

import random
import time


class LLNode(Node):
    def __init__(self, data=None):
        super().__init__(data)
        self.next = None
        
class LLVNode(VNode, LLNode):
    def __init__(self, data=None, shape: Shape = None):
        super().__init__(data, shape)
        self.shape = shape
        
    def get_x(self):
        return self.shape.get_x()
    
    def get_y(self):
        return self.shape.get_y()
    
    def get_width(self):    
        return self.shape.get_width()
        
    def draw(self, surface):
        self.shape.draw(surface)
        
    def draw_text(self, surface, text, font, font_color):
        self.shape.draw_text(surface, text, font, font_color)
        
    def update_shape(self):
        self.shape.update_rect()
        
    def handle_event(self, event):
        return self.shape.handle_event(event)
    
    def resize(self, width, height):
        self.shape.set_width(width)
        self.shape.set_height(height)
        self.update_shape()
        
    def move(self, x, y):
        self.shape.set_x(x)
        self.shape.set_y(y)
        self.update_shape()        

class LList:
    
    def __init__(self, nodeType=LLNode):
        self.head = None
        self.tail = None
        self.nodeType = nodeType

    def add(self, val, **kwargs):
        """Adds to the end of the LList

        Args:
            val (any): value to add

        """
        node = self.nodeType(val, **kwargs)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def preadd(self, val, **kwargs):
        """Adds to the front of the LList

        Args:
            val (any): value to add

        """
        node = self.nodeType(val, **kwargs)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node

    def remove(self, val) -> Union[bool, any]:
        """Removes the first instance of val from the LList

        Args:
            val (any): value to remove

        Returns:
            Union[bool, any]: False if val is not in LList, otherwise the value removed

        """
        if self.head is None:
            return False

        temp_node = self.head

        if self.head.value == val:
            self.head = self.head.next
            return temp_node.value

        node = self.head
        while node.next:
            temp_node = node.next
            
            if node.next.value == val:
                node.next = node.next.next
                return temp_node.value
            
            node = node.next
            
        return False

    def peek(self):
        """Returns the first value in the LList

        Returns:
            Union[bool, any]: False if LList is empty, otherwise the first value

        """
        if self.head is None:
            return False

        return self.head.value

    def is_empty(self):
        """Returns True if LList is empty, False otherwise"""
        return self.head is None

    def __str__(self) -> str:
        node = self.head
        output = []
        while node:
            output.append(str(node.value))
            node = node.next

        output.append("None")
        return "->".join(output)
    
    
class LListVisualizer(LList):
    def __init__(self, screen_x:int, screen_y:int, surface, nodeType=LLVNode):
        super().__init__(nodeType)
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.surface = surface
        self.setup()
        
        
    def add(self, val):
        """Adds to the end of the LList

        Args:
            val (any): value to add

        """
        
        node = self.nodeType(val, shape=Circle((0,0), (0, 255, 255), 10))
        if not self.head:
            node.move(0 + node.get_width(), self.screen_y//2)
            self.head = node
        else:
            node.move(self.tail.shape.pos[0] + self.tail.shape.rect.width*2, self.tail.shape.pos[1])
            self.tail.next = node
            
        self.tail = node

    def preadd(self, val, **kwargs):
        """Adds to the front of the LList

        Args:
            val (any): value to add

        """
        node = self.nodeType(val, **kwargs)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node

    def remove(self, val) -> Union[bool, any]:
        """Removes the first instance of val from the LList

        Args:
            val (any): value to remove

        Returns:
            Union[bool, any]: False if val is not in LList, otherwise the value removed

        """
        if self.head is None:
            return False

        temp_node = self.head

        if self.head.value == val:
            self.head = self.head.next
            return temp_node.value

        node = self.head
        while node.next:
            # change color of node
            temp_node = node.next
            
            if node.next.value == val:
                node.next = node.next.next
                return temp_node.value
            
            node = node.next
            
        return False
                
    def update_shapes(self):
        node = self.head
        x = self.screen_x
        y = self.screen_y
        while node:
            node.move(x, y)
            x += node.shape.rect.width
            node = node.next            
    
    def draw(self):
        node = self.head
        while node:
            print("Drawing node", node.value, "at", node.shape.pos)
            
            node.draw(self.surface)
            node.draw_text(self.surface, str(node.value), self.font, self.font_color) 
            # draw arrow
            if node.next:
                next_node = node.next
                pygame.draw.line(self.surface, (0, 255, 255), (node.get_x() + node.get_width()//2, node.get_y()), (next_node.get_x() - next_node.get_width()//2, next_node.get_y()))
            node = node.next
            pygame.display.update()
            
        
    
    def handle_event(self, event):
        node = self.head
        while node:
            if node.handle_event(event):
                # do something later
                return True
            node = node.next
        return False
    
    def visualize(self, event):
        # handle events
        self.draw()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.add(random.randint(0, 100))
            
    def setup(self):
        self.surface.fill((155, 196, 203))
        self.font = pygame.font.SysFont("Arial", 10)
        self.font_color = (0, 0, 0)
        
        
        
    
        
        
        
        
if __name__ == "__main__":
    # make LList
    list = LList()

    list.add(1)
    list.add(2)
    list.preadd(3)

    print(list)

    list.remove(3)
    print(list)
    list.remove(2)
    print(list)
    list.remove(1)
    print(list)
