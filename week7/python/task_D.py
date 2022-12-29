from sys import stdin
 
 
INF = 1e18
 
 
class Node():
    def __init__(self, value=INF, parent=None):
        # min value among two childrens
        self.min = value
        # if need to increment all childs with add
        self.add = 0
        # if need to set values of the node and all its childs
        self.set = None
 
 
class SegmentTree():
    def __init__(self, array):
        self.size = None  # number of all nodes (with leafs)
        self.leafs = None  # number of leafs in the tree
        self.tree = None  # array with nodes
        # initialization of the self.tree
        self.build_tree(array)
 
    def print_tree(self):
        for ind, node in enumerate(self.tree):
            print(f"{ind}. Val = {[node.min, node.add, node.set]},\t Parent = {node.parent}")
    
    # GET INDEXES
    def get_childs(self, ind):
        # returns indexes of the left and right childs of the node tree[ind]
        return 2 * ind + 1, 2 * ind + 2
    
    def get_leaf_ind(self, ind_leaf):
        # returns leaf index in the tree by its index in initial array
        return ind_leaf + self.leafs - 1
    
    # UPDATE VALS    
    def update_node(self, ind, l, r):
        '''
        int ind - index (in tree) of node to update value
        int l, r - indexes (in tree) of left and right childs
        '''
        self.tree[ind].min = min(self.get(l), 
                                 self.get(r))
    
    def get(self, ind):  # lr, rr)
        '''
        int ind - index of the node (in tree) to get value
        '''
        if self.tree[ind].set is None:
            return self.tree[ind].min + self.tree[ind].add
        return self.tree[ind].set
 
    # TREE
    def build_tree(self, leafs_array):
        '''
        list[int] leafs_array - array of leafs values from the condition
        '''
        arr_len = len(leafs_array)
        self.leafs = 1  # number of leafs
        power = 0
        while self.leafs < arr_len:
            self.leafs *= 2
        # necessary number of nodes in the full binary tree
        self.size =  2 * self.leafs - 1
        # create array for tree with "empty nodes"
        self.tree = [Node() for _ in range(self.size)]
        # store initial array "in the end" of the tree (leafs)
        for ind_leaf, value_leaf in enumerate(leafs_array):
            ind_leaf_in_tree = self.get_leaf_ind(ind_leaf)
            self.tree[ind_leaf_in_tree].min = value_leaf
        # fill the rest of the tree (down -> up)
        for ind_node in reversed(range(self.leafs - 1)):
            left_child, right_child = self.get_childs(ind_node)
            self.update_node(ind_node, left_child, right_child)
    
    # OPERATIONS    
    def push(self, ind):  # lefter, righter
        '''
        int ind - index of the node in tree to push
        Comment:
                in the node can be not more than one marker: add or set!
        '''
        l, r = self.get_childs(ind)  # left and right childs of  the node[ind]
        # if list is the "setting" one
        if self.tree[ind].set is not None:
            to_set = self.tree[ind].set
            # if node is the leaf
            if l >= self.size:
                # print(f"Node {ind_node} set")
                self.tree[ind].min = to_set
            else:
                for child in [l, r]:
                    # the new set resets previous adds in childrens
                    self.tree[child].add = 0
                    # and updates set previous set values
                    self.tree[child].set = to_set
                # node value update after push
                self.update_node(ind, l, r)
            self.tree[ind].set = None  # reset set that was pushed down!
            return
        # if list is the "adding" one (non-zero)
        if not self.tree[ind].add == 0:
            to_add = self.tree[ind].add
            # if node is the leaf
            if l >= self.size:
                self.tree[ind].min += self.tree[ind].add
            else:
                for child in [l, r]:
                    # if we have no set in childfor
                    if self.tree[child].set is None:
                        self.tree[child].add += to_add
                    else: # if child has "set" - update set
                        self.tree[child].set += to_add
                # node value update after push
                self.update_node(ind, l, r)
            self.tree[ind].add = 0  # reset set that was pushed down
            return
        
    def update_add(self, ind,
                   lr, rr,
                   a, b,
                   value):
        '''
        int self, ind - index (in tree) of the node
        int lr, rr    - indexes (in tree) of lefter and righter reachable leafs
        int a, b      - indexes (in tree) of left (l) and right (r) leafs to update the segment
        int value     - value to add
        '''
        self.push(ind)
        if lr > b or rr < a:  # [a ... b] ... [lr ... rr]  OR  [lr ... rr] ... [a ... b]
            return
        if lr >= a and rr <= b:  # [a ... [lr ... rr] ... b]
            self.tree[ind].add += value  # update add
            # can't be something else since we pushed the node[ind]
            return
        # [a ... [lr ... b] ... rr]  OR  [lr ... [a ... rr] ... b]
        mr = (lr + rr) // 2  # middle reachable leaf from node[ind]
        l, r = self.get_childs(ind)  # left and right childs of  the node[ind]
        
        self.update_add(l, lr, mr, a, b, value)
        self.update_add(r, mr + 1, rr, a, b, value)
        
        self.update_node(ind, l, r)  # update node value
        
    def update_set(self, ind,
                   lr, rr,
                   a, b,
                   value):
        '''
        int self, ind - index (in tree) of the node
        int lr, rr    - indexes (in tree) of lefter and righter reachable leafs
        int a, b      - indexes (in tree) of left (l) and right (r) leafs to update the segment
        int value     - value to add
        '''
        self.push(ind)
        if lr > b or rr < a:  # [a ... b] ... [lr ... rr]  OR  [lr ... rr] ... [a ... b]
            return
        if lr >= a and rr <= b:  # [a ... [lr ... rr] ... b]
            self.tree[ind].set = value  # update set
            # can't be something else since we pushed the node[ind]
            return
        # [a ... [lr ... b] ... rr]  OR  [lr ... [a ... rr] ... b]
        mr = (lr + rr) // 2  # middle reachable leaf from node[ind]
        l, r = self.get_childs(ind)  # left and right childs of  the node[ind]
        
        self.update_set(l, lr, mr, a, b, value)
        self.update_set(r, mr + 1, rr, a, b, value)
        
        self.update_node(ind, l, r)  # update node value
                    
    def rmq(self, ind,
            lr, rr,
            a, b):
        '''
        int self, ind - index (in tree) of the node
        int ll, rr    - indexes (in tree) of lefter and righter reachable leafs
        int a, b      - indexes (in tree) of left (l) and right (r) leafs to update the segment
        Comment:
                When calling from main() {ind = 0, lr = 0, righter = self.size - 1} - starting rmq() from root
        '''
        self.push(ind)
        if lr > b or rr < a:  # [a ... b] ... [lr ... rr]  OR  [lr ... rr] ... [a ... b]
            return INF
        if lr >= a and rr <= b:  # [a ... [lr ... rr] ... b]
            return self.get(ind)
        # [a ... [lr ... b] ... rr]  OR  [lr ... [a ... rr] ... b]
        mr = (lr + rr) // 2  # middle reachable leaf from node[ind]
        l, r = self.get_childs(ind)  # left and right childs of  the node[ind]
        
        return min(self.rmq(l, lr, mr, a, b),
                   self.rmq(r, mr + 1, rr, a, b))
 
 
n = int(input())
array = list(map(int, input().split()))
segment_tree = SegmentTree(array)
# define root 
root = 0  # index of the root in tree
root_lr = segment_tree.leafs - 1  # index (in tree) of the lefter achievable leaf from root
root_rr = segment_tree.size - 1  # index (in tree) of the righter achievable leaf from root
zero_leaf_ind = root_lr  # index of a zero leaf
# READING OPERATIONS
for operation in stdin:
    args = operation.split()
    # define indexes of the segment borders in the tree
    ind_from = int(args[1]) - 1 + zero_leaf_ind
    ind_to = int(args[2]) - 1 + zero_leaf_ind
    if args[0] == "set":
        value = int(args[3])
        segment_tree.update_set(ind=root, lr=root_lr, rr=root_rr, a=ind_from, b=ind_to, value=value)
    elif args[0] == "min":
        print(segment_tree.rmq(ind=root, lr=root_lr, rr=root_rr, a=ind_from, b=ind_to))
    else:  # add
        value = int(args[3])
        segment_tree.update_add(ind=root, lr=root_lr, rr=root_rr, a=ind_from, b=ind_to, value=value)
