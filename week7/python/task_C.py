from sys import stdin
 
 
class FenwickTree():
    def __init__(self, array):
        self.size = len(array)
        self.array = array
        self.prefix_sums = self.compute_prefix_sums(array)
    
    @staticmethod
    def first_in_prefix(ind):
        return ind & ind + 1
 
    def compute_prefix_sums(self, array):
        sums = [0 for _ in range(self.size)]
        for ind in range(self.size):
            for ind_prefix in range(self.first_in_prefix(ind), ind + 1):
                sums[ind] += array[ind_prefix]
        return sums
    
    def get_sum(self, ind):
        res = 0
        while ind >= 0:
            res += self.prefix_sums[ind]
            ind = self.first_in_prefix(ind) - 1
        return res
 
    def rsq(self, left, right):
        if left == 0:
            return self.get_sum(right)
        return self.get_sum(right) - self.get_sum(left - 1)
    
    def add(self, ind, delta):
        ind_new = ind
        while ind_new < self.size:
            self.prefix_sums[ind_new] += delta
            ind_new = ind_new | ind_new + 1
    
    def set_elem(self, ind, value):
        delta = value - self.array[ind]
        self.array[ind] = value
        self.add(ind, delta)
 
 
n = int(input())
array = list(map(int, input().split()))
fw_tree = FenwickTree(array)
for operation in stdin:
    op_type, arg_1, arg_2 = operation.split()
    arg_1, arg_2 = map(int, [arg_1, arg_2])
    if op_type == "sum":
        print(fw_tree.rsq(arg_1 - 1, arg_2 - 1))
    else:  # set
        fw_tree.set_elem(arg_1 - 1, arg_2)
