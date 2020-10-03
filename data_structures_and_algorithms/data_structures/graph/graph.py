class Node:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        if value in self._adjacency_list:
            print('Vertex',value,' already exists')
        self._adjacency_list[node.value] = []

    def add_edge(self, start_node, end_node, weight=1):
        if start_node not in self._adjacency_list.keys():
           print("Vertex ", start_node, " does not exist.")
        elif end_node not in self._adjacency_list.keys():
            print("Vertex ", end_node, " does not exist.")
        else:
            temp = [end_node, weight]
            self._adjacency_list[start_node].append(temp)

    def get_nodes(self):
            # for vertex in self._adjacency_list:
            #   for edges in self._adjacency_list[vertex]:
            #        print(vertex, " -> ", edges[0], " edge weight: ", edges[1])
        if len(self._adjacency_list) == 0:
            return None
        else:
            return self._adjacency_list

    def get_neighbors(self, node):
        for edges in self._adjacency_list[node]:
               return f"{node} --> {edges[0]} edge weight: {edges[1]}"

    def size(self):
        return len(self._adjacency_list)

if __name__ == "__main__":
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
    print(g.get_nodes())

    print(g.get_neighbors('a'))
    print(g.size())


