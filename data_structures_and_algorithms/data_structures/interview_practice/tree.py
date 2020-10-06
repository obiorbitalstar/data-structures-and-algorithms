
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


def in_order(start):
        arr = []
        if start:
            arr += in_order(start.left)
            arr.append(start.value)
            arr += in_order(start.right)
        return arr


def merge_two_trees(tree1, tree2):
    """
    Input:
        Tree 1            Tree 2
            2                 3
           / \               / \
          1   4             6   1
         /                   \   \
        5                     2   7

    Output: Merged tree:
         5
        / \
       7   5
      / \   \
     5   2   7
    """
    if (not tree1):
        return tree2
    if (not tree2):
        return tree1

    tree1.value += tree2.value
    tree1.left = merge_two_trees(tree1.left, tree2.left)
    tree1.right = merge_two_trees(tree1.right, tree2.right)

    return tree1


def maxDepth(node):
    """
                maxDepth('1') = max(maxDepth('2'), maxDepth('3')) + 1
                                        = 2 + 1
                                            /    \
                                            /         \
                                        /             \
                                        /                 \
                                    /                     \
                        maxDepth('2') = 1                maxDepth('3') = 1
            = max(maxDepth('4'), maxDepth('5')) + 1
            = 1 + 1   = 2
                            /    \
                            /        \
                        /            \
                        /                \
                    /                    \
            maxDepth('4') = 1     maxDepth('5') = 1


     """
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



def is_full_tree(root):
    """
    To check whether a binary tree is a full binary tree we need to test the following cases:-

    1) If a binary tree node is NULL then it is a full binary tree.
    2) If a binary tree node does have empty left and right sub-trees, then it is a full binary tree by definition.
    3) If a binary tree node has left and right sub-trees, then it is a part of a full binary tree by definition. In this case recursively check if the left and right sub-trees are also binary trees themselves.
    4) In all other combinations of right and left sub-trees, the binary tree is not a full binary tree.
    """
    # If empty tree
    if root is None:
        return True

    # If leaf node
    if root.left is None and root.right is None:
        return True

    # If both left and right subtress are not None and
    # left and right subtress are full
    if root.left is not None and root.right is not None:
        return (is_full_tree(root.left) and is_full_tree(root.right))

    # We reach here when none of the above if condiitions work
    return False

 # min value in Binary Search Tree

class BinarySearchTree:
    def __init__(self):
         self.root = None

    def insert(self,value):
         if self.root == None:
            self.root=Node(value)
         else:
            self._insert(value,self.root)

    def _insert(self,value,cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already exists")



    def find_min_node(self):
        """This is quite simple. Just traverse the node from root to left recursively until left is NULL. The node whose left is NULL is the node with minimum value.

        """
        if self.root is None:
            return 0
        else:
            current = self.root
            while current.left is not None:
                current = current.left
            return current.value

    def find_max_node(self):
        """Same as min find min value but go right instead of left"""
        if self.root is None:
            return 0
        else:
            current = self.root
            while current.right is not None:
                current = current.right
            return current.value

if __name__ == "__main__":
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.right = Node(6)


    root2 = Node(4)
    root2.left = Node(1)
    root2.right = Node(7)
    root2.left.left = Node(3)
    root2.right.left = Node(2)
    root2.right.right = Node(6)

    root3 = merge_two_trees(root1, root2)
    print("The Merged Binary Tree is:")
    print(in_order(root3))
    print ("Height of tree is %d" %(maxDepth(root1)))

    print ("#----------(BST)------------#")
    tree4 = BinarySearchTree()
    tree4.insert(9)
    tree4.insert(1)
    tree4.insert(2)
    tree4.insert(3)
    tree4.insert(4)
    tree4.insert(11)
    tree4.insert(5)
    tree4.insert(7)
    tree4.insert(10)

    print(tree4.find_min_node())
    print(tree4.find_max_node())
