from sys import stdin
import random
 
 
EMPTY = []
RIP = None
FRAC = 4
# for hashing
NUM_P = 614657  # 65537
MIN_A = 1
MAX_A = 100
 
 
class HashTable:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.size = 0  # with ripped!
        self.ripped = 0
        self.array = [EMPTY] * capacity
        self.hash_a = random.randint(MIN_A, MAX_A)
        self.flag_rehashing = False
 
    def print_array(self):
        return
        print(self.array)
        
    def hash_func(self, element):
        return ( (self.hash_a * abs(element)) % NUM_P ) % self.capacity
    
    def next_empty(self, ind):
        return (ind + 1) % self.capacity
    
    def rehashing(self, frac):
        self.flag_rehashing = True
        self.capacity = int(self.capacity * frac)
        self.hash_a = random.randint(MIN_A, MAX_A)  # new A in hash-function
        
        self.size = 0
        self.ripped = 0
        old_array = self.array
        self.array = [EMPTY] * self.capacity
        for element in old_array:
            if (not element == EMPTY) and (not element == RIP):
                self.insert(element)
        self.flag_rehashing = False
        
    def insert(self, element):
        arr_place = self.hash_func(element)
        first_ripped_ind = None
        while not self.array[arr_place] == EMPTY:
            if self.array[arr_place] == element:  # element is already in set
                self.print_array()
                return
            if self.array[arr_place] == RIP and first_ripped_ind is None:  # potentially fill ripped element
                first_ripped_ind = arr_place
            arr_place = self.next_empty(arr_place)  # next space
        else:
            if first_ripped_ind is None:
                self.array[arr_place] = element
                self.size += 1
            else:  # if ripped place was found
                self.array[first_ripped_ind] = element
                self.ripped -= 1
        
        if (not self.flag_rehashing) and (FRAC * (self.size - self.ripped) > self.capacity):
            self.rehashing(FRAC)
        self.print_array()
 
    def contains(self, element):
        arr_place = self.hash_func(element)
        while not self.array[arr_place] == EMPTY:
            if self.array[arr_place] == element:
                return True
            arr_place = self.next_empty(arr_place)  # next space
        return False
    
    def delete(self, element):
        arr_place = self.hash_func(element)
        while not self.array[arr_place] == EMPTY:
            if self.array[arr_place] == element:
                self.array[arr_place] = RIP
                self.ripped += 1
                self.print_array()
                break
            arr_place = self.next_empty(arr_place)  # next space
 
        # if (not self.flag_rehashing) and (FRAC ** 2 * (self.size - self.ripped) < self.capacity) and (self.size > 1):
        #     self.rehashing(1 / FRAC)  # // FRAC
        self.print_array()
 
 
table = HashTable()
for operation in stdin:
    op_list = operation.split()
    op_type, val = op_list
    if op_type == "insert":
        table.insert(int(val))
    elif op_type == "delete":
        table.delete(int(val))
    else:  # exists
        if table.contains(int(val)):
            print("true")
        else:
            print("false")
