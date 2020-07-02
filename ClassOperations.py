# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 08:24:18 2019

@author: ArunMukesh
"""

class FirstName:
    
    def __init__(self, data):
        self.data = data
        
class Name :
    
    def __init__(self):
        
        self.name = None
        
    def addName(self, data):
        
        self.name = FirstName(data)
        
        print (self.name)
        
n = Name()

n.addName("sam")

        