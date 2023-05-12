from typing import Union

from .llist import LList

class Queue(LList):
    def __init__(self):
        super().__init__()
        
    def enqueue(self, val):
        """Adds to the end of the Queue
        
        Args:
            val (any): value to add
            
        """
        self.add(val)
        
    def pop(self) -> Union[bool, any]:
        """Removes the first value in the Queue
        
        Returns:
            Union[bool, any]: False if Queue is empty, otherwise the value removed
            
        """
        if not self.head:
            return False
        else:
            val = self.head.value
            self.head = self.head.next
            return val
        
    def peek(self) -> Union[bool, any]:
        """Returns the first value in the Queue
        
        Returns:
            Union[bool, any]: False if Queue is empty, otherwise the first value
            
        """
        return super().peek()
    
    def is_empty(self) -> bool:
        """Returns True if Queue is empty, False otherwise"""
        return super().is_empty()
    
    
if __name__ == "__main__":
    # make Queue
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    print(q.is_empty())
    print(q.peek())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q)
    
    