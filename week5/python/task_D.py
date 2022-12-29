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
 
 
class MultiMap:
 
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.array = [ [] for _ in range(self.capacity)]
        self.hash_a = random.choice(PRIMES)  # for hashing
        self.hash_b = random.choice(PRIMES)
        
        self.cells_size = [ 0 for _ in range(self.capacity)]
        self.cells_putted = [ 0 for _ in range(self.capacity)]
 
    def print_array(self):
        return
        print(*self.array, sep='\n')
        print(*self.cells_putted)
        
    def hash_func(self, word):
        word_hash = self.hash_a
        for char in word:
            char_abc_ind = (ord(char) - FIRST_ABC + 1)
            word_hash = word_hash * self.hash_a + char_abc_ind
        # print(f"Hash for '{word}' = {word_hash} % {self.capacity} = {word_hash % self.capacity}")
        return word_hash % self.capacity
    
    def rehashing(self, frac):        
        self.capacity = self.capacity * frac
        self.hash_a = random.choice(PRIMES)  # for hashing
        self.hash_b = random.choice(PRIMES)  # new constants in hash-function
        
        old_array = self.array
        
        self.cells_size = [ 0 for _ in range(self.capacity)]
        self.cells_putted = [ 0 for _ in range(self.capacity)]
        
        self.array = [ [] for _ in range(self.capacity)]
        for slot in old_array:
            for ind, key_values_i in enumerate(slot):
                self.rehashing_put(key_values_i)
        self.print_array()
        
    def rehashing_put(self, key_values):  # just put
        key_hash = self.hash_func(key_values[0])  # calculate a hash for key
        self.array[key_hash].append(key_values)
        self.cells_size[key_hash] += 1  # key added to the cell
        self.cells_putted[key_hash] += len(key_values) - 1  # values added
 
    def put(self, key, value):
        key_hash = self.hash_func(key)
        for ind, key_values_i in enumerate(self.array[key_hash]):
            key_i = key_values_i[0]
            values_i = key_values_i[1]  # set of values
            if key_i == key:  # key exists
                if not value in values_i:
                    self.array[key_hash][ind][1].add(value)  # add value to set for key
                    self.cells_putted[key_hash] += 1  # value added
                self.print_array()
                return
                
        self.array[key_hash].append([key, set([value])])  # add new key
        self.cells_size[key_hash] += 1  # key added to the cell
        self.cells_putted[key_hash] += 1  # value added
        
        if self.rehashing_needed(key_hash):  # check if rehashing needed!
            self.rehashing(FRAC)
        self.print_array()
 
    def rehashing_needed(self, key_hash):  # return True or False
        if self.cells_size[key_hash] > 1 and \
                self.cells_putted[key_hash] > self.capacity and \
                    self.cells_putted[key_hash] >= sum(self.cells_putted) // self.capacity + int(TRESHOLD * self.capacity):
            return True
        return False
    
    def get(self, key):
        key_hash = self.hash_func(key)
        for ind, key_values_i in enumerate(self.array[key_hash]):
            key_i = key_values_i[0]
            values_i = key_values_i[1]  # set of values
            if key_i == key:
                return values_i  # return only values
        return []  # empty
 
    def delete(self, key, value):
        key_hash = self.hash_func(key)
        for ind, key_values_i in enumerate(self.array[key_hash]):
            key_i = key_values_i[0]
            values_i = key_values_i[1]  # set of values
            if key_i == key:
                if value in values_i:  # FAST FOR SETS!
                    if len(values_i) == 1:
                        del self.array[key_hash][ind]  # delete key at all
                        self.cells_size[key_hash] -= 1
                        self.cells_putted[key_hash] -= len(values_i)  # key deleted
                        self.print_array()
                        return
                    else:  # remove one element from set
                        values_i.remove(value)
                        self.cells_putted[key_hash] -= 1  # value deleted
                        self.print_array()
                        return
            
    def deleteall(self, key):
        key_hash = self.hash_func(key)
        for ind, key_values_i in enumerate(self.array[key_hash]):
            key_i = key_values_i[0]
            values_i = key_values_i[1]  # set of values
            if key_i == key: # if key is in the Map
                del self.array[key_hash][ind]
                self.cells_size[key_hash] -= 1
                self.cells_putted[key_hash] -= len(values_i)  # key deleted
                self.print_array()
                return
 
 
table = MultiMap()
for operation in stdin:
    op_list = operation.split()
    op_type = op_list[0]
    if op_type == "get":
        values = table.get(op_list[1])
        print(len(values), end="")
        if len(values) > 0:
            print("", *values)
        else:
            print()
    elif op_type == "deleteall":
        table.deleteall(op_list[1])
    elif op_type == "delete":
        table.delete(op_list[1], op_list[2])
    else:  # put
        table.put(op_list[1], op_list[2])
