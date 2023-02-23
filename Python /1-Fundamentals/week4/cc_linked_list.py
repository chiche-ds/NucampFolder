class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("head node created: ", self.head.value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        
        node.next = new_node
        print("Appended new Node with value:", node.next.value)


    def prepend(self , value):
        new_node = Node(value)

        if self.head is not None:
            self.head = new_node
            print("Head Node created: ", self.head.value )
            return
        new_node.next = self.head
        self.head = new_node
       # oldhead = self.head
       # self.head = new_node
       # self.head.next = oldhead
        print("Prepend new head with value: ", self.head)







llist = Linkedlist()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")
llist.prepend("First Node")
llist.prepend("insert new first node")