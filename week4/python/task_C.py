EXPAND_FACTOR = 2
EMPTY_ELEMENT = None
 
 
class QueueOnVector:
 
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.front = 0  # first element where queue starts
        self.elements = [EMPTY_ELEMENT] * self.capacity
        # print(f"Queue (sz {self.size}, fr {self.front}): {self.elements}")
 
    def expand(self, factor):
        new_capacity = int(self.capacity * factor)
        new_elements = [EMPTY_ELEMENT] * new_capacity
        for i in range(self.size):  # cyclical!
            new_elements[i] = self.elements[(self.front + i) % self.capacity]
        self.elements = new_elements
        self.capacity = new_capacity
        self.front = 0
 
    def add(self, element):
        if self.size == self.capacity:
            self.expand(EXPAND_FACTOR)  # expand array
        self.elements[(self.front + self.size) % self.capacity] = element
        self.size += 1
        # print(f"Queue (sz {self.size}, fr {self.front}): {self.elements}")
 
    def pop_front(self):
        if self.size > 0:
            element = self.elements[self.front]
            self.elements[self.front] = EMPTY_ELEMENT
            self.size -= 1
            self.front = (self.front + 1) % self.capacity
            if self.size > 0 and self.size <= self.capacity // EXPAND_FACTOR ** 2:
                self.expand(1 / EXPAND_FACTOR)
            # print(f"Queue (sz {self.size}, fr {self.front}): {self.elements}")
            return element
        else:
            return EMPTY_ELEMENT
 
 
queue = QueueOnVector()
num_command = int(input())
for command_ind in range(num_command):
    command = list(input().split())
    if command[0] == '+':
        queue.add(int(command[1]))
    else:
        print(queue.pop_front())
