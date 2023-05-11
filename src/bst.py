from typing import Union

from node import Node


class BSTNode(Node):
    def __init__(self, data=None):
        super().__init__(data)
        self.left = None
        self.right = None
        self.level = None



class BSTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        """Adds to the BSTree

        Args:
            val (any): value to add

        """
        new_node = BSTNode(val)

        if self.root is None:
            self.root = new_node
            self.root.level = 0

        else:
            self._add(self.root, new_node, level=1)

    def _add(self, node: BSTNode, new_node: BSTNode, level: int):
        """Helper function for add"""

        if new_node <= node:
            if node.left is None:
                node.left = new_node
                node.left.level = level
            else:
                self._add(node.left, new_node, level+1)

        else:
            if node.right is None:
                node.right = new_node
                node.right.level = level
            else:
                self._add(node.right, new_node, level+1)
                
    def remove(self, val) -> Union[bool, any]:
        """Removes the first instance of val from the BSTree

        Args:
            val (any): value to remove

        Returns:
            Union[bool, any]: None if val is not in BSTree, otherwise the value removed

        """
        if self.root is None:
            return None
        
        self.root = self._remove(self.root, val)
        return val
        
    def _remove(self, node: BSTNode, val) -> BSTNode:
        if node is None:
            return None

        if val < node.value:
            node.left = self._remove(node.left, val)

        elif val > node.value:
            node.right = self._remove(node.right, val)

        else:
            # no children or only right child
            if node.left is None:
                return node.right

            # only left child
            elif node.right is None:
                return node.left

            # two children
            else:
                # find the predecessor
                pred = self._predecessor(node)
                # swap the values
                node.value = pred.value
                # delete the predecessor from the left subtree
                node.left = self._remove(node.left, pred.value)

        return node
                
                
        
    def _predecessor(self, node: BSTNode) -> BSTNode:
        """Returns the predecessor of node, or None if node has no predecessor"""
        
        if node.left is None:
            return None
        
        curr = node.left
        
        # traverse right until we can't anymore
        while curr.right is not None:
            curr = curr.right
            
        return curr
        
        
                
    def level_order(self) -> list:
        if self.root is None:
            return []
        
        queue = [self.root]
        output = []
        
        while queue:
            node = queue.pop(0)
            
            if node is not None:
                output.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
                
        return output

    def __str__(self):

        # level order with new lines
        if self.root is None:
            return "Empty tree"

        queue = [self.root]
        output = ""

        curr_level = 0
        counter = 0

        while queue:
            node = queue.pop(0)

            if node is None:
                output += "X "

            else:
                output += str(node.value) + " "
                queue.append(node.left)
                queue.append(node.right)

            counter += 1

            # add a newline after each level
            if counter == 2**curr_level:
                output += "\n"
                curr_level += 1
                counter = 0

        return output.strip()


if __name__ == "__main__":
    t = BSTree()
    to_add = [5, 2, 3, 7, 10, 6, 4]
    for i in to_add:
        t.add(i)
    print(t)
    print(t.level_order())
    
    to_remove = to_add[::-1]
    for i in to_remove:
        t.remove(i)
        print(t)
        print()
        
    print(t.level_order())
        
    