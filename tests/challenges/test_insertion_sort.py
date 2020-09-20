from data_structures_and_algorithms.challenges.insertion_sort.insertion_sort import insertion_sort

def test_sort_normal_list():
    x=[8,4,23,42,16,15]
    expected =[4, 8, 15, 16, 23, 42]
    actual = insertion_sort(x)
    assert expected == actual


def test_sort_reversed_list():
    x =[20,18,12,8,5,-2]
    expected = [-2, 5, 8, 12, 18, 20]
    actual = insertion_sort(x)
    assert expected == actual


def test_empty_list():
    x= []
    expected = 'This list is empty'
    actual = insertion_sort(x)
    assert expected == actual
