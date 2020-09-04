from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack,Queue
import pytest

@pytest.fixture
def data():
    new_stack = Stack()
    new_queue = Queue()
    return {'stack':new_stack,'queue':new_queue}


def test_stack_push_one_element(data):
    data['stack'].push(1)
    actual = data['stack'].top.data
    expected = 1
    assert actual == expected
def test_stack_push_multiple_elements(data):
    data['stack'].push(1)
    data['stack'].push(2)
    data['stack'].push(3)
    actual= data['stack'].__str__()
    expected = '3-> 2-> 1-> None'
    assert expected == actual
def test_stack_pop_one_element(data):
    data['stack'].push(1)
    data['stack'].push(2)
    actual = data['stack'].pop()
    expected = 2
    assert expected == actual
def test_stack_multipl_pop(data):
    data['stack'].push(1)
    data['stack'].push(2)
    data['stack'].pop()
    data['stack'].pop()
    actual = data['stack'].top
    expected = None
    assert expected == actual
def test_stack_peek(data):
    data['stack'].push(1)
    data['stack'].push(2)
    actual = data['stack'].peek()
    expected = 2
    assert expected == actual
def test_start_empty_stack(data):
    actual =data['stack'].top
    expected = None
    assert expected == actual
def test_stack_pop_peek_empty(data):
    actual1 = data['stack'].pop()
    actual2 =data['stack'].peek()
    expected = 'Stack is empty'
    assert expected == actual1 == actual2

def test_queue_enqueue_one_element(data):
    data['queue'].enqueue(1)
    actual = data['queue'].front.data
    excpected = 1
    assert excpected == actual

def test_queue_enqueue_multiple_elemements(data):
    data['queue'].enqueue(1)
    data['queue'].enqueue(2)
    data['queue'].enqueue(3)
    actual = data['queue'].elements
    excpected = [1,2,3]
    assert excpected == actual

def test_queue_dequeue(data):
    data['queue'].enqueue(1)
    data['queue'].enqueue(2)
    data['queue'].dequeue()
    actual = data['queue'].rear.data
    expected = 2
    assert expected == actual

def test_queue_peek(data):
    data['queue'].enqueue(1)
    actual = data['queue'].peek()
    expected = 1
    assert expected == actual

def test_queue_empty_after_multi_dequeue(data):
    data['queue'].enqueue(1)
    data['queue'].enqueue(2)
    data['queue'].enqueue(3)
    data['queue'].dequeue()
    data['queue'].dequeue()
    data['queue'].dequeue()
    actual = data['queue'].front
    expected = None
    assert expected == actual

def test_queue_starts_empty(data):
    actual = data['queue'].front
    expected = None
    assert expected == actual

def test_queue_pop_peek_on_empty_raises_excpetion(data):
    actual1 = data['queue'].peek()
    actual2 = data['queue'].dequeue()
    expected = 'Queue is empty'
    assert expected == actual1 == actual1

