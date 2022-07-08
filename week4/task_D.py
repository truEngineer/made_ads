import sys


class PriorityQueue:
    def __init__(self):
        self.entries = []

    def push(self, value):
        self.entries.append(value)

    def extract_min(self):
        if not self.entries:
            return None  # raise UnderFlowError("The queue is empty")
        else:
            data = min(self.entries)
            self.entries.remove(data)
            return data

    def decrease_key(self, push_num, value):
        if not self.entries:
            return None  # raise UnderFlowError("The queue is empty")
        else:
            data = min(self.entries)
            self.entries.remove(data)
            return data


pqueue = PriorityQueue()
m = int(sys.stdin.readline())
for i in range(m):
    cmd = ['push 3', 'push 4', 'push 2', 'extract-min', 'decrease-key 2 1',
           'extract-min', 'extract-min', 'extract-min'][i].split()  # list(sys.stdin.readline().split())
    if cmd[0] == "push":
        pqueue.push(int(cmd[1]))
    elif cmd[0] == "extract-min":
        print(pqueue.extract_min())
    elif cmd[0] == "decrease-key":
        pqueue.decrease_key(int(cmd[1]), int(cmd[2]))
