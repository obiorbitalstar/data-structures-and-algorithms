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
        if traversal_type == "preorder":
            return self.pre_order(self.root, "")
        elif traversal_type == "inorder":
            return self.in_order(self.root, "")
        elif traversal_type == "postorder":
            return self.post_order(self.root, "")
        elif traversal_type == 'breadthfirst':
            return self.breadth_first(self.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def pre_order(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal

    def in_order(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.in_order(start.right, traversal)
        return traversal

    def post_order(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.post_order(start.left, traversal)
            traversal = self.post_order(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
    def find_maximum_value(self):
            """ return the max value inside a tree """
            lol = self.print_tree('preorder')
            if lol == None or lol == "None-":
                return "Value dose not exist in the tree"
            else:
                x= lol.split('-')
                y= x.remove('')
                max = 0
                for i in range(len(x)):
                    if int(x[i]) > max:
                        max = int(x[i])
                return max
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

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._add(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._add(value, cur_node.right)
        else:
            print("Value already exists")

    def contains(self, value):
        if self.root:
            is_found = self._contains(value, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _contains(self, value, cur_node):
        if value > cur_node.value and cur_node.right:
            return self._contains(value, cur_node.right)
        if value < cur_node.value and cur_node.left:
            return self._contains(value, cur_node.left)
        if value == cur_node.value:
            return True

if __name__ == "__main__":

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print(tree.print_tree('breadthfirst'))
    # print(tree.print_tree("preorder"))
    # print(tree.print_tree("inorder"))
    # print(tree.print_tree("postorder"))
    print(tree.find_maximum_value())
    # bst = BinarySearchTree()
    # bst.add(1)
    # bst.add(2)
    # bst.add(3)
    # bst.add(4)
    # print(bst.contains(3))
