# Problem Statement: Check Balanced Parentheses. Given string str containing just the characters '(', ')', '{', '}', '[' and ']', check if the input string is valid and return true if the string is balanced otherwise return false. .
# Example 1:
# Input: str = “( )[ { } ( ) ]”
# Output: True
# Explanation: As every open bracket has its corresponding close bracket. Match parentheses are in correct order hence they are balanced.


parenthesesString = '()[]'


stack = []
stackvalues = {
    ")": "(",
    "}": "{",
    "]": "["
}
def parenthese_checker(parenthesesString): 
    if len(parenthesesString) % 2 == 1 : 
         return False 

    for parentheses in parenthesesString: 
        
        if parentheses in ["(","{","["]: 
          stack.append(parentheses)
        else : 
            poppedvalue = stack.pop()
            print(poppedvalue,stackvalues[parentheses])
            if poppedvalue != stackvalues[parentheses]: 
                    print("Not in sequence")
                    return False 
    
    return len(stack) == 0 
       

if parenthese_checker(parenthesesString=parenthesesString) : 
     print("It is a Correct Sequence")
else:
    print("It is not a correct Sequence")

    #    if  (ord(parentheses) - ord(poppedvalue)) !=  1 and  (ord(parentheses)-ord(poppedvalue)) != 2: 
    #         print("The parentehesis are not in Sequence")
    #         break  
            




