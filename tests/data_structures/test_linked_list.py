from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList
import pytest


@pytest.fixture
def data():
    linked_list = LinkedList()
    return {'list': linked_list}


def test_empty(data):
    actual = data['list'].__str__()
    expected = None
    assert actual == expected


def test_insert(data):
    actual = data['list'].insert(1)
    expected = 1
    assert expected == data['list'].length()


def test_head(data):
    # The .get is a function i made to get the value given an index ,at index 0 is the head , i entered the first value and checked index of 0
    head = data['list'].insert('firstEntry')
    expected = 'firstEntry'
    assert expected == data['list'].get(0)


def test_multi_input(data):
    # length is a method i made to check the length of a linked list
    data['list'].insert(1)
    data['list'].insert(2)
    data['list'].insert(3)
    data['list'].insert(4)
    actual = data['list'].length()
    expected = 4
    assert actual == expected


def test_finiding_value(data):
    data['list'].insert(1)
    data['list'].insert(2)
    data['list'].insert(3)
    actual = data['list'].includes(2)
    expected = True
    assert expected == actual


def test_dont_exists(data):
    data['list'].insert(1)
    data['list'].insert(2)
    actual = data['list'].includes(5)
    expected = False
    assert expected == actual


def test_print_all(data):
    data['list'].insert(1)
    data['list'].insert(2)
    data['list'].insert(3)
    data['list'].insert(4)
    data['list'].insert(5)
    expected = [1, 2, 3, 4, 5]
    actual = data['list'].display()
    assert expected == actual
