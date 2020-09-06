class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Put docstring here
    """

    # put your LinkedList implementation here
    def __init__(self):
        self.head = None

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
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def appened(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, data, new_val):

        new_node = Node(new_val)
        current = self.head
        if not self.head:
            self.head = new_node
        else:
            if self.head.data == data:
                previous_node = self.head
                self.head = new_node
                new_node.next = previous_node
                return
            else:
                current = self.head
            while current.next != None:
                if current.next.data == data:
                    previous_node = current.next
                    current.next = new_node
                    new_node.next = previous_node
                    return
                else:
                    current = current.next



    def insert_after(self,data,new_val):

        new_node = Node(new_val)
        current = self.head
        if not self.head:
                self.head = new_node
        else:
            current = self.head
            while current.next != None:
                if current.next.data == data:
                    current = current.next
                    previous_node = current.next
                    current.next = new_node
                    new_node.next = previous_node
                    return
                else:
                    current = current.next

    def length(self):
        current = self.head
        total = 0

        while current:
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

    def get(self, index):
        if index == self.length():
            raise Exception("Index is out of range")
            return None
        current_index = 0
        current_node = self.head
        while True:
            if current_index == index:
                return current_node.data
            current_index += 1
            current_node = current_node.next

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

    def reverse_list(self):
        prev = None
        cure = self.head
        while cure:
            nxt = cure.next
            cure.next = prev
            prev = cure
            cure = nxt
        self.head = prev
    # @staticmethod

    def kth_from_end(self, index):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        if index > len(elements) or index <= -1:
            return f"{index} is not in the range of the list"
        elif index == len(elements):
            return elements[index-1]
        elements.reverse()
        return elements[index]




if __name__ == "__main__":
    list_1 = LinkedList()
    list_2 = LinkedList()

    list_1.appened(1)
    list_1.appened(3)
    list_1.appened(2)

    list_2.appened(5)
    list_2.appened(9)

    list_1.zip_lists(list_2)
    print(list_1.display())
