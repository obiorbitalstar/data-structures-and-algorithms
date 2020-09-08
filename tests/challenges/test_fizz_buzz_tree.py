from data_structures_and_algorithms.challenges.fizz_buzz_tree.fizz_buzz_tree import fizz_buzz_tree,BinaryTree,Node
import pytest

@pytest.fixture
def data():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(15)

    empty_tree= BinaryTree()
    return {'tree':tree,'etree':empty_tree}




def test_fizz_buzz_fizzbuzz_add_correctly(data):
    assert fizz_buzz_tree(data['tree']) == ['1', '2', '4', 'Buzz', 'Fizz', 'Fizz', 'FizzBuzz']

def test_if_tree_is_empty(data):
    assert fizz_buzz_tree(data['etree']) == "Tree is empty"


# i dont have any edge cases in mind for this one
