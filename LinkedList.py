class Node:


    def __init__(self,data = None, next_node = None):
        self.data = data
        print (" int node constructor "+str(self.data))
        self.next_node = next_node
        #print ("data")
        #print (data)
        #print ("Node")
        #print (next_node)


    def get_data (self):
        #print ("In return ")
        #print (self.data)
        return self.data

    def set_data (self, data):
        #print ("Set the data")
        self.data = data

    def get_next_node(self):
        return self.next_node


    def set_next_node(self, new_node):
        self.next_node = new_node

##################    Linked List   ########################################

class LinkedList:

    def __init__(self, head = None):
        self.head = head

    def insert_node(self,node):
        new_node = node
        new_node.set_next_node(self.head)
        self.head = new_node

    def SizeOfNode(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            #print(curr_node.get_data())
            ##print (curr_node.get_next_node())
            curr_node = curr_node.get_next_node()
        return count

    def SearchNode(self,data):
        cur_node = self.head
        while cur_node:
            print ("Searching node")
            print (cur_node.get_data())
            if cur_node.get_data() == data:
                return True
            else:
                cur_node = cur_node.get_next_node()

            if cur_node is None :
                return False

    def get_node(self,data):
        cur_node = self.head
        while cur_node:
            print (cur_node.data)
            if cur_node.data == data:
                return cur_node
            print ("Assigning the nex one ")
            cur_node = cur_node.next_node
        return None

    def delete_current_node (self, cur_node):

        real_node = self.head
        while True:
            if real_node.get_data() == cur_node.get_data():
                print ("match found")
                print (real_node.get_data())
                print ("deleting the node ")
                print ("before deleting node  ")
                print (real_node.get_data())
                temp = real_node.get_next_node()
                real_node.set_data( temp.get_data() )
                real_node.set_next_node( temp.get_next_node())
                print ("After change setting new node")
                print (real_node.get_data())
                break
            elif real_node.get_next_node() != None:
                print ("didn't match ")
                real_node = real_node.get_next_node()
            else :
                break

    def delete_without_header(self,node):
        print (node.data)
        if (node.next_node) != None:
            node.set_data(node.next_node.get_data)
            node.node = node.next_node.next_node
        print (node.data)


ls = LinkedList()
ls.insert_node(Node(123))
ls.insert_node(Node(456))
ls.insert_node(Node(789))
print("Node Size")
print(ls.SizeOfNode())
print (ls.SearchNode(456))
print (" the deleting ")
#ls.delete_current_node(Node(456))
ls.delete_without_header(ls.get_node(123))
print("Searching the deleted node")
print (ls.SearchNode(123))
