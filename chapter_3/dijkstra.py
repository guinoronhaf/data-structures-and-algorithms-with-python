DISTANCE = 0
PREVIOUS_NODE = 1

graph = dict()
graph['A'] = {'B': 5, 'D': 9, 'E': 2}
graph['B'] = {'A': 5, 'C': 2}
graph['D'] = {'A': 9, 'C': 3, 'F': 2}
graph['E'] = {'A': 2, 'F': 3}
graph['C'] = {'B': 2, 'C': 3}
graph['F'] = {'E': 3, 'D': 2}

distances = {
        'A': [0, None],
        'B': [float("inf"), None],
        'C': [float("inf"), None],
        'D': [float("inf"), None],
        'E': [float("inf"), None],
        'F': [float("inf"), None],
}

def get_shortest_distance(table, vertex): # retorna a menor distância entre a origem e o nó 'vertex'
    global DISTANCE
    return table[vertex][DISTANCE]

def set_shortest_distance(table, vertex, new_distance) # define a menor distância entre a origem e o nó 'vertex'
    global DISTANCE
    table[vertex][DISTANCE] = new_distance

def set_previous_node(table, vertex, previous_node): # define o nó anterior no menor caminho entre a origem e o nó 'vertex'
    global PREVIOUS_NODE 
    table[vertex][PREVIOUS_NODE] = previous_node

def get_distance(graph, first_vertex, second_vertex): # retorna a distância entre um 'vertex' e outro no grafo
    return graph[first_vertex][second_vertex]

def get_next_node(table, visited_nodes): # retorna o próximo nó/vértice a ser analisado
    global DISTANCE
    unvisited_nodes = list(set(table.keys()).difference(set(visited_nodes))) # vértices ainda por visitar
    assumed_min = table[unvisited_nodes[0]][DISTANCE] 
    min_vertex = unvisited_nodes[0] # assume-se que o primeiro de 'unvisited_nodes' é o de menor DISTANCE
    for node in table.keys(): # verifica-se se existe algum vértice cuja distância da origin é menor
        if table[node][DISTANCE] < assumed_min:
            assumed_min = table[node][DISTANCE]
            min_vertex = node
    return min_vertex # retorna o vértice cuja distância à origem é a menor

def get_shortest_path(graph, table, origin):

    visited_nodes = list()
    current_node = origin
    starting_node = origin
