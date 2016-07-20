import re

def compute_scc(array):
    """
    It computes sizes of strong connected components of the graph
    Using [Kosaraju's algorithm](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm)

    Input array has the following format
    [
        '1 2',
        '3 5',
        '4 7',
        ...
    ]
    where each line represents one directed edge
    e.g. '1 2' means directed edge is going from 1 to 2
    """
    max = 0
    max_len = 0
    graph = {}
    for edge in array:
        first_vertex, second_vertex = re.split('\t|\s', edge)
        max_vertex = int(first_vertex if int(first_vertex) > int(second_vertex) else second_vertex)
        if max_vertex > max:
            max = max_vertex
    
        if first_vertex not in graph:
            graph[first_vertex] = []

        if second_vertex not in graph:
            graph[second_vertex] = []

        graph[first_vertex].append(second_vertex)
        new_len = len(graph[first_vertex])
        if new_len > max_len:
            max_len = new_len

    discovered = {}
    s = { "value": 1 }
    remapping = {}

    def dfs(vertex):
        if vertex not in discovered:
            link_vertex = vertex
            stack = []
            while (link_vertex):
                discovered[link_vertex] = True
                edges = graph[link_vertex]
                
                found = False
                for second_vertex in edges:
                    if second_vertex not in discovered:
                        found = True
                        stack.append(link_vertex)
                        link_vertex = second_vertex
                        break

                if found == False:
                    remapping[link_vertex] = str(s["value"])
                    s["value"] = s["value"] + 1
                    if len(stack):
                        link_vertex = stack.pop()
                    else:
                        link_vertex = None

    for vertex in range(int(max), 0, -1):
        vertex = str(vertex)
        dfs(vertex)


    rev_graph = {}
    for edge in array:
        first_vertex, second_vertex = re.split('\t|\s', edge)
        mapped_first_vertex = remapping[second_vertex]
        mapped_second_vertex = remapping[first_vertex]

        if first_vertex not in rev_graph:
            rev_graph[first_vertex] = []

        if second_vertex not in rev_graph:
            rev_graph[second_vertex] = []
    
        if mapped_first_vertex not in rev_graph:
            rev_graph[mapped_first_vertex] = []

        if mapped_second_vertex not in rev_graph:
            rev_graph[mapped_second_vertex] = []

        rev_graph[mapped_first_vertex].append(mapped_second_vertex)

    rev_discovered = {}
    r = { "value": 0 }
    sizes = []
    def rev_dfs(vertex):
        if vertex not in rev_discovered:
            link_vertex = vertex
            stack = []
            while (link_vertex):
                rev_discovered[link_vertex] = True
                edges = rev_graph[link_vertex]
                
                found = False
                for second_vertex in edges:
                    if second_vertex not in rev_discovered:
                        found = True
                        stack.append(link_vertex)
                        link_vertex = second_vertex
                        break

                if found == False:
                    r["value"] = r["value"] + 1
                    if len(stack):
                        link_vertex = stack.pop()
                    else:
                        link_vertex = None

    for vertex in range(int(max), 0, -1):
        vertex = str(vertex)
        rev_dfs(vertex)
        if r["value"] > 0:
            sizes.append(r["value"])
            r["value"] = 0

    return sizes
