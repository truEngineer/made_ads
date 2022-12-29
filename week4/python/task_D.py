from sys import stdin
 
 
class MyHeap():
    
    def __init__(self):
        self.size = 0
        self.elements = []
        self.pushes = []
    
    @staticmethod
    def parent_ind(child_ind):  # returns parent index
        return (child_ind - 1) // 2
    
    @staticmethod
    def left_child_ind(parent_ind):
        return 2 * parent_ind + 1
    
    @staticmethod
    def right_child_ind(parent_ind):
        return 2 * parent_ind + 2
    
    def check_print(self):
        # print(f"{self.elements}, {self.pushes}")
        return
        
    def swap(self, ind1, ind2):
        self.elements[ind1], self.elements[ind2] = \
                            self.elements[ind2], self.elements[ind1]
        # swap keys together with elements
        self.pushes[ind1], self.pushes[ind2] = \
                            self.pushes[ind2], self.pushes[ind1]
    
    def sift_up(self, child_ind):
        parent_ind = self.parent_ind(child_ind)
        while (parent_ind >= 0) and (self.elements[child_ind] < self.elements[parent_ind]):
            self.swap(child_ind, parent_ind)
            child_ind = parent_ind
            parent_ind = self.parent_ind(child_ind)
        self.check_print()
        
    def insert(self, element, push_num):
        self.size += 1
        self.elements.append(element)  # add
        self.pushes.append(push_num) 
        
        self.sift_up(child_ind=self.size - 1)
        
    
    def sift_down(self, parent_ind):
        while self.left_child_ind(parent_ind) < self.size:  # while we have next level
            parent = self.elements[parent_ind]
            # childrens indeces
            left_ind = self.left_child_ind(parent_ind)
            right_ind = self.right_child_ind(parent_ind)
            # left children value
            left_child = self.elements[left_ind]
            # find the minimal child
            min_ind = left_ind
            if right_ind < self.size and self.elements[right_ind] < left_child:
                # right children value
                right_child = self.elements[right_ind]
                min_ind = right_ind
            min_child = self.elements[min_ind]
            if min_child < parent:  # if the min child less than parent
                self.swap(min_ind, parent_ind)
                parent_ind = min_ind
            else:
                self.check_print()
                break
        
    def remove_min(self):
        if  self.size == 0:
            print("*")
            return
        min_to_return = self.elements[0]
        ind_of_push = self.pushes[0]
        self.swap(0, self.size - 1)
        del self.elements[-1]
        del self.pushes[-1]
        self.size -= 1
        
        self.sift_down(parent_ind=0)
        print(*[min_to_return, ind_of_push])
    
    def decrease_elem(self, push_num, new_val):
        if not push_num in self.pushes:
            return None
        elem_ind = self.pushes.index(push_num)
        self.elements[elem_ind] = new_val
        self.check_print()
        
        # since we decrease element!
        self.sift_up(elem_ind)
        self.check_print()
 
 
heap = MyHeap()
n_operation = 0
for operation in stdin:
    n_operation += 1
    op_list = operation.split()
    op_type = op_list[0]
    if op_type == "push":
        heap.insert(int(op_list[1]), n_operation)
    elif op_type == "extract-min":
        heap.remove_min()
    else:  # decrease-key
        heap.decrease_elem(int(op_list[1]), int(op_list[2]))
