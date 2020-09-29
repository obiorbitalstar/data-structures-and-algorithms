class Queue:
    def __init__(self):
        self.items =[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) ==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'breadthfirst':
            return self.breadth_first(self.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def breadth_first(self,start):
            if start is None:
                return
            queue = Queue()
            queue.enqueue(start)
            traversal = []
            while len(queue)>0:
                traversal.append(queue.peek())
                node = queue.dequeue()
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            return traversal

def tree_intersection(t1,t2):
    if t1.root is None or t2.root is None:
        return f'One of the trees is empty so no intersections'
    first_tree = t1.print_tree('breadthfirst')
    second_tree = t2.print_tree('breadthfirst')
    intersectted =[]
    for i,c in enumerate(first_tree):
        if first_tree[i] == second_tree[i]:
          intersectted.append(c)
        else:
            continue
    return intersectted

if __name__ == "__main__":
    tree = BinaryTree(150)
    tree.root.left = Node(100)
    tree.root.right = Node(250)
    tree.root.left.left = Node(75)
    tree.root.left.right = Node(160)
    tree.root.left.right.left=Node(125)
    tree.root.left.right.right = Node(175)
    tree.root.right.left = Node(200)
    tree.root.right.right = Node(350)
    tree.root.right.right.Left=Node(300)
    tree.root.right.right.right=Node(500)


    tree2 = BinaryTree(42)
    tree2.root.left = Node(100)
    tree2.root.right = Node(600)
    tree2.root.left.left = Node(15)
    tree2.root.left.right = Node(160)
    tree2.root.left.right.left=Node(125)
    tree2.root.left.right.right = Node(175)
    tree2.root.right.left = Node(200)
    tree2.root.right.right = Node(350)
    tree2.root.right.right.Left=Node(4)
    tree2.root.right.right.right=Node(500)


    print(tree.print_tree('breadthfirst'))
    print(tree2.print_tree('breadthfirst'))
    print(tree_intersection(tree,tree2))
