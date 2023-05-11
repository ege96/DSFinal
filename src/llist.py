from typing import Union

from node import Node

import pygame

import os

from button import Button

from shape import Shape


class LLNode(Node):

    def __init__(self, data=None):
        super().__init__(data)
        self.next = None


class LList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        """Adds to the end of the LList

        Args:
            val (any): value to add

        """
        node = LLNode(val)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def preadd(self, val):
        """Adds to the front of the LList

        Args:
            val (any): value to add

        """
        node = LLNode(val)
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
