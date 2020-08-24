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
    def insert_before(self,next_node,data):

        if not next_node:
            print('node dose not exist')
            return
        new_node=Node(data)
        current_node=self.head
        if next_node == current_node:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        while current_node:
            if current_node.next==next_node:
                new_node.next=current_node.next
                current_node.next=new_node
                return
            else:
                current_node=current_node.next

    def insert_after(self, prev_node,data):
        if not prev_node:
            print('The previous node is not in the list')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next=new_node



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
    my_list.appened(1)
    my_list.appened(2)
    my_list.appened(3)
    my_list.appened(4)
    my_list.appened(5)
    print(my_list.display())
    y= my_list.head.next.next.next
    my_list.insert_after(y,6)
    print(my_list.display())
    my_list.insert_before(my_list.head.next.next.next,'a')
    print(my_list.display())

