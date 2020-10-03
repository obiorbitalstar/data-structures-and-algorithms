from data_structures_and_algorithms.data_structures.graph.graph import Graph


def test_node_can_be_added_to_graph():
    g = Graph()
    g.add_node('a')
    actual = g.get_nodes()
    expected = {'a': []}
    assert expected == actual

def test_edge_added_to_graph():
    g=Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_edge('a', 'b', 1)

    actual = g.get_neighbors('a')
    expected = 'a --> b edge weight: 1'
    assert actual == expected

def test_collection_of_nodes_properly_retrived():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    actual = g.get_nodes()
    expected = {'a': [],'b': [],'c': []}
    assert expected == actual

def test_all_neighbors_can_be_retrived():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')

    g.add_edge('a', 'b', 1)
    g.add_edge('a', 'd', 3)
    g.add_edge('b', 'd', 4)
    g.add_edge('d', 'd', 6)
    g.add_edge('d', 'a', 5)
    actual = g.get_nodes()
    expected = {'a': [['b', 1], ['d', 3]], 'b': [['d', 4]], 'c': [], 'd': [['d', 6], ['a', 5]]}
    assert expected == actual

def test_all_neighbors_can_be_retrived_with_weight():
    g = Graph()
    g.add_node('a')
    g.add_node('b')

    g.add_edge('a','b',4)

    actual = g.get_neighbors('a')
    expected = 'a --> b edge weight: 4'

    assert expected == actual

def test_proper_size_is_returned():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')

    actual = g.size()
    expected = 4
    assert expected == actual

def test_one_node_one_edge():
    g = Graph()
    g.add_node('a')

    g.add_edge('a','a')
    actual = g.get_neighbors('a')
    expected = 'a --> a edge weight: 1'
    assert expected == actual
def test_empty_graph_return_none():
    g = Graph()
    actual = g.get_nodes()
    excepted = None
    assert excepted == actual

