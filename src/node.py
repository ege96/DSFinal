from dataclasses import dataclass

from .shapes import *

@dataclass(order=True)
class Node:
    value: any

class VNode(Node):
    def __init__(self, data, shape: Shape):
        super().__init__(data)
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
        
        
if __name__ == '__main__':
    a = VNode(1, Rectangle())
    print(a)