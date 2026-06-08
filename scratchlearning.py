
import numpy as np 
X  =np.array([
    [1,0],
    [0,0],
    [1,0],
    [0,0]
])
Y = np.array([
    [1],
    [0],
    [1],
    [0]
])


W1 = np.random.randn(2,3)
W2 = np.random.randn(3,3)
W3 = np.random.randn(3,3)
W4 = np.random.randn(3,1)
b1 = np.zeros((1,3))
b2 = np.zeros((1,3))
b3 = np.zeros((1,3))
b4 = np.zeros((1,1))


def sigmoid_function(x): 
    return  1/(1 + np.exp(-x))
def sigmoid_derivative(x): 
    return np.exp(-x)/(1 + np.exp(-x)) **2  
     

for epoch in range(10000): 
    Z1 = np.dot(X,W1) + b1 

    a1 = sigmoid_function(Z1)
    Z2 = np.dot(a1,W2) + b2 
    a2 = sigmoid_function(Z2)
    
    Z3 = np.dot(a2,W3) + b3 
    a3 = sigmoid_function(Z3)
  
    Z4 = np.dot(a3,W4) + b4 
    y_pred = sigmoid_function(Z4)
    
    loss = np.mean((y_pred-Y) ** 2)
    #Output Error Delta 
    dZ4 = (y_pred - Y ) * sigmoid_derivative(y_pred)
    dW4 = np.dot(a3.T,dZ4)
    db4 = np.sum(dZ4,axis=0,keepdims=True)

    dZ3 = np.dot(dZ4,W4.T) * sigmoid_derivative(a3)
    dW3 = np.dot(a2.T,dZ3)
    db3 = np.sum(dZ3,axis=0,keepdims=True)

    dZ2 = np.dot(dZ3,W3.T) * sigmoid_derivative(a2)
    dW2 = np.dot(a1.T,dZ2)
    db2 = np.sum(dZ2,axis=0,keepdims=True)

    dZ1 = np.dot(dZ2,W2.T) * sigmoid_derivative(a1)
    dW1 = np.dot(X.T,dZ1)
    db1 = np.sum(dZ1,axis=0,keepdims=True)

    learning_rate = 0.02

    # Update weights
    W4 -= learning_rate * dW4
    W3 -= learning_rate * dW3
    W2 -= learning_rate * dW2
    W1 -= learning_rate * dW1

    # Update biases
    b4 -= learning_rate * db4
    b3 -= learning_rate * db3
    b2 -= learning_rate * db2
    b1 -= learning_rate * db1

    if epoch % 1000  == 0 : 
        print(f"Loss:{loss}, Epoch:{epoch}")

print(y_pred)

