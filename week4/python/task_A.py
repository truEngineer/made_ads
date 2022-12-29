class Node:
 
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        # min at the moment of adding of the element
        self.this_min = None
 
 
class Stack:
 
    def __init__(self):
        self.tail = None
 
    def insert(self, value):
        if self.tail is None:
            self.tail = Node(value)
            self.tail.this_min = value
        else:
            new_node = Node(value)
            new_node.prev = self.tail
            new_node.this_min = min(self.tail.this_min, value)
            self.tail = new_node
 
    def erase_tail(self):
        if self.tail is None:
            return None
        else:
            self.tail = self.tail.prev
 
 
stack = Stack()
n_operations = int(input())
for ind_operation in range(n_operations):
    operation = list(map(int, input().split()))
    if operation[0] == 1:  # add element to the end
        stack.insert(operation[1])
    elif operation[0] == 2:  # delete tail
        stack.erase_tail()
    else:  # print min
        print(stack.tail.this_min)
