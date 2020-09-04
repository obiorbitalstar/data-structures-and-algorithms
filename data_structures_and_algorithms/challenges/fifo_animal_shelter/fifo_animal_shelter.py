class AnimalShelter :
    def __init__(self):
      self.dog = Queue()
      self.cat = Queue()

    def enqueue(self,name,kind):
        if kind == 'dog':
            self.dog.enqueue(name)
        else:
            self.cat.enqueue(name)



    def dequeue(self,kind):

       if kind == 'dog':
           return self.dog.dequeue()
       elif kind =='cat':
           return self.cat.dequeue()
       else:
            return None



class Dog(AnimalShelter):
    pass


class Cat(AnimalShelter):
    pass

class Node:
    """
    to initiate a node
    """
    def __init__(self, data):
        self.data = data
        self.next = None

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
    pref1,pref2 = 'dog' ,'cat'
    potato = AnimalShelter()
    potato.enqueue('Oscar','dog')
    potato.enqueue('Sherry','cat')
    potato.enqueue('roro','cat')
    potato.enqueue('kaji','cat')
    potato.enqueue('naruto','cat')
    potato.enqueue('sasuke','dog')

    print(potato.dequeue('dog'))
    print(potato.dequeue('cat'))
    print(potato.cat.__str__() , potato.dog.__str__() , sep='  ')
    print(potato.dequeue('dog'))
