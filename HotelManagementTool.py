class Rooms1:
    rooms = {}
    def __init__(self,room_no,Customer):
        self.room_no = room_no
        self.Customer = Customer


    def add_room(self):
        if self.room_no not in self.rooms.keys():
            self.rooms[self.room_no]=self.Customer
            print ("Room assigned successfully")
        else :
            print ("Rooms Already in use")

    def show_avble_rooms(self):
        for x in self.rooms.keys():
            print ('the Room no '+str(x)+" and the customer {}".format(self.rooms[x].get_address()))



class Customer:

    def __init__(self,name,address):
        self.name = name
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address


a = Customer('Arun','Chennai')
b = Customer('Sam','Mumbai')

aa = Rooms1(101,a)
aa.add_room()
aa.show_avble_rooms()

aa = Rooms1(102,b)
aa.add_room()
aa.show_avble_rooms()












