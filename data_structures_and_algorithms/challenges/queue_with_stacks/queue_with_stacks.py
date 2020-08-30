class PseudoQueue:
    def __init__(self):
        self.elements=[]

    def enqueue(self,data):
        if data == None:
            return "Not a valid input"
        else:
            self.elements.insert(0,data)

    def dequeue(self):
        if len(self.elements) == 0:
            return "PseudoQueue is empty"
        else:
            return self.elements.pop()
    def peek(self):
        if len(self.elements) == 0:
            return "PseudoQueue is empty"
        else:
            return self.elements[len(self.elements)-1]
    def is_empty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False


if __name__ == '__main__':

    ch11 = PseudoQueue()
    ch11.enqueue(20)
    ch11.enqueue(15)
    ch11.enqueue(10)
    ch11.enqueue(5)
    print(ch11.elements)
    ch11.dequeue()
    print(ch11.elements)
