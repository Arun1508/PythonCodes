
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
    
    
    def removeNode(self, rData):
        
        if self.root:
            
            self.removeNodeData(rData, self.root)
            print (" After removel the binary tree looks like ")
            self.traversel()
        else:
            print (" Root node is not present ")
        
    def removeNodeData(self,data,node):
        
        if not node : 
            return node;
        
        if data < node.data:
            
            node.left = self.removeNodeData(data,node.left);
        
        elif data > node.data:
            
            node.right = self.removeNodeData(data, node.right);
        else: 
            
            if not node.left and not node.right:
                
                print(" Deleting the root node ");
                print(" Deleting a leaf node %s" %node.data)
                del node;
                return None;
            
            elif not node.left:
                print(" Removing the node with right child");
                tnode = node.right;
                del node;
                return tnode;
            elif not node.right:
                print(" Removing the node with left child");
                temp = node.left;
                del node;
                return temp;
            
            print (" If the node have two children ");
            temp = self.getPredecessor(node.left)
            node.data = temp.data
            node.left = self.removeNodeData(temp.data, node.left)
            
        return node
            
    def getPredecessor(self, node):
        
        if node.right:
            return self.getPredecessor(node.right);
        return node;
        
            
        
    
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
print ("the max value %s"%bs.getMaxValue())
print ("the min value %s"%bs.getMinValue())
bs.removeNode(9)
print ("the max value %s"%bs.getMaxValue())
print ("the min value %s"%bs.getMinValue())

#bs.inOrderTraversel(bs.root)

        
        
        
                
        
    
        
    