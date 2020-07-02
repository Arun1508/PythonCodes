# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:31:39 2019

@author: ArunMukesh
"""

class ANode:
    
    def __init__(self,data):
        
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
        
class AVLTree:
    
    def __init__(self):
        
        self.root = None
        
    def calcHeight(self, node):
        
        if not node:
            
            return -1
        
        return node.height
    
    def calcBalance(self, node):
        
        if not node:
            
            return 0
        
        return self.calcHeight(node.left) - self.calcHeight(node.right)
    
    
