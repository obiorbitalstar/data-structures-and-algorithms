class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """
    Put docstring here
    """

    # put your LinkedList implementation here
    def __init__(self):
        self.head = Node()

    def __str__(self):
        elements = []
        current = self.head
        while current.next != None:
            current = current.next
            elements.append(current.data)
        print(''.join("{} -> ".format(*k) for k in enumerate(elements))+'NULL')
    def display(self):
        elements = []
        current = self.head
        while current.next != None:
            current = current.next
            elements.append(current.data)
        return elements

    def insert(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total

    def includes(self, value):
        current_node = self.head
        while current_node.next != None:
            if current_node.data == value:
                return True
            else:
                current_node = current_node.next
        return False
    def get(self,index):
        if index == self.length():
            raise Exception("Index is out of range")
            return None
        current_index = 0
        current_node =self.head
        while True:
            current_node=current_node.next
            if current_index == index:return current_node.data
            current_index+=1

    def erase(self, index):
        if index >= self.length():
            raise Exception("this index is out of range")
            return None
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1


if __name__ == "__main__":
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)
    my_list.insert(4)
    my_list.insert(5)
    print(my_list.includes(3))
    print(my_list.includes(7))
    my_list.__str__()
    print(my_list.get(0))
