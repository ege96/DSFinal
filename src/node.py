from dataclasses import dataclass

from ..shapes import *

@dataclass(order=True)
class Node:
    value: any

class VNode: 
    def __init__(self, node: Node, shape: Shape): 
        self.shape = shape
        self.node = node

    def 

