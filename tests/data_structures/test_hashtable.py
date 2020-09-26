from data_structures_and_algorithms.data_structures.hashtable.hashtable import HashTable


def test_add_key_value_in_data_structure():
    table = HashTable()
    table.add('silent', 'listen')
    actual = table.contains('silent')
    expected = True
    assert expected == actual


def test_get_value_from_key():
    table = HashTable()
    table.add('potato', 'ketchup')
    actual = table.get('potato')
    expected = 'ketchup'
    assert expected == actual


def test_return_null_if_value_dose_not_exist():
    table = HashTable()
    actual = table.get('somthing')
    expected = None
    assert expected == actual


def test_collision():
    table = HashTable()
    table.add('potato', 'ketchup')
    table.add('potato', 'fries')
    actual = table.get('potato')
    expected = 'ketchup'
    assert expected == actual


def test_hash_key():
    table = HashTable()
    actual = table.hash('jump')
    expected = 502
    assert expected == actual


def test_retrieve_value_with_collsion():
    table = HashTable()
    table.add('potato', 'ketchup')
    table.add('potato', 'fries')
    actual = table.get('potato')
    expected = 'ketchup'
    assert expected == actual
