'''class HashTable:

    def __init__(self, size):
        self.max_length = size
        self.max_load_factor = 0.75
        self.length = 0
        self.table = [None] * self.max_length

    def __len__(self):
        return self.length

    def __setitem__(self, key, value):
        self.length += 1
        hashed_key = self._hash(key)
        while self.table[hashed_key] is not None:
            if self.table[hashed_key][0] == key:
                self.length -= 1
                break
            hashed_key = self._increment_key(hashed_key)
        pair = (key, value)
        self.table[hashed_key] = pair
        if self.length / float(self.max_length) >= self.max_load_factor:
            self._resize()

    def __getitem__(self, key):
        index = self._find_item(key)
        return self.table[index][1]

    def __delitem__(self, key):
        index = self._find_item(key)
        self.table[index] = None

    def _hash(self, key):
        # TODO more robust
        return hash(key) % self.max_length

    def _increment_key(self, key):
        return (key + 1) % self.max_length

    def _find_item(self, key):
        hashed_key = self._hash(key)
        if self.table[hashed_key] is None:
            raise KeyError
        if self.table[hashed_key][0] != key:
            original_key = hashed_key
            while self.table[hashed_key][0] != key:
                hashed_key = self._increment_key(hashed_key)
                if self.table[hashed_key] is None:
                    raise KeyError
                if hashed_key == original_key:
                    raise KeyError
        return hashed_key

    def _resize(self):
        self.max_length *= 2
        self.length = 0
        old_table = self.table
        self.table = [None] * self.max_length
        for pair in old_table:
            if pair is not None:
                self[pair[0]] = pair[1]'''

#from hashlib import md5

class LinkedListNode:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get(self):
        return self.value


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        new_node = LinkedListNode(value, self.head)
        self.head = new_node
        if self.tail is not None:
            self.tail = new_node
        return self

    def append(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node
        return self

    def find(self, value):
        if self.head is None:
            return None
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        return None

    def delete(self, value):
        if self.head is None:
            return None
        deleted_node = None
        while self.head is not None and self.head.value == value:
            deleted_node = self.head
            self.head = None
        current_node = self.head
        if current_node is not None:
            while current_node.next is not None:
                if current_node.next.value == value:
                    deleted_node = current_node.next
                    current_node.next = current_node.next.next
                else:
                    current_node = current_node.next
        if self.tail.value == value:
            self.tail = current_node
        return deleted_node


class HashTable:

    def __init__(self, size):
        self.buckets = [LinkedList() for _ in range(0, size)]
        self.keys = {}

    def set(self, key, value):
        key_hash = self.hash(key)
        self.keys[key] = key_hash
        bucket_ll = self.buckets[key_hash]
        node = bucket_ll.find({key: value})
        if node is None:
            bucket_ll.append({key: value})
        else:
            node.value.value = value

    def get(self, key):
        bucket_ll = self.buckets[self.hash(key)]
        current_node = bucket_ll.head
        while current_node is not None:
            for k in current_node.value:
                if k == key:
                    return current_node.value[k]
            current_node = current_node.next
        return None

    def delete(self, key):
        key_hash = self.hash(key)
        del self.keys[key]
        bucket_ll = self.buckets[key_hash]
        node = None
        current_node = bucket_ll.head
        while current_node is not None and node is None:
            for k in current_node.value:
                if k == key:
                    node = current_node
                    break
            current_node = current_node.next
        if node is not None:
            return bucket_ll.delete(node.value)
        return None

    def hash(self, key):
        #k = 0
        #for s in list(md5(str(key).encode('utf-8')).hexdigest()):
        #    k += ord(s)
        #return k % len(self.buckets)
        return key % len(self.buckets)

    def has(self, key):
        if key in self.keys.keys():
            return True
        else:
            return False

    def get_keys(self):
        return list(self.keys.keys())


hasht = HashTable(int(1e5))
operation = input().split()
while operation:
    op, x = operation[0], int(operation[1])
    if op == "insert":
        hasht.set(x, 1)
    elif op == "exists":
        print(hasht.has(x))
    elif op == "delete":
        hasht.delete(x)
    operation = input().split()
