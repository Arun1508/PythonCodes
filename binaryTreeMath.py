
class Node:
    
    def __init__(self,data):
        
        self.data = data
        self.left = None
        self.right = None
        

class BinarySearcgAlg:
    
    def __init__(self):
        
        self.root = None

    def binaryInsert(self, data):
        

        if not self.root:
            
            self.root = Node(data)
        else :
            
            self.binaryLeafInsert(data, self.root)
            
            
    def binaryLeafInsert(self,data, node):
        
    
        if node.data > data:
            
            if node.left:
                
                self.binaryLeafInsert(data,node.left)
            else :
                
                node.left = Node(data)
                
        elif node.data < data:
            
            if node.right :
                
                self.binaryLeafInsert(data,node.right)
                
            else :
                
                node.right = Node(data)
        #print (self.root.data)
          
    def traversel(self):
        
        if self.root:
            return self.traversalNode(self.root)
        
    def traversalNode(self, node):
        
        if node.left:
            self.traversalNode(node.left)
        
        print ("The node is %s" %node.data)
        
        if node.right:
            self.traversalNode(node.right)
        
    def inOrderTraversel(self, node):
        
        if node:
            self.inOrderTraversel(node.left)
            print (node.data)
            self.inOrderTraversel(node.right)
    
    def getMaxValue(self):
        
        if self.root:
            return self.maxValue(self.root)
        
    def maxValue(self, node):
        
        if node.right:
            return self.maxValue(node.right)
        
        return node.data
    
    def getMinValue(self):
        
        if self.root:
            return self.minValue(self.root)
        
    def minValue(self, node):
        
        if node.left:
            return self.minValue(node.left)
        
        return node.data
    
            
        
    
bs = BinarySearcgAlg()

bs.binaryInsert(5)
bs.binaryInsert(3)
bs.binaryInsert(4)
bs.binaryInsert(2)
bs.binaryInsert(7)
bs.binaryInsert(8)
bs.binaryInsert(6)
bs.binaryInsert(1)
bs.binaryInsert(9)
bs.binaryInsert(10)
bs.traversel()
       
        
        
                
        
    
        
def evalExpressionTree(root):
    
    if root:
        
        evalExpressionTree(root.left);
        if root.left.data.isnumber() and root.right.data.isnumber():
            if root.data == "+":
                root.data = int(root.left.data) + int(root.right.data)
                root.left, root.right = None
            elif root.data == "-":
                root.data = int(root.left.data) - int(root.right.data)
                root.left, root.right = None
            elif root.data == "*":
                root.data = int(root.left.data) * int(root.right.data)
                root.left, root.right = None
            elif root.data == "/":
                root.data = int(root.left.data) / int(root.right.data)
                root.left, root.right = None
        evalExpressionTree(root.right)
            
            
        evalExpressionTree(root.right);