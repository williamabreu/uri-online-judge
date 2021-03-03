# - Directed graph
# - Number of roads (edges) = Number of cities (vertices)
# - Eulerian Graph problem

from copy import copy


class DiGraph:
    
    def __init__(self):
        # Using dict (hash table) to save memory
        self.__adj_list = {}
        self.__transpose_adj_list = {}
    
    def __get_degree(self, adj_list, vertex):
        if vertex in adj_list:
            return len(adj_list[vertex])
        else:
            return 0
    
    def __add_edge(self, adj_list, u, v):
        if u in adj_list:
            adj_list[u].append(v)
        else:
            adj_list[u] = [v]

    def degree_plus(self, vertex):
        # d+(v)
        return self.__get_degree(self.__adj_list, vertex)
    
    def degree_minus(self, vertex):
        # d-(v)
        return self.__get_degree(self.__transpose_adj_list, vertex)

    def add_edge(self, edge):
        u, v = edge
        # Add into graph
        self.__add_edge(self.__adj_list, u, v)
        # Add into transpose graph
        self.__add_edge(self.__transpose_adj_list, v, u)
    
    def neighborhood(self, vertex):
        if vertex in self.__adj_list:
            return copy(self.__adj_list[vertex])
        else:
            return []


def check_conex(graph, num_vertices, start):
    # DFS - Check if is a conex graph
    visited = {}
    stack = graph.neighborhood(start)
    
    while stack != []:
        vertex = stack.pop()
        visited[vertex] = 1
        stack.extend([v for v in graph.neighborhood(vertex) if not visited.get(v, 0)])
    
    return len(visited) == num_vertices


def check_eulerian(graph, vertices):
    # Euler Theorem - Check if is a pseudo symmetric graph
    if not check_conex(graph, len(vertices), 1):
        return False

    for v in vertices:
        if graph.degree_plus(v) != graph.degree_minus(v):
            return False
    
    return True


if __name__ == '__main__':
    
    N = int(input()) # Num. cities
    graph = DiGraph()
    vertices = set()

    for i in range(N):
        A, B = map(int, input().split())
        graph.add_edge((A, B)) # A -> B
        vertices.add(A)
        vertices.add(B)
    
    eulerian = 'S' if check_eulerian(graph, vertices) else 'N'

    print(eulerian)
