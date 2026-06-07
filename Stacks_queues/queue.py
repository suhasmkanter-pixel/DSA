class Queue : 
    def __init__(self,limit):
        self.queue = []
        self.limit = limit
    

    def insert_queue(self,value): 
        
        if self.limit == len(self.queue) : 
            print("The limit is over either remove the element or like increase the limit")
            return
        self.queue.append(value)
    
    def pop_queue(self): 
        if len(self.queue) == 0 : 
            print("No element to POP")
            return 
        print(self.queue[0])
        return self.queue.pop(0)
    
    def view_queue(self): 

        print(self.queue)
    

queue = Queue(5)
queue.insert_queue(23)
queue.insert_queue(24)
queue.insert_queue(25)
queue.insert_queue(26)
queue.insert_queue(27)
queue.insert_queue(28)
queue.view_queue()
queue.pop_queue()
queue.pop_queue()