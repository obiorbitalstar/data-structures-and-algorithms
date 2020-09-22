from data_structures_and_algorithms.challenges.merge_sort.merge_sort import merge_sort

def test_sort_normal_list():
    x=[8,4,23,42,16,15]
    expected =[4, 8, 15, 16, 23, 42]
    actual = merge_sort(x)
    assert expected == actual


def test_empty_list():
    x= []
    expected = 'This list is empty'
    actual = merge_sort(x)
    assert expected == actual
