class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.elements=[]

    def push(self, data):
        if self.top == None:
            self.top = Node(data)
            self.elements.append(data)
        else:
            new_node = Node(data)
            self.top.next = new_node
            self.top = new_node
            self.elements.append(new_node.data)

    def pop(self):
        try:
            popped = self.top
            self.top = self.top.next
            popped.next = None
            return popped.data
        except AttributeError as e:
            return 'Stack is empty'

    def peek(self):
        try:
            return self.top.data
        except AttributeError as e:
            return "Stack is empty"

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False
    # def display(self):

    #     return elements
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
        except AttributeError as e:
            return "Queue is empty"

    def peek(self):
        try:
            return self.front.data
        except AttributeError as e:
            return "Queue is empty"

    def is_empty(self):
       if not self.front:
           return True
       else :
           return False


if __name__ == "__main__":
    new_stack = Stack()
    new_stack.push(1)
    new_stack.push(2)
    new_stack.push(3)
    new_stack.push(4)
    print(new_stack.elements)
    print(new_stack.peek())
    print(new_stack.pop())
    # print(new_stack.peek())
    # print(new_stack.pop())
    # print(new_stack.peek())
    # print(new_stack.is_empty())
    # q = Queue()
    # q.enqueue(10)
    # q.enqueue(20)
    # q.dequeue()
    # q.dequeue()
    # q.enqueue(30)
    # q.enqueue(40)
    # q.enqueue(50)
    # print(q.dequeue())
    # print(q.peek())
    # print("Queue Front " + str(q.front.data))
    # print("Queue Rear " + str(q.rear.data))
