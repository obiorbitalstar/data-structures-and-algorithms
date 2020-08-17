from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray

def test_arr_shift():
   actual = insertShiftArray([2,4,6,8],5)
   expected = [2,4,5,6,8]
   assert actual == expected

def test_arr_shift2():
    actual = insertShiftArray([4,8,15,23,42],16)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_arr_shift3():
    actual= insertShiftArray([1,5,10,15],20)
    expected = [20,1,5,10,15]
    assert actual != expected

