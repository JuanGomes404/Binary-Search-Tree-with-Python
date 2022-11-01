class Node:
    def __init__(self, data):
        self.data = data;
        self.left = None;
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None;
        self.size = 0;
        
    def insertIteratively(self, data):
        newNode = Node(data);
        
        if (self.size == 0):
            self.root = newNode;
            
        currentNode = self.root;
        previousNode = None;
        
        while (currentNode != None):
            previousNode = currentNode;

            if (data < currentNode.data):
                currentNode = currentNode.left;
            elif (data > currentNode.data):
                currentNode = currentNode.right;
        
        if (newNode.data < previousNode.data):
            previousNode.left = newNode;
        else:
            previousNode.right = newNode;
        
    def search(self, data):
        if (self.size == 0):
            return;
        
        self.searchRecursively(data, self.root);
    
    def searchRecursively(self, data, currentNode):
        if (currentNode.data == data):
            return currentNode;
        
        if (data < currentNode.data):
            return self.searchRecursively(data, currentNode.left);
        elif (data > currentNode.data):
            return self.searchRecursively(data, currentNode.right);
        
        return None;
        
        
        
