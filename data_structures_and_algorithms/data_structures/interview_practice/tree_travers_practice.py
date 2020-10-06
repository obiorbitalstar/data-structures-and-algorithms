class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    in order -->  left --> root -- > right

    pre order --> root --> left -- > right

    post order -->  left --> right --> root

    """

    def __init__(self):
        self.root = None

    def in_order(self, start=None, arr=None):

        if arr is None:
            arr = []

        if start:
            arr = self.in_order(start.left)
            arr.append(start.value)
            arr += self.in_order(start.right)
        return arr

    def post_order(self,start):
        arr = []
        if start:
            arr = self.post_order(start.left)
            arr += self.post_order(start.right)
            arr.append(start.value)
        return arr

        """
            1
          /    \
         2       4

         2  4  1

        """

    def pre_order(self,start):
        arr = []
        if start:
            arr.append(start.value)
            self.pre_order(start.left)
            self.pre_order(start.right)
        return arr


def maxDepth(node):
    if node is None:
        return 0 ;

    else :

        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(4)
    print(tree.in_order(tree.root))
    print(tree.post_order(tree.root))
    print(tree.pre_order(tree.root))
    print(maxDepth(tree.root))
