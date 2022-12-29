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
 
 
class NodeKey:
 
    def __init__(self, val, prv=None, nxt=None):
        self.val = val
        self.prv = prv  # NodeKey instance
        self.nxt = nxt  # NodeKey instance
 
 
class LinkedMap:
 
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.array = [ [] for _ in range(self.capacity)]
        self.cells_size = [ 0 for _ in range(self.capacity)]
        
        # add value: [key_i (of class NodeKey), value_i]
        self.prev_key = None
        
        self.hash_a = random.choice(PRIMES)  # for hashing
        self.hash_b = random.choice(PRIMES)
        
    def print_array(self):
        return
        key = self.prev_key
        while not key is None:
            print(f"{key.val} >>", end=" ")
            key = key.prv
        print()
        print(*self.array, sep='\n')
        
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
        self.array = [ [] for _ in range(self.capacity)]
        for slot in old_array:
            for ind, [key_i, value_i] in enumerate(slot):
                self.rehashing_put(key_i, value_i)
        self.print_array()
    
    def rehashing_put(self, key: NodeKey, value):  # just put^ saving all keys links on next and previous
        key_hash = self.hash_func(key.val)
        self.array[key_hash].append([key, value])
        self.cells_size[key_hash] += 1  # key added to the cell
 
    def put(self, key_val, value):
        key_hash = self.hash_func(key_val)
        for ind, [key_i, value_i] in enumerate(self.array[key_hash]):  # key_i is a NodeKey instance
            if key_i.val == key_val:
                self.array[key_hash][ind][1] = value  # update key value in self.array
                self.print_array()
                return
        
        key = NodeKey(val=key_val, prv=self.prev_key, nxt=None)  # create new key
        if not self.prev_key is None:
            self.prev_key.nxt = key  # update next key for previously added key
        
        self.array[key_hash].append([key, value])  # add new key-value pair to self.array
        self.prev_key = key
        self.cells_size[key_hash] += 1  # key added to the cell
        
        # print(f"{len(self.array[key_hash])} ? {self.words_number // self.capacity + TRESHOLD_VAL}")
        if self.rehashing_needed(key_hash):  # check if rehashing needed!
            self.rehashing(FRAC)
        self.print_array()
        
    def rehashing_needed(self, key_hash):  # return True or False
        if self.cells_size[key_hash] > self.capacity and \
                    self.cells_size[key_hash] >= sum(self.cells_size) // self.capacity + int(TRESHOLD * self.capacity):
            return True
        return False
 
    def get(self, key_val):
        key_hash = self.hash_func(key_val)
        for ind, [key_i, value_i] in enumerate(self.array[key_hash]):
            if key_i.val == key_val:
                return self.array[key_hash][ind]  # return key-value pair
        return None
 
    def delete(self, key_val):
        key_hash = self.hash_func(key_val)
        for ind, [key_i, value_i] in enumerate(self.array[key_hash]):
            if key_i.val == key_val:
                # change linked keys for key_i.prev and key_i.next
                if not key_i.prv is None:
                    nxt_i = key_i.nxt
                    if not nxt_i is None:
                        nxt_i.prv = key_i.prv
                    key_i.prv.nxt = nxt_i
                if not key_i.nxt is None:
                    key_i.nxt.prv = key_i.prv
                if key_i.nxt is None:  # if last added key deleted
                    self.prev_key = key_i.prv
                    
                del self.array[key_hash][ind]  # delete key value
                self.cells_size[key_hash] -= 1
                self.print_array()
                return
            
    def get_prev_key(self, key_val):
        get_key_value_pair = self.get(key_val)
        if get_key_value_pair is None:
            return None
        if get_key_value_pair[0].prv is None:
            return None
        return self.get(get_key_value_pair[0].prv.val)  # return value of previously added key
    
    def get_next_key(self, key_val):
        get_key_value_pair = self.get(key_val)
        if get_key_value_pair is None:
            return None
        if get_key_value_pair[0].nxt is None:
            return None
        return self.get(get_key_value_pair[0].nxt.val)  # return value of next added key
 
 
def none_print(value):
    if value is None:
        print('none')
    else:
        print(value[1])
 
 
table = LinkedMap()
for operation in stdin:
    op_list = operation.split()
    op_type = op_list[0]
    if op_type == "get":
        none_print(table.get(op_list[1]))
    elif op_type == "delete":
        table.delete(op_list[1])
    elif op_type == "prev":
        none_print(table.get_prev_key(op_list[1]))
    elif op_type == "next":
        none_print(table.get_next_key(op_list[1]))
    else:  # put
        table.put(op_list[1], op_list[2])
