from sys import stdin
 
EMPTY_LINK = None
EMPTY_KEY = None
 
 
class Node:
 
    def __init__(self, key=EMPTY_KEY, parent=EMPTY_LINK):
        self.key = key
        self.parent = parent
        self.left = EMPTY_LINK
        self.right = EMPTY_LINK
    
    def insert(self, node, key, parent=EMPTY_LINK):
        if node == EMPTY_LINK or node.key == EMPTY_KEY:
            return Node(key=key, parent=parent)  # add new Node()
        if key < node.key:
            node.left = self.insert(node.left, key, parent=node)
        if key > node.key:
            node.right = self.insert(node.right, key, parent=node)
        return node
    
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
        return node
 
    def find_max(self, node):
        while not node.right == EMPTY_LINK:
            node = self.find_max(node.right)
        return node
        
    def search(self, node, key):
        if node == EMPTY_LINK or node.key == EMPTY_KEY:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)
    
    def next_key(self, key):
        node = self  # root
        res = EMPTY_LINK  # link on minimal key that is greater than "key" (answer)
        while not node == EMPTY_LINK:
            if node.key == EMPTY_KEY:
                break
            if node.key > key:
                res = node
                node = node.left
            else:
                node = node.right
        return res
    
    def prev_key(self, key):
        node = self  # root
        res = EMPTY_LINK  # link on maximal key that is less than "key" (answer)
        while not node == EMPTY_LINK:
            if node.key == EMPTY_KEY:
                break
            if node.key < key:
                res = node
                node = node.right
            else:
                node = node.left
        return res
 
 
tree = Node()
for operation in stdin:
    op_type, key = operation.split()
    key = int(key)
    if op_type == "insert":
        tree = tree.insert(tree, key)
    elif op_type == "delete":
        tree = tree.delete(tree, key)
    elif op_type == "exists":
        if tree.search(tree, key):
            print("true")
        else:
            print("false")
    else:  # next or prev
        if op_type == "next":
            res = tree.next_key(key)
        else:  # prev
            res = tree.prev_key(key)
        if res is not EMPTY_LINK:
            print(res.key)
        else:
            print("none")
