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
            return f"PseudoQueue is empty"


    def peek(self):
        """
        This will show the current top of the stack
        """
        try:
            return self.top.data
        except AttributeError as e:
            return "PseudoQueue is empty"

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


class PseudoQueue:
    """
    a Queue like class where u add to the end of the stack and
     remove elements from the front

    """

    def __init__(self):
        self.en = Stack()
        self.de = Stack()

    def enqueue(self, data):
        """
        insert a value to the front of the Queue
        """
        if data == None:
            return "Not a valid input"
        self.en.push(data)
        return self.en

    def dequeue(self):
        """
        Remove a value from the end of the Queue
        """

        pointer = self.en.top
        while pointer:
            value_to_queue = self.en.pop()
            self.de.push(value_to_queue)
            pointer = pointer.next

        holder = self.de.pop()

        pointer = self.de.top
        while pointer:
            value_back_to_stack = self.de.pop()
            self.en.push(value_back_to_stack)
            pointer = pointer.next
        return holder

    def peek(self):
        if self.en.is_empty():
            return False
        else:
          return True


if __name__ == '__main__':

    p_q = PseudoQueue()
    p_q.enqueue(20)
    p_q.enqueue(15)
    p_q.enqueue(10)
    p_q.enqueue(5)

    print(p_q.dequeue())
