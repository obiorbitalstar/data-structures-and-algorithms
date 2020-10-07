from data_structures_and_algorithms.challenges.depth_first.depth_first import graph_dfs


def test_returning_the_correct_path():
     graph = {"A": ["B", "C", "D"],
             "B": ["E"],
             "C": ["F", "G"],
             "D": ["H"],
             "E": ["I"],
             "F": ["J"]}

     actual = graph_dfs(graph, "A")
     expected = ['A', 'B', 'E', 'I', 'C', 'F', 'J', 'G', 'D', 'H']
     assert actual == expected

def test_pasing_empty_graph():
    potato={}
    actual = graph_dfs(potato,'A',path=[])
    expected = ['A']
    assert expected == actual

# no edge cases in mind



