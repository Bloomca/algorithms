import random
import re

def getRandomCuts(array):
    """
    Get random cuts size of graph
    It just cuts graph down to two vertices, and after
    returns number of edges between

    It is a random algorithm, so the single run will fail
    trying to find min cut
    
    Array structure:
    [
        '1 5 10 4 6',
        '2 3 4 5 6',
        '3 1 2 7 9',
        ...
    ]
    Where the first number in row is a vertex, and next numbers
    are number of vertices which have edges between first vertex
    """
    graph = {}
    # parsing graph to represent it as a dict
    for string in array:
        values = filter(bool, re.split('\t|\s', string))
        vertices_len = len(values) 
        if (vertices_len):
            vertex = values[0]
            first = [vertex] * (vertices_len - 1)
            second = values[1::]
            graph[vertex] = zip(first, second)

    vertices = graph.keys()
    vertices_num = len(vertices)

    # we have to leave 2 vertices, therefore iterate through n-2 vertices
    for i in range(0, vertices_num - 2):
        # we choose random vertex only to choose random edge later
        # we could create list of all edges, but to avoid maitaining it,
        # we just choose random stuff twice
        random_vertex = random.choice(vertices)
        edges_from_vertex = graph[random_vertex]
        # choose random edge to contract
        random_edge = random.choice(edges_from_vertex)
        first_vertex, second_vertex = random_edge

        # copy all edges from the second vertex to the first one
        graph[first_vertex] = graph[first_vertex] + graph[second_vertex]

        # we remove always second just for convenience
        # we could remove the first one with the same result
        vertices.remove(second_vertex)
        del graph[second_vertex]

        # now we have to replace second vertex to the first one in all edges
        # so we iterate through all graph
        for vertex in graph:
            edges = graph[vertex]
            edges_num = len(edges)

            for index in range(0, edges_num):
                edge_check = edges[index]
                first_vertex_check, second_vertex_check = edge_check

                same_edge_1 = (first_vertex, second_vertex) == edge_check
                same_edge_2 = (second_vertex, first_vertex) == edge_check
                
                # it the edge is between two selected vertices, just delete it
                if same_edge_1 or same_edge_2:
                    edges[index] = None
                # otherwise replace the second vertex with the first one
                elif first_vertex_check == second_vertex:
                    edges[index] = (first_vertex, second_vertex_check)
                elif second_vertex_check == second_vertex:
                    edges[index] = (first_vertex_check, first_vertex)
            
            # we filter only to remove edges which are `None`
            graph[vertex] = filter(bool, edges)

    edges_list = graph.values()

    # it doesn't matter here which edges list to take -- 0 or 1
    # because we have only two vertices left, and all edges are between them
    return len(edges_list[0])

def findMinCuts(array):
    """
    Runs finding random cuts size n^2 times, which increases chances
    drastically

    Array structure:
    [
        '1 5 10 4 6',
        '2 3 4 5 6',
        '3 1 2 7 9',
        ...
    ]
    Where the first number in row is a vertex, and next numbers
    are number of vertices which have edges between first vertex
    """
    num = len(array)
    min = None

    for i in range(0, num ** 2):
        new_min = getRandomCuts(array)

        if min is None or new_min < min:
            min = new_min

    return min