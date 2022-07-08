import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


class PostfixEvaluator2:  # Standard Python structures
    def __init__(self):
        self.head = 0
        # self.capacity = capacity
        self.array = []

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


class DynamicArray:  # (object)
    def __init__(self):
        self.size = 0
        self.capacity = 1   # default buffer size
        self.array = self._create_array(self.capacity)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            return None
            # raise IndexError('Given index: {0} is larger than array size {1}'.format(index, self.size))
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


expression = sys.stdin.readline().split()  # "8 9 + 1 7 - *".split()  # -102
evaluator = PostfixEvaluator()
print(evaluator.evaluate_expr(expression))


'''stack = Stack()
string = sys.stdin.readline().split()
n = 0
for ch in string:
    if ch < '0': #or ch > '9':
        if ch == '+':
            #a, b = stack.pop(), stack.pop()
            #stack.push(a + b)
            stack.items[n - 2] = stack.items[n - 2] + stack.items[n - 1]
            n -= 1
            #break
        elif ch == '-':
            #a, b = stack.pop(), stack.pop()
            #stack.push(a - b)
            stack.items[n - 2] = stack.items[n - 2] - stack.items[n - 1]
            n -= 1
            #break
        elif ch == '*':
            #a, b = stack.pop(), stack.pop()
            #stack.push(a * b)
            stack.items[n - 2] = stack.items[n - 2] * stack.items[n - 1]
            n -= 1
            #break
        elif ch == '/':
            #a, b = stack.pop(), stack.pop()
            #stack.push(a / b)
            stack.items[n - 2] = stack.items[n - 2] / stack.items[n - 1]
            n -= 1
            #break
    else:
        print(ch)
        #stack.push(int(ch))
        stack.items.append(int(ch))
        n += 1

print("result", stack.pop()) '''
# 8 9 + 1 7 - *   -102
