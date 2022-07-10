import sys
 
 
class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1  # default buffer size
        self.array = self._create_array(self.capacity)
 
    def __len__(self):
        return self.size
 
    def __getitem__(self, index):
        if not 0 <= index < self.size:
            return None
        return self.array[index]
 
    @staticmethod
    def _create_array(length):
        return [None] * length
 
    def _resize(self, new_capacity):
        new_array = self._create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
 
    def append(self, element):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)  # expand array
        self.array[self.size] = element
        self.size += 1
 
    def pop(self):
        element = None
        if self.size > 0:
            element = self.array[self.size - 1]
            self.array[self.size - 1] = None
            self.size -= 1
            if self.size <= self.capacity // 4:
                self._resize(self.capacity // 2)  # reduce array
        return element
 
 
class PostfixEvaluator:
    def __init__(self):
        self.head = 0
        self.array = DynamicArray()
 
    def pop(self):
        if self.head != 0:
            self.head -= 1
            return self.array.pop()
        else:
            return None
 
    def push(self, op):
        self.head += 1
        self.array.append(op)
 
    def evaluate_expr(self, exp):  # evaluate postfix expression
        for ch in exp:
            if ch.isdigit():
                self.push(ch)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + ch + val1)))
        return int(self.pop())
 
 
expression = sys.stdin.readline().split()
evaluator = PostfixEvaluator()
print(evaluator.evaluate_expr(expression))
