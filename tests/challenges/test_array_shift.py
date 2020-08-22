from data_structures_and_algorithms.challenges.array_shift.array_shift import insert_shift_array

def test_arr_shift():
   actual = insert_shift_array([2,4,6,8],5)
   expected = [2,4,5,6,8]
   assert actual == expected

def test_arr_shift2():
    actual = insert_shift_array([4,8,15,23,42],16)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_arr_shift3():
    actual= insert_shift_array([1,5,10,15],20)
    expected = [20,1,5,10,15]
    assert actual != expected

def test_none_value():
    actual = insert_shift_array([1,2,3,4,5],None)
    expected = [1,2,3,4,5]
    assert expected == actual
def test_empty_array():
    actual = insert_shift_array([],5)
    expected = [5]
    assert actual == expected
def test_empty_none():
    actual = insert_shift_array([],None)
    expected = []
    assert actual == expected
