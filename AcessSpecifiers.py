class Trial:
    def __init__(self):
        self.name = 'Arun'####         pubile
        self._age = 23    ####         protected  - can't be called directly from object
        self.__adderss = 'Chennai'#    private    - can't be called directly from obbject

    def set_age(self, no):
        self._age = no
        print ("from set function Age "+str(self._age))

    def getname(self):
        return self.name

    def getage(self):
        return self._age

    def getaddress(self):
        return self.__adderss

    def print_data(self):
        print ("The name "+self.name+" age "+str(self._age)+" Address "+self.__adderss)


a = Trial()
print (a.getaddress())
a.set_age(20)


class Trials1(Trial):
    def Print_data1(self):
        print (self.getaddress())

b = Trials1()
b.Print_data1()
b.set_age(30)