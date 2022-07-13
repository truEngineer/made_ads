import sys
 
 
class Queue:
    def __init__(self):
        self.entries = []
        self.length = 0
        self.front = 0
 
    def add(self, item):
        self.entries.append(item)
        self.length = self.length + 1
 
    def get(self):
        self.length = self.length - 1
        dequeued = self.entries[self.front]
        self.entries = self.entries[1:]
        return dequeued
 
 
queue = Queue()
m = int(sys.stdin.readline())
for _ in range(m):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == '+':
        queue.add(int(cmd[1]))  # add element
    elif cmd[0] == '-':
        print(queue.get())  # get element
