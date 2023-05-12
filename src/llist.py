from typing import Union

from .node import Node, VNode

from .shapes import *


class LLNode(Node):
    def __init__(self, data=None):
        print(data)
        super().__init__(data)
        self.next = None
        
class LLVNode(VNode, LLNode):
    def __init__(self, data=None, shapeType: Shape = None):
        super().__init__(data, shapeType)
        self.shape = shapeType()
        
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
    def __init__(self, screen_x:int, screen_y:int, nodeType=LLVNode):
        super().__init__(nodeType)
        self.screen_x = screen_x
        self.screen_y = screen_y
        
    def add(self, val, shape: Shape):
        super().add(val, shape)
        
    def preadd(self, val, shape: Shape):
        super().preadd(val, shape)
        
    def remove(self, val):
        super().remove(val)
                
    def update_shapes(self):
        node = self.head
        x = self.screen_x
        y = self.screen_y
        while node:
            node.move(x, y)
            x += node.shape.rect.width
            node = node.next            
    
    def draw(self, surface):
        node = self.head
        while node:
            node.draw(surface)
            node = node.next
    
    def handle_event(self, event):
        node = self.head
        while node:
            if node.handle_event(event):
                # do something later
                return True
            node = node.next
        return False
        
        
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
