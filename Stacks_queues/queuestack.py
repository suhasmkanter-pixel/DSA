class Stack: 
    def __init__(self):
        self.stack = []   # Input stack
        self.stack2 = []  # Output stack

    def add_element(self, value): 
        self.stack.append(value)
    
    def delete_element(self): 
        # If BOTH stacks are empty, the queue is empty
        if len(self.stack) == 0 and len(self.stack2) == 0: 
            print("No elements there to pop")
            return 
        
        # ONLY move elements if stack2 is completely empty
        if len(self.stack2) == 0:
            while len(self.stack) > 0:
                self.stack2.append(self.stack.pop())
                
        # Pop directly from stack2 (it holds elements in correct FIFO order)
        return self.stack2.pop()
     
    def top_view(self): 
        # Peek needs to look at the next item to be deleted
        if len(self.stack2) == 0:
            while len(self.stack) > 0:
                self.stack2.append(self.stack.pop())
                
        if len(self.stack2) > 0:
            print(self.stack2[-1]) # Look at top of stack2


stack = Stack()
for i in range(100000): 
    stack.add_element(i)
for i in range(99999): 
   print(    stack.delete_element()
)