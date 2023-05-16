from typing import Union
import pygame
import random

from .node import VisualNode
from .visualizer import BaseVisualizer

from .COLORS import BLUE, BROWN, BLACK

from .shapes import Shape, Rectangle, Circle


class LLNode(VisualNode):
    def __init__(self, data=None, shape: Rectangle | Circle = None):
        super().__init__(data, shape)
        self.next = None


class LList(BaseVisualizer):
    def __init__(self, surface, font, nodeType=LLNode):
        super().__init__(surface, font, nodeType)

        self.head = None
        self.tail = None
        self.nodeType = nodeType
        self.node_count = 0
        self.total_nodes = 0
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
        self.total_nodes += 1

    def insert_node(self, value, pos):
        """Insert a node with the given value at the specified position in the linked list"""
        if self.head is None:
            self.add(value)
            return

        if pos < 1 or pos > self.node_count + 1:
            print("Invalid position")
            return

        new_node = self.nodeType(value)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for i in range(1, pos - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

            if current_node == self.tail:
                self.tail = new_node

        self.node_count += 1
        self.total_nodes += 1

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

        self.node_count += 1
        self.total_nodes += 1

    def remove_tail(self) -> Union[bool, any]:
        """Removes the tail of the LList
    
        Returns:
            Union[bool, any]: False if LList is empty, otherwise the value removed
    
        """
        if self.head is None:
            return False

        self.node_count -= 1


        if self.head == self.tail:
            temp_value = self.head.value
            self.head = None
            self.tail = None
            return temp_value

        node = self.head
        while node.next.next:
            node = node.next

        temp_value = node.next.value
        node.next = None
        self.tail = node

        return temp_value

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
                self.node_count -= 1
                return temp_node.value

            node = node.next

        return False

    def remove_at(self, pos) -> Union[bool, any]:
        """Removes the node at the specified position in the linked list
        
        Args:
            pos (int): position of the node to remove
            
        Returns:
            Union[bool, any]: False if LList is empty or pos is invalid, otherwise the value removed"""
        if self.head is None:
            return False

        if pos < 1 or pos > self.node_count + 1:
            return False

        self.node_count -= 1

        if pos == 1:
            temp_value = self.head.value
            self.head = self.head.next
            return temp_value

        current_node = self.head

        for i in range(1, pos - 1):
            current_node = current_node.next

        temp_value = current_node.next.value
        current_node.next = current_node.next.next

        if current_node.next is None:
            self.tail = current_node

        return temp_value

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

    def setup(self):
        btn_names = ["add", "preadd", "insert", "search", "exit"]
        self.add_buttons(btn_names)

    def _buttonMenu(self, event):
        for btn in self.btns:
            btn_obj = self.btns[btn]
            btn_obj.draw(self.surface, width=2)
            btn_obj.draw_text(self.surface, btn.capitalize(), self.font, BLACK)

            if btn_obj.handle_event(event):
                match btn:
                    case "add":
                        self.add(self.total_nodes + 1)
                    case "preadd":
                        self.preadd(self.total_nodes + 1)
                    case "insert":
                        self.insert_node(self.total_nodes + 1, random.randint(1, self.node_count + 1))
                    case "search":
                        pass
                    case "exit":
                        return "exit"

    def _visualize(self, event):
        self.surface.fill(BLUE)

        if self._buttonMenu(event) == "exit":
            return "exit"

        curr = self.head

        x = self.surface.get_width() // 10
        y = self.surface.get_height() // 5

        prevNode = None
        pos = 1

        radius: int = 30
        x_inc = y_inc = int(radius * 2.5)

        while curr is not None:
            changed_level = False

            if x >= self.surface.get_width() - radius:
                changed_level = True
                # draw line from prevNode to right screen
                pygame.draw.line(self.surface, BLACK, (x-(x_inc-radius), y), (self.surface.get_width(), y), 2)

                # reset x and y
                x = self.surface.get_width() // 10
                y += y_inc

                # draw line from left screen to curr
                pygame.draw.line(self.surface, BLACK, (0, y), (x-radius, y), 2)

            curr.shape = Circle((x, y), BROWN, radius)
            curr.move(x, y)

            # update position
            x += x_inc
            pos += 1

            curr.draw(self.surface)
            curr.draw_text(self.surface, str(curr.value), self.font, BLUE)
            curr.draw_outline(self.surface, BLACK)

            if curr.shape.handle_event(event):
                if event.button == 1:
                    self.remove_at(pos-1)
                    if self.node_count == 0:
                        self.total_nodes = 0
                elif event.button == 3:
                    self.insert_node(self.node_count + 1, pos)

            if prevNode is not None:
                # draw line
                n1 = prevNode
                n2 = curr

                # edge of n1
                x1 = n1.shape.pos[0] + n1.shape.radius
                y1 = n1.shape.pos[1]

                # edge of n2
                x2 = n2.shape.pos[0] - n2.shape.radius
                y2 = n2.shape.pos[1]

                if changed_level is False:
                    pygame.draw.line(self.surface, BLACK, (x1, y1), (x2, y2), 2)

            prevNode = curr
            curr = curr.next

        pygame.display.update()
