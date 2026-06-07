# implement stack using the queue 

from collections import deque


class Queue : 
    def __init__(self):
        self.queue1= deque()
        self.queue2 = deque() 

    def add_element(self,value): 
   

        self.queue1.append(value)
    
    def delete_element(self): 
         popped_Value = 0
         while len(self.queue1) >= 1 : 
              if len(self.queue1) == 1:
                  popped_Value =  self.queue1.popleft()
              else:
                self.queue2.append(self.queue1.popleft())

         
         while len(self.queue2) >= 1: 
               self.queue1.append(self.queue2.popleft())
               print(self.queue1,"Queue1")
               print(self.queue2,"Queue2")
         return popped_Value
      
         
    
    def top_view(self): 
        pass 

queue = Queue()
queue.add_element(1)
queue.add_element(2)
queue.add_element(3)
queue.add_element(4)
queue.add_element(5)
print(queue.delete_element())
print(queue.delete_element())