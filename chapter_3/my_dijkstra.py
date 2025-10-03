DISTANCE = 0
PREVIOUS_NODE = 1
INFINITY = float("inf")

graph = dict()
graph['A'] = {'B': 5, 'D': 9, 'E': 2}
graph['B'] = {'A': 5, 'C': 2}
graph['D'] = {'A': 9, 'C': 3, 'F': 2}
graph['E'] = {'A': 2, 'F': 3}
graph['C'] = {'B': 2, 'C': 3}
graph['F'] = {'E': 3, 'D': 2}

table = {
        'A': [0, None],
        'B': [float("inf"), None],
        'C': [float("inf"), None],
        'D': [float("inf"), None],
        'E': [float("inf"), None],
        'F': [float("inf"), None],
}

def get_shortest_distance(table, vertex):
    global DISTANCE
    return table[vertex][DISTANCE]

def set_shortest_distance(table, vertex, new_distance):
    global DISTANCE
    table[vertex][DISTANCE] = new_distance

def set_previous_node(table, vertex, previous_node):
    global PREVIOUS_NODE
    table[vertex][PREVIOUS_NODE] = previous_node

def get_distance(graph, first_vertex, second_vertex):
    return graph[first_vertex][second_vertex]

def get_next_node(table, visited_nodes):
    global DISTANCE
    unvisited_nodes = list(set(table.keys()).difference(set(visited_nodes)))
    assumed_min = table[unvisited_nodes[0]][DISTANCE]
    min_node = unvisited_nodes[0]
    for node in unvisited_nodes:
        if table[node][DISTANCE] < assumed_min:
            assumed_min = table[node][DISTANCE]
            min_node = node
    return min_node

def get_shortest_path(graph, table, origin):

    visited_nodes = list()
    starting_node = origin
    current_node = origin

    while True:
        adjacent_nodes = graph[current_node]
        if set(adjacent_nodes).issubset(set(visited_nodes)):
            pass
        else:
            unvisited_nodes = set(adjacent_nodes).difference(set(visited_nodes))
            for vertex in unvisited_nodes:
                if get_shortest_distance(table, vertex) == INFINITY and starting_node == current_node:
                    total_distance = get_distance(graph, current_node, vertex)
                else:
                    total_distance = get_shortest_distance(table, current_node) + get_distance(graph, current_node, vertex)
                if total_distance < get_shortest_distance(table, vertex):
                    set_shortest_distance(table, vertex, total_distance)
                    set_previous_node(table, vertex, current_node)
        visited_nodes.append(current_node)
        if len(visited_nodes) == len(graph.keys()):
                break
        current_node = get_next_node(table, visited_nodes)

    print(table)


get_shortest_path(graph, table, "A")
