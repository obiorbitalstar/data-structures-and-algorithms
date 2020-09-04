class Node:
    """
    to initiate a node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """
    You just created a new stack
    """
    def __init__(self):
        self.top = None


    def push(self, data):
        """
        Add a new value to the stack
        """
        node = Node(data)
        temp = self.top
        self.top = node
        self.top.next = temp

    def pop(self):

        """
        Remove a value from the top of the stack
        """

        if self.top:
            popped = self.top
            self.top = self.top.next
            return popped.data
        else:
            return f"Stack is empty"


    def peek(self):
        """
        This will show the current top of the stack
        """
        try:
            return self.top.data
        except AttributeError as e:
            return "Stack is empty"

    def is_empty(self):
        """
        to check if the stack is empty or not
        """
        if self.top:
            return False
        else :
            return True

    def __str__(self):
        """
        Show the stack elements
        """
        pointer = self.top
        elements = ''
        while pointer:
            elements += f"{pointer.data}-> "
            pointer = pointer.next
        elements += f"{pointer}"
        return elements


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.elements =[]
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear == None:
            self.front = self.rear = new_node
            self.elements.append(new_node.data)
            return

        self.rear.next = new_node
        self.rear = new_node
        self.elements.append(new_node.data)

    def dequeue(self):
        try:
            temp = self.front
            self.front = temp.next
            if self.front == None:
               self.rear = None
            self.elements.pop(0)
            return temp.data
        except AttributeError as e:
            return "Queue is empty"

    def peek(self):
        try:
            return self.front.data
        except AttributeError as e:
            return "Queue is empty"


    def __str__(self):
        """
        Show the queue elements
        """
        pointer = self.front
        elements = ''
        while pointer:
            elements += f"{pointer.data}-> "
            pointer = pointer.next
        elements += f"{pointer}"
        return elements

    def is_empty(self):
       if not self.front:
           return True
       else :
           return False


if __name__ == "__main__":
    # new_stack = Stack()
    # new_stack.push(1)
    # new_stack.push(2)
    # new_stack.push(3)
    # new_stack.push(4)
    # # print(new_stack.elements)
    # # print(new_stack.peek())
    # print(new_stack.__str__())
    # new_stack.pop()
    # new_stack.pop()
    # print(new_stack.__str__())
    new_queue=Queue()
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    print(new_queue.__str__())
    print(new_queue.dequeue())
    print(new_queue.__str__())
    print(new_queue.dequeue())
    print(new_queue.__str__())
    print(new_queue.dequeue())
    print(new_queue.__str__())
    new_queue.dequeue()
    new_queue.dequeue()
    print(new_queue.dequeue())
    print(new_queue.__str__())
