import sys


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.min = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
            self.head.min = value
        else:
            new_node = Node(value)
            new_node.next = self.head
            new_node.min = min(self.head.min, value)
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.value
            self.head = self.head.next
            return popped

    def min(self):
        if self.head is None:
            return None
        else:
            return self.head.min


stack = Stack()
n = int(sys.stdin.readline())
for _ in range(n):
    cmd = list(map(int, sys.stdin.readline().split()))
    if cmd[0] == 1:
        stack.push(cmd[1])  # add element
    elif cmd[0] == 2:
        stack.pop()  # delete element
    else:
        print(stack.min())  # print current min
