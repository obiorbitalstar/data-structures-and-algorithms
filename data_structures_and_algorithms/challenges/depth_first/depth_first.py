def graph_dfs(graph, source, path=[]):

    if source not in path:

        path.append(source)

        if source not in graph:
            return path

        for neighbor in graph[source]:

            path = graph_dfs(graph, neighbor, path)

    return path


if __name__ == "__main__":
    # graph = {"A": ["B", "C", "D"],
    #          "B": ["E"],
    #          "C": ["F", "G"],
    #          "D": ["H"],
    #          "E": ["I"],
    #          "F": ["J"]}

    # path = graph_dfs(graph, "A")

    # print(" ".join(path))
    pass
