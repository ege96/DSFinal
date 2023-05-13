from .llist import LList

class Stack(LList):
    def __init__(self):
        super().__init__()
        
    def push(self, val):
        """Adds to the top of the Stack
        
        Args:
            val (any): value to add
            
        """
        self.preadd(val)
        
    def pop(self):
        """Removes the top value in the Stack
        
        Returns:
            Union[bool, any]: False if Stack is empty, otherwise the value removed
            
        """
        if self.head is None:
            return False
        
        return self.remove(self.peek())
    
    
    def peek(self):
        """Returns the top value in the Stack
        
        Returns:
            Union[bool, any]: False if Stack is empty, otherwise the top value
            
        """
        return super().peek()
    
    def is_empty(self) -> bool:
        """Returns True if Stack is empty, False otherwise"""
        return super().is_empty()

    
    
    
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.pop())