import math 
from treenode import Node 
X = [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [6.2, 3.4, 5.4, 2.3],
    [5.9, 3.0, 5.1, 1.8],
    [5.5, 2.3, 4.0, 1.3],
    [6.5, 2.8, 4.6, 1.5]
]

y = [
    0,  # Setosa
    0,
    2,  # Virginica
    2,
    1,  # Versicolor
    1
]



def split_dataset(X,y,feature,thresholds):
    leftX =[]
    leftY=[]
    rightX =[]
    rightY =[]

    for i in range(len(X)):
        if X[i][feature] < thresholds:
            leftX.append(X[i])
            leftY.append(y[i])
        else:
            rightX.append(X[i])
            rightY.append(y[i])
    return leftX,leftY,rightX,rightY

def entropy(labels):
    total = len(labels) 
    if total == 0 : 
        return 0 
    counts = {}

    for label in labels: 
        counts[label] = counts.get(label,0) +1

    ent = 0 
    for count in counts.values(): 
        p = count/total
        ent -= p * math.log2(p)
    return ent


def information_gain(parent_y, left_y, right_y):
    parent_entropy =  entropy(parent_y)
    total = len(parent_y)
    left_weight = len(left_y)/total 
    right_weight = len(right_y)/total
    child_entropy = (
        left_weight * entropy(left_y)
        +
        right_weight * entropy(right_y)
    )
    return parent_entropy - child_entropy
def best_split(X,y): 
    best_gain = -1
    best_feature = None
    best_threshold = None
    for feature in range(len(X[0])): 
        value = [row[feature] for row in X ]
        for thresholds in value:
           left_X,left_y,right_X,right_y= split_dataset(X,y,feature,thresholds)
           gain = information_gain(
               y,left_y,right_y
           )
           if gain > best_gain  :
                print("Gain:",gain,"Best Feature:",feature,"Best Threshold:",thresholds)
                best_gain = gain 
                best_feature = feature 
                best_threshold = thresholds

    return best_feature,best_threshold
feature, threshold = best_split(X,y)

def build_tree(X,y,depth=0,max_depth=4): 
      
      if len(X) == 0 or len(y) == 0 : 
          return 
    
      unique_labels = set(y)
      if len(unique_labels) == 1 : 
          return Node(value=y[0])
      
      if depth >= max_depth: 
          majority = max(unique_labels,key=y.count)
          return Node(value=majority)
     
      feature,threshold = best_split(X,y)
      
      print(feature,threshold)
      if feature is None : 
          majority = max(unique_labels,key=y.count)
          return Node(value=majority)
      left_X,left_Y, right_X,right_Y = split_dataset(X,y,feature,threshold)
 
      print("Left Value:",left_X,)

      left_child = build_tree(
          left_X,
          left_Y,
          depth+1,
          max_depth
      )

      right_child = build_tree(
          right_X,
          right_Y,
          depth+1,
          max_depth
      )
      return Node(
          feature = feature,
          threshold=threshold,
          left= left_child,
          right= right_child
      )

tree = build_tree(X,y)


def predict(node, sample):

    if node.value is not None:
        return node.value

    if sample[node.feature] <= node.threshold:
        return predict(node.left, sample)

    return predict(node.right, sample)

person =   [5.9, 4.0, 5.1, 1.8]

def print_tree(node, depth=0):
    if node is None:
        return

    print("  " * depth, end="")

    if node.value is not None:
        print(f"Leaf: {node.value}")
        return

    print(f"Feature {node.feature} < {node.threshold}")

    print_tree(node.left, depth + 1)
    print_tree(node.right, depth + 1)
# print_tree(tree)