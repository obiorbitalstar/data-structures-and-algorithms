from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList
import pytest


@pytest.fixture
def data():
    linked_list = LinkedList()
    return {'list': linked_list}


def test_empty(data):
    actual = data['list'].length()
    expected = 0
    assert actual == expected


def test_insert(data):
    actual = data['list'].appened(1)
    expected = 1
    assert expected == data['list'].length()


def test_head(data):
    # The .get is a function i made to get the value given an index ,at index 0 is the head , i entered the first value and checked index of 0
    head = data['list'].appened('firstEntry')
    expected = 'firstEntry'
    assert expected == data['list'].head.data

def test_multi_input(data):
    # length is a method i made to check the length of a linked list
    data['list'].appened(1)
    data['list'].appened(2)
    data['list'].appened(3)
    data['list'].appened(4)
    actual = data['list'].length()
    expected = 4
    assert actual == expected


def test_finiding_value(data):
    data['list'].appened(1)
    data['list'].appened(2)
    data['list'].appened(3)
    actual = data['list'].includes(2)
    expected = True
    assert expected == actual


def test_dont_exists(data):
    data['list'].appened(1)
    data['list'].appened(2)
    actual = data['list'].includes(5)
    expected = False
    assert expected == actual


def test_print_all(data):
    data['list'].appened(1)
    data['list'].appened(2)
    data['list'].appened(3)
    data['list'].appened(4)
    data['list'].appened(5)
    expected = [1, 2, 3, 4, 5]
    actual = data['list'].display()
    assert expected == actual

def test_add_to_end_and_add_multi_to_end(data):
    data['list'].appened(1)
    data['list'].appened(2)
    data['list'].appened(3)
    data['list'].appened(4)
    data['list'].appened(5)
    actual = data['list'].display()
    expected = [1,2,3,4,5]
def test_add_to_middle(data):
    data['list'].appened(1)
    data['list'].appened(2)
    data['list'].appened(4)
    data['list'].appened(5)
    data['list'].appened(6)
    location = data['list'].head.next.next
    data['list'].insert_before(location,3)
    actual = data['list'].display()
    expected = [1,2,3,4,5,6]
    assert expected==actual
def test_add_to_first(data):
    data['list'].appened(1)
    data['list'].appened(2)
    location = data['list'].head
    data['list'].insert_before(location,5)
    actual = data['list'].display()
    expected = [5,1,2]
    assert expected == actual

def test_insert_after_middle(data):
    data['list'].appened(1)
    data['list'].appened(2)
    data['list'].appened(3)
    data['list'].appened(5)
    data['list'].appened(6)

    location = data['list'].head.next.next
    data['list'].insert_after(location,4)

    actual = data['list'].display()
    expected = [1,2,3,4,5,6]
    assert expected ==actual

def test_insert_after_last_node(data):
    data['list'].appened(1)
    data['list'].appened(2)
    location = data['list'].head.next
    data['list'].insert_after(location,3)
    actual = data['list'].display()
    expected = [1,2,3]
    assert expected == actual
def test_k_is_greater_than_list_length(data):
    data['list'].appened(1)
    data['list'].appened(2)
    data['list'].appened(3)
    data['list'].appened(5)
    actual = data['list'].kth_from_end(7)
    expected = '7 is not in the range of the list'
    assert expected == actual
def test_k_has_same_length_of_list(data):
    data['list'].appened(1)
    data['list'].appened(2)
    data['list'].appened(3)
    data['list'].appened(5)
    actual = data['list'].kth_from_end(4)
    expected = 5
    assert expected == actual
def test_k_is_negative(data):
    data['list'].appened(1)
    data['list'].appened(2)
    actual = data['list'].kth_from_end(-1)
    expected = '-1 is not in the range of the list'
    assert expected == actual
def test_list_length_is_one(data):
    data['list'].appened(1)
    actual = data['list'].kth_from_end(0)
    expected = 1
    assert expected == actual
def test_happy_path(data):
    data['list'].appened(1)
    data['list'].appened(2)
    data['list'].appened(3)
    data['list'].appened(4)
    data['list'].appened(5)
    data['list'].appened(6)
    actual = data['list'].kth_from_end(3)
    expected =3

    assert expected == actual
