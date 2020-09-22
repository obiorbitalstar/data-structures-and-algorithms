from data_structures_and_algorithms.challenges.quick_sort.quick_sort import quick_sort

def test_sort_normal_list():
    x=[8,4,23,42,16,15]
    n=len(x)
    expected =[4, 8, 15, 16, 23, 42]
    actual = quick_sort(x,0,n-1)
    assert expected == x


def test_sort_reversed_list():
    x =[20,18,12,8,5,-2]
    n=len(x)
    expected = [-2, 5, 8, 12, 18, 20]
    actual = quick_sort(x,0,n-1)
    assert expected == x


def test_empty_list():
    x= []
    n= len(x)
    expected = 'This list is empty'
    actual = quick_sort(x,0,n-1)
    assert expected == actual
