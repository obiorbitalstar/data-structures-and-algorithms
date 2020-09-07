from data_structures_and_algorithms.data_structures.tree.tree import BinarySearchTree,BinaryTree,Node


def test_if_this_is_conntected():
    new_tree = BinaryTree()
    assert new_tree.root.value == None
def test_instantiate_tree_with_single_root_node():
    tree = BinaryTree(1)
    assert tree.root.value == 1
def test_add_left_and_right_childeren_to_a_node():
    tree =BinaryTree()
    left =tree.root.left = Node(2)
    right =tree.root.right = Node(3)
    assert  tree.root.left.value == 2
    assert tree.root.right.value == 3
def test_pre_order_traversal():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    assert tree.print_tree("preorder") == '1-2-4-5-3-6-7-'
def test_in_order_traversal():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    assert tree.print_tree("inorder") == '4-2-5-1-6-3-7-'
def test_post_order_traversal():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    assert tree.print_tree("postorder") == '4-5-2-6-7-3-1-'

def test_find_max_value():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    assert tree.find_maximum_value() == 7

def test_find_max_value_for_empty_tree():
    tree = BinaryTree()
    assert tree.find_maximum_value() == "Value dose not exist in the tree"

def test_breadth_first_correct_order():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    assert tree.print_tree('breadthfirst') == [1, 2, 3, 4, 5, 6, 7]
