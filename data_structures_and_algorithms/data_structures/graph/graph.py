class Node:
    def __init__(self, value):
        self.value = value


class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        if value in self._adjacency_list:
            print('Vertex', value, ' already exists')
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

    def breadth_first_search(self, s):
        visited = [False] * (len(self._adjacency_list))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self._adjacency_list[s][0]:
                print(i)
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    g = Graph()
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3,3)
    g.add_edge(2,2)
    g.add_edge(2,4)
    g.add_edge(4,2)
    # print(g.get_nodes())
    g.breadth_first_search(2)
    # print(g.get_neighbors('a'))
    # print(g.size())
