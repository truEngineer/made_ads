from sys import stdin
import random
 
 
FRAC = 2
# for hashing
# initialising primes
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
          47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 
          107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 
          167, 173, 179, 181, 191, 193, 197, 199]
TRESHOLD = 0.2  # from capacity
FIRST_ABC = ord("a")
 
 
class MapChain:
 
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.array = [ [] for _ in range(self.capacity)]
        self.hash_a = random.choice(PRIMES)  # for hashing
        self.hash_b = random.choice(PRIMES)
        
        self.cells_size = [0] * self.capacity
        self.rehashing_process = False  # if rehashing in progress
 
    def print_array(self):
        return
        print(*self.array, sep='\n')
        
    def hash_func(self, word):
        word_hash = self.hash_a
        for char in word:
            char_abc_ind = (ord(char) - FIRST_ABC + 1)
            word_hash = word_hash * self.hash_a + char_abc_ind
        # print(f"Hash for '{word}' = {word_hash} % {self.capacity} = {word_hash % self.capacity}")
        return word_hash % self.capacity
    
    def rehashing(self, frac):
        self.rehashing_process = True
        
        self.capacity = self.capacity * frac
        self.hash_a = random.choice(PRIMES)  # for hashing
        self.hash_b = random.choice(PRIMES)  # new constants in hash-function
        
        old_array = self.array
        
        self.cells_size = [0] * self.capacity
        self.array = [ [] for _ in range(self.capacity)]
        for slot in old_array:
            for ind, [key_i, value_i] in enumerate(slot):
                self.put(key_i, value_i)
        self.print_array()
        self.rehashing_process = False
        
    def rehashing_needed(self, key_hash):  # return True or False
        if self.cells_size[key_hash] > self.capacity and \
                    self.cells_size[key_hash] >= sum(self.cells_size) // self.capacity + int(TRESHOLD * self.capacity):
            return True
        return False
 
    def put(self, key, value):
        key_hash = self.hash_func(key)
        for ind, [key_i, value_i] in enumerate(self.array[key_hash]):
            if key_i == key:
                self.array[key_hash][ind][1] = value  # update value
                self.print_array()
                return
        self.array[key_hash].append([key, value])  # add new value
        self.cells_size[key_hash] += 1  # key added to the cell
        
        # print(f"{len(self.array[key_hash])} ? {self.words_number // self.capacity + TRESHOLD_VAL}")
        if not self.rehashing_process:
            if self.rehashing_needed(key_hash):  # check if rehashing needed!
                self.rehashing(FRAC)
        self.print_array()
 
    def get(self, key):
        key_hash = self.hash_func(key)
        for ind, [key_i, value_i] in enumerate(self.array[key_hash]):
            if key_i == key:
                return self.array[key_hash][ind][1]  # return key value
        return None
 
    def delete(self, key):
        key_hash = self.hash_func(key)
        for ind, [key_i, value_i] in enumerate(self.array[key_hash]):
            if key_i == key:
                del self.array[key_hash][ind]  # delete key value
                self.cells_size[key_hash] -= 1
                self.print_array()
                return
 
 
table = MapChain()
for operation in stdin:
    op_list = operation.split()
    op_type = op_list[0]
    if op_type == "get":
        value = table.get(op_list[1])
        if value is None:
            print('none')
        else:
            print(value)
    elif op_type == "delete":
        table.delete(op_list[1])
    else:  # put
        table.put(op_list[1], op_list[2])
