INITIAL_CAPACITY = 1024


class Node:
    """
    This is a node class altred to be used in hash table
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)

    def __repr__(self):
        return str(self)


class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None]*self.capacity

    def hash(self, key):
        """Hashes a given string to use as index

        Args:
            key (String): The value you want to switch to index

        Returns:
            [intger]: The value of the string switched into intger to use as index
        """
        hashsum = 0
        for idx, c in enumerate(key):
            # Add (index + length of key) ^ (current char code)
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    def add(self, key, value):
        """Adds a new value to the hashtable

        Args:
            key (String): To point at the value you want
            value (Anything): Any value you want to store
        """
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def get(self, key):
        """Returns a value based on key

        Args:
            key (String): The key you used to store a value

        Returns:
            Anything: The value linked to the given key, or null if the value dose not exist
        """
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def contains(self, key):
        """check if the value exists in the table or not

        Args:
            key (String): The key you used to store values

        Returns:
            Boolean: True if value exists and false if not
        """
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return False
        else:
            return True


if __name__ == "__main__":
    table = HashTable()
    print(table.hash('silent'))
    table.add('silent', 'listen')
    table.add('tomato', 'tomoto')
    print(table.get('silent'))
    print(table.contains('potato'))
