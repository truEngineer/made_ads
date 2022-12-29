EMPTY_LINK = None
EMPTY_KEY = None
# OPERATIONS CODES
INSERT_OP = 1
DELETE_OP = -1
FIND_K_OP = 0
 
 
class NodeAVL:
 
    def __init__(self, key=EMPTY_KEY, parent=EMPTY_LINK):
        self.key = key
        self.parent = parent
        self.height = 1
        self.size = 1
        
        self.left = EMPTY_LINK
        self.right = EMPTY_LINK
    
    def node_params(self, node):
        if not node == EMPTY_LINK:  # if not empty!
            return node.size, node.height
        return 0, 0
    
    def subtrees_heights(self):
        '''
        Returns heights and sizes of the node's subtrees
            Return format: int left_size, 
                           int height_left, 
                           int size_right, 
                           int height_right
        '''
        size_left, height_left = self.node_params(self.left)
        size_right, height_right = self.node_params(self.right) 
        return size_left, height_left, size_right, height_right
    
    def balance_factor(self):
        '''
        Returns a balance factor of the Node object (self)
            Return format: int
        '''
        _, height_left, _, height_right = self.subtrees_heights()
        return height_right - height_left
    
    def height_update(self):
        '''
        Updates the Node object (self) height
        '''
        size_left, height_left, size_right, height_right = self.subtrees_heights()
        self.size = size_left + size_right + 1
        if height_left > height_right:
            self.height = height_left + 1
        else:
            self.height = height_right + 1
            
    # ROTATIONS
    def rotate_right(self, node):
        '''
        Perform a right rotation around the Node object (self)
        '''
        # update links
        left_node = node.left
        node.left = left_node.right
        left_node.right = node
        # update parents
        left_node.parent = node.parent
        node.parent = left_node
        # update heights
        node.height_update()
        left_node.height_update()
        
        return left_node
    
    def rotate_left(self, node):
        '''
        Perform a left rotation around the Node object (self)
        '''
        # update links
        right_node = node.right
        node.right = right_node.left
        right_node.left = node
        # update parents
        right_node.parent = node.parent
        node.parent = right_node
        # update heights
        node.height_update()
        right_node.height_update()
        
        return right_node
    
    def balance(self, node):
        node.height_update()
        if node.balance_factor() == 2:
            if node.right.balance_factor() < 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        if node.balance_factor() == -2:
            if node.left.balance_factor() > 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        return node  # no balance needed
    
    # OPERATIONS
    def insert(self, node, key, parent=EMPTY_LINK):
        if node == EMPTY_LINK or node.key == EMPTY_KEY:
            return NodeAVL(key=key, parent=parent)  # add new Node()
        if key < node.key:
            node.left = self.insert(node.left, key, parent=node)
        if key > node.key:
            node.right = self.insert(node.right, key, parent=node)
        return self.balance(node)
    
    def delete(self, node, key):
        if node == EMPTY_LINK or node.key == EMPTY_KEY:
            return node
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if node.left != EMPTY_LINK and node.right != EMPTY_LINK:  # two childs
                node.key = self.find_max(node.left).key
                node.left = self.delete(node.left, node.key)  # delete max
            else:  # one or no childs!
                if node.left == EMPTY_LINK:
                    if node.right == EMPTY_LINK:  # no childs
                        if node.parent == EMPTY_LINK:  # root is the only element in tree!
                            node.key = EMPTY_KEY
                        else:
                            return EMPTY_LINK
                    else:  # one child: node.right != EMPTY_LINK
                        node.right.parent = node.parent
                        node = node.right
                else:  # one child: node.left != EMPTY_LINK
                    node.left.parent = node.parent
                    node = node.left
        return self.balance(node)
 
    def find_max(self, node):
        while not node.right == EMPTY_LINK:
            node = self.find_max(node.right)
        return node
    
    def find_k_max(self, node, k):
        if node.left == EMPTY_LINK:
            this_max_ind = node.size
        else:
            this_max_ind = node.size - node.left.size
        if this_max_ind == k:
            return node
        else:
            if this_max_ind > k:
                return self.find_k_max(node.right, k)
            else:
                return self.find_k_max(node.left, k - this_max_ind)
 
 
tree = NodeAVL()
n_operations = int(input())
for _ in range(n_operations):
    op_i, k_i = map(int, input().split())
    if op_i == INSERT_OP:
        tree = tree.insert(tree, k_i)
    elif op_i == DELETE_OP:
        tree = tree.delete(tree, k_i)
    else:  # find k'th
        print(tree.find_k_max(tree, k_i).key)
