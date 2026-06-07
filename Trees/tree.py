
class Node: 
    def __init__(self,value):
        self.value = value 
        self.right = None; 
        self.left = None 
    



def treeCreation(strings,nodeValue=0): 
    value = input(f'Enter the {strings} value of {nodeValue} (-1 for no node)')
    if value == '-1': 
        return None 
    node = Node(value)
    node.left = treeCreation("left node",node.value)
    node.right = treeCreation("right node",node.value)
    return node 

nodevalue = treeCreation("root node")






def traversal(node): 
    if node is  None : 
        return 
    print(node.value)
    traversal(node.left)
    traversal(node.right)

traversal(nodevalue)



