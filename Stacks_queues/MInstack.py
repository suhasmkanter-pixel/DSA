
instruction = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]  
values = [ [], [-2], [0], [-3], [ ], [ ], [ ], [ ] ] 



print(values[0])

instructionSet = []


      

pop =  0 
minimum = 99999999
for index,i in enumerate(instruction):
    match i : 
          case 'MinStack' : 
               instructionSet.append(["null"])
          case 'push' : 
                instructionSet.append(values[index])
        
          case 'pop' : 
                instructionSet.append(['null'])
                pop += 1 
        #   case 'top': 
        #        tempValue = pop 
        #        for i in range(len(instruction)-1,-1): 
        #             if type(instructionSet[i]) == 'number' and tempValue == 0 : 
        #                   instructionSet.append() 
        #             else: 
        #                   tempValue -= 1 


print(instructionSet)