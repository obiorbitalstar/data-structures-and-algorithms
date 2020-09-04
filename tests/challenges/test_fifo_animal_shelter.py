from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter
def test_addeing_animal():
    new_shelter =AnimalShelter()
    new_shelter.enqueue('Oscar','dog')
    actual = new_shelter.dog.__str__()
    expected = 'Oscar-> None'
    assert expected == actual
def test_dequeue_works_correctly_there_is_dogs_and_cats():
    new_shelter = AnimalShelter()
    new_shelter.enqueue('Oscar','dog')
    new_shelter.enqueue('Sherry','cat')
    actual = new_shelter.dequeue('dog')
    expected = 'Oscar'
    assert expected == actual
def test_dequeue_to_a_value_other_than_cat_or_dog():
    new_shelter=AnimalShelter()
    actual =new_shelter.dequeue('potato')
    expected = None
    assert expected == actual
