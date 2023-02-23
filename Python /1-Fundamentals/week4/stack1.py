class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.num_nodes = 0

    def push(self, value):
        new_node = Node(value)

        if self.head is not None:
            new_node.next = self.head

        self.head = new_node
        self.num_nodes += 1 

    def pop(self):
        if self.head is None:
            return None

        pop_node = self.head.value 
        self.head = self.head.next 
        self.num_nodes -= 1 
        return pop_node



stack = Stack()
""" stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Pass" if (stack.num_nodes == 5 ) else "Fail")
stack.push(5)
print("Pass" if (stack.num_nodes == 5 ) else "Fail")

print("Pass" if (stack.pop() == 5) else "Fail")
print("Pass" if (stack.pop() == 4) else "Fail")  """

while True:
    print('push <value>')
    print('pop')
    print('quit')
    my_input = input('what action would you like to perform ?'.split())

    operation = my_input[0].strip().lower()
    if operation == 'push':
        stack.push(int(my_input[1]))
    elif operation == 'pop':
        delval = stack.pop()
        if delval is None:
            print('stack is empty')
        else:
            print('The deleted value is :', int(delval))
    elif operation == 'quit':
        break