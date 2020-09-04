from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks import PseudoQueue

def test_happy_path():
    pseudo_q=PseudoQueue()
    pseudo_q.enqueue(20)
    pseudo_q.enqueue(15)
    pseudo_q.enqueue(10)
    pseudo_q.enqueue(5)
    actual = pseudo_q.en.__str__()
    expected = '5-> 10-> 15-> 20-> None'
    assert expected == actual

def test_failure_case():
    pseudo_q=PseudoQueue()
    assert pseudo_q.dequeue() == "PseudoQueue is empty"

def test_edge_case():
    pseudo_q = PseudoQueue()
    assert pseudo_q.enqueue(None) == "Not a valid input"
