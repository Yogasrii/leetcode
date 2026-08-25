class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node()   # Least recently used side
        self.right = Node()  # Most recently used side

        self.left.next = self.right
        self.right.prev = self.left

    # Add node just before right
    def insert(self, node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    # Remove node
    def remove(self, node):
        prev = node.prev
        next_node = node.next

        prev.next = next_node
        next_node.prev = prev

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Mark as most recently used
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            # Remove old node
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node

        # Add as most recently used
        self.insert(node)

        # If capacity exceeded
        if len(self.cache) > self.capacity:
            # Remove least recently used node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]