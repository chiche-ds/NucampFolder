class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def iter_linked_list(node):
    while node is not None:
        print(node.value)
        node = node.next




head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")
head.next.next.next = Node("4th Node")
head.next.next.next.next = Node("5th Node")

#Node = ["1st node ","2nd node","3rd node","4th node","5th node", None]

iter_linked_list(head)