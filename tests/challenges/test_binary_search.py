from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import BinarySearch

def test_binary_true():
    actual = BinarySearch([ 2, 3, 4, 10, 40 ,50,60,70,80], 40)
    expected = 4
    assert actual == expected

def test_binary_false():
    actual = BinarySearch([ 2, 3, 4, 10, 40 ,50,60,70,80], 100)
    expected = -1
    assert expected ==actual

def test_binary_odd():
    actual = BinarySearch([],1)
    expected = -1
    assert actual == expected
