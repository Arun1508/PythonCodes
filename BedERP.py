##########  object from  sizb

class Sizb:


    def __init__(self, length, breadth, height):
        self.length  = length
        self.breadth = breadth
        self.height  = height

    def getLength(self):
        return self.length

    def setLength(self, length):
        self.length = length

    def getBreadth(self):
        return self.breadth

    def setBreadth(self, breadth):
        self.breadth = breadth

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

from pymongo import MongoClient

class SizbDBCall:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.mydb = self.client.SIZB
        self.coll = self.mydb.SiZb1

    def add_data(self, Sizb):
        i = 0
        self.dataa = [{'length':Sizb.length,'breadth':Sizb.breadth,"height":Sizb.height}]
        i = self.coll.insert_many(self.dataa)
        return i

    def display_data(self):
        return self.coll.find()

b = Sizb(12,23,34)
print (b.height)
a = SizbDBCall()
#print(a.add_data(b))
print (a.display_data())
for x in a.display_data():
    print (x)