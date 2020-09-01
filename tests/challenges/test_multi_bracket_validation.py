from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_happy_path():
    actual = multi_bracket_validation('[some string]')
    expected = True
    assert expected== actual

def test_fail():
    assert multi_bracket_validation('[') ==False

def test_edge():
    assert multi_bracket_validation('{)') == False

