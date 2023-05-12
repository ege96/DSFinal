from typing import Union
import pygame

from .node import Node

from .COLORS import BLUE, BROWN, BLACK

from .shapes import Shape


class LLNode(Node):
    def __init__(self, data=None, shape: Shape=None):
        super().__init__(data)
        self.next = None
        self.shape = shape

    def draw(self, surface):
        self.shape.draw(surface)
        
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
    def __init__(self, surface, font, nodeType=LLNode):
        self.head = None
        self.tail = None
        self.nodeType = nodeType
        self.node_count = 0    
        self.surface = surface
        self.font = font

    def add(self, val):
        """Adds to the end of the LList

        Args:
            val (any): value to add

        """
        node = self.nodeType(val)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        
        self.node_count += 1

    def insert_node(self, value, pos):
        """Insert a node with the given value at the specified position in the linked list"""
        if pos < 1 or pos > self.node_count + 1:
            print("Invalid position")
            return

        new_node = Node(value)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for i in range(1, pos-1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

        self.node_count += 1
    
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

    def display(self):
        current = self.head
        x = 100
        y = 250

        while current:
            current.position = (x, y)
            pygame.draw.circle(self.surface, BROWN, [x, y], 30)
            text = self.font.render(str(current.value), True, BLUE)
            text_rect = text.get_rect(center=(x, y))
            self.surface.blit(text, text_rect)
            pygame.draw.circle(self.surface, BLACK, [x, y], 30, 2)

            # Draw an arrow from the current node to the next node (if there is one)
            if current.next:
                pygame.draw.line(self.surface, BLACK, [x + 30, y], [x + 50, y], 2)
                pygame.draw.polygon(self.surface, BLACK, [(x + 50, y - 5), (x + 50, y + 5), (x + 60, y)], 0)

            x += 80
            current = current.next 
            
    def __str__(self) -> str:
        node = self.head
        output = []
        while node:
            output.append(str(node.value))
            node = node.next

        output.append("None")
        return "->".join(output)

    def 

    
    
        
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
