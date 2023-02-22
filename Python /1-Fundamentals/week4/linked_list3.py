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

llist = Linkedlist()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")