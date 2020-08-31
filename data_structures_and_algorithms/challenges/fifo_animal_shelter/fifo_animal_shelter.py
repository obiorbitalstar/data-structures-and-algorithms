class AnimalShelter :
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.front = None
        self.rear=None

    def enqueue(self,name):
        if self.front==None:
            self.front=name
            self.rear=name
        else:
            temp=self.rear
            self.rear=name
            self.rear.next=temp
            temp.previous=self.rear



    def dequeue(self,ttype):
        if self.front==None and self.rear==None:
            return None

        end=self.rear

        if end.type==ttype:
            temp=self.rear
            self.rear=self.rear.next
            self.rear.previous=None
            return temp.name

        current=self.front

        if  current.type==ttype:
            temp=self.front
            self.front=self.front.previous
            self.front.next=None
            return temp.name
        while current:
            if current.type==ttype:
                temp=current.next
                temp.previous=current.previous
                current.previous.next=temp
                return current.name
            current=current.previous
        return None


class Dog(AnimalShelter):
    def __init__(self,dog_name):
        self.name=dog_name
        self.type='Dog'

class Cat(AnimalShelter):
    def __init__(self,cat_name):
        self.name=cat_name
        self.type='Cat'




if __name__ == "__main__":

    potato = AnimalShelter('oscar',Dog('oscar'))
    print(potato)
