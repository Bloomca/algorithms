import re

def compute_paths(array, start_node, finish_node, not_found = 1000000):
    """
    Naive implementation of dijkstra algorithm, without heap
    So the running time here is n * m,
    where n is number of vertices,
    and m is number of edges

    Array has the following format:
    [
        '1 2,3 4,5, 7,5',
        '2 1,3 4,4 5,1',
        ...
    ]
    The first number in the string is the vertex number
    Following pairs (x,y): x -- number of vertex which has edge with
    the initial vertex and y is the length of this edge
    """
    
    # we put it to the same type to avoid problems in the future
    start_node = str(start_node)
    finish_node = str(finish_node)

    # we transform graph representation to the dict one
    # with vertices as keys and lists of edges as values
    graph = {}
    for line in array:
        splitted_string = re.split('\t|\s', line)
        vertex = splitted_string[0] 
        graph[vertex] = splitted_string[1:]

    # check input correctness, that nodes are inside graph
    if start_node not in graph:
        raise TypeError("no start node in the presented graph!")

    if finish_node not in graph:
        raise TypeError("no finish node in the presented graph!")

    vertices = set(graph.keys())
    vertices.remove(start_node)
    vertex = start_node
    discovered = {
        start_node: True
    }
    while len(vertices) > 0:
        edges = graph[vertex]
        current_length = None
        current_vertex = None
        for edge in edges:
            [second_vertex, length] = edge.split(",")
            length = int(length)
            if second_vertex not in discovered:
                if current_length is None or length < current_length:
                    current_length = length
                    current_vertex = second_vertex

        if current_vertex in vertices:
            discovered[current_vertex] = True

            if current_vertex == finish_node:
                return current_length
            vertices.remove(current_vertex)

            def update_edges(edge):
                [second_vertex, length] = edge.split(",")
                length = int(length)
                return "{0}, {1}".format(second_vertex, length + current_length)

            updated_values = [update_edges(edge) for edge in graph[current_vertex]]

            graph[vertex] = graph[vertex] + updated_values
            def filter_edges(edge):
                [second_vertex, length] = edge.split(",")
                return second_vertex not in discovered
            graph[vertex] = filter(filter_edges, graph[vertex])

        else:
            return not_found

    return not_found
