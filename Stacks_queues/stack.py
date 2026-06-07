
class Stack: 
    def __init__(self,limit):
        self.stack = []
        self.limit = limit
    

    def insert_data(self,value): 
        if (len(self.stack) == self.limit):
             print("The Stack is full either pop the last element or extend the limit")
             return  
        self.stack.append(value)
    
    def delete_data(self):
        if len(self.stack) == 0 : 
            print("No elements to Pop")
            return 
    
        return self.stack.pop()
    
    def view_data(self): 
        print(self.stack)
    
    def peak_stack(self):  
        print(self.stack[-1])

    


stack = Stack(4)
stack.insert_data(12)
stack.insert_data(34)
stack.insert_data(45)
stack.insert_data(23)
stack.insert_data(55)
stack.view_data()
stack.delete_data()
stack.delete_data()
stack.view_data()