EXPAND_FACTOR = 2
EMPTY_ELEMENT = None
 
 
class Vector:
 
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.elements = [EMPTY_ELEMENT] * self.capacity
 
    def expand(self, factor):
        new_capacity = int(self.capacity * factor)
        new_elements = [EMPTY_ELEMENT] * new_capacity
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements
        self.capacity = new_capacity
 
    def add(self, element):
        if self.size == self.capacity:
            self.expand(EXPAND_FACTOR)  # expand array
        self.elements[self.size] = element
        self.size += 1
 
    def get_last(self):
        if self.size > 0:
            element = self.elements[self.size - 1]
            self.elements[self.size - 1] = EMPTY_ELEMENT
            self.size -= 1
            if self.size <= self.capacity // EXPAND_FACTOR ** 2:
                self.expand(1 / EXPAND_FACTOR)
            return element
        else:
            return EMPTY_ELEMENT
 
 
expression = input().split()
numbers = Vector()
 
for char in expression:
    if char.isdigit():  # reading number
        numbers.add(char)
    else:  # reading operation char
        value_1 = numbers.get_last()
        value_2 = numbers.get_last()
        operation_res = eval(value_2 + char + value_1)
        numbers.add(str(operation_res))
print(numbers.get_last())
