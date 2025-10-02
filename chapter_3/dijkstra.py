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

def get_shortest_distance(table, vertex): # retorna a menor distância entre a origem e o nó 'vertex'
    global DISTANCE
    return table[vertex][DISTANCE]

def set_shortest_distance(table, vertex, new_distance): # define a menor distância entre a origem e o nó 'vertex'
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
    for node in unvisited_nodes: # verifica-se se existe algum vértice, entre os não visitados, cuja distância da origin é menor
        if table[node][DISTANCE] < assumed_min:
            assumed_min = table[node][DISTANCE]
            min_vertex = node
    return min_vertex # retorna o vértice cuja distância à origem é a menor

def get_shortest_path(graph, table, origin):

    visited_nodes = list() # controle dos nós visitados
    current_node = origin # nó atual
    starting_node = origin # nó de origem

    while True:
        adjacent_nodes = graph[current_node] # nós vizinhos (adjacentes) do nó atual
        if (set(adjacent_nodes).issubset(set(visited_nodes))): # verificando se todos os nós adjacentes foram visitados
            pass
        else:
            unvisited_nodes = set(adjacent_nodes).difference(set(visited_nodes)) # set de nós vizinhos a visitar
            for vertex in unvisited_nodes:
                distance_from_starting_node = get_shortest_distance(table, vertex) # obtém a menor distância em 'table'
                if distance_from_starting_node == INFINITY and current_node == starting_node: # se a distância for ifinita (não setada) e current_node == starting_node,
                    # significa que a distância a ser setada é simplesmente a distância em relação ao nó de origem
                    total_distance = get_distance(graph, vertex, current_node)
                else:
                    total_distance = get_shortest_distance(table, current_node) + get_distance(graph, current_node, vertex)
                    # soma a distância do nó anterior ao de origem com a distância do nó anterior ao atual
                if total_distance < distance_from_starting_node: # atualiza a menor distância e o nó anterior se necessário
                    set_shortest_distance(table, vertex, total_distance)
                    set_previous_node(table, vertex, current_node)
        visited_nodes.append(current_node) # marca o nó como visitado
        if len(visited_nodes) == len(table.keys()): # verificação de saída o laço
            break
        current_node = get_next_node(table, visited_nodes) # atualiza o nó atual

    print(table)


get_shortest_path(graph, table, 'A')
