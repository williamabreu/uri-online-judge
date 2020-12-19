import json
from sys import stdin


class DiGraph:
    def __init__(self):
        # Using dict (hash table) to save memory
        self.__adj_list = {}
        self.__transpose_adj_list = {}
    

    def sucessors(self, vertex):
        if vertex in self.__adj_list:
            return self.__adj_list[vertex]
        else:
            return []
    

    def predecessors(self, vertex):
        if vertex in self.__transpose_adj_list:
            return self.__transpose_adj_list[vertex]
        else:
            return []
    

    def add_edge(self, edge):
        vertex1, vertex2 = edge
        # Add into graph
        if vertex1 in self.__adj_list:
            self.__adj_list[vertex1].append(vertex2)
        else:
            self.__adj_list[vertex1] = [vertex2]
        # Add into transpose graph
        if vertex2 in self.__transpose_adj_list:
            self.__transpose_adj_list[vertex2].append(vertex1)
        else:
            self.__transpose_adj_list[vertex2] = [vertex1]
        

    def exchange_vertexes(self, vertex1, vertex2):
        # For removing side effects...
        copy = dict(self.__adj_list)
        
        # 1. adj_list
        self.__exchange(copy, self.sucessors, self.predecessors, vertex1, vertex2)
        
        # 2. transpose_adj_list
        self.__exchange(self.__transpose_adj_list, self.predecessors, self.sucessors, vertex1, vertex2)

        self.__adj_list = copy
        

    def __exchange(self, adj_list, sucessor_func, predecessor_func, vertex1, vertex2):
        temp = sucessor_func(vertex1)
        
        adj_list[vertex1] = sucessor_func(vertex2)
        self.__exchange_vertex_in_adj_list(adj_list, vertex1, vertex1, vertex2)
        
        adj_list[vertex2] = temp
        self.__exchange_vertex_in_adj_list(adj_list, vertex2, vertex2, vertex1)

        for predecessor in predecessor_func(vertex1):
            self.__exchange_vertex_in_adj_list(adj_list, predecessor, vertex1, vertex2)
        
        for predecessor in predecessor_func(vertex2):
            self.__exchange_vertex_in_adj_list(adj_list, predecessor, vertex2, vertex1)
    

    def __exchange_vertex_in_adj_list(self, adj_list, predecessor, old_vertex, new_vertex):
        if predecessor in adj_list and old_vertex in adj_list[predecessor]:
            adj_list[predecessor].remove(old_vertex)
            adj_list[predecessor].append(new_vertex)


def get_min_reachable(graph, initial_vertex, values, num_vertexes):
    # DFS - Tested (OK)
    stack = list(graph.predecessors(initial_vertex))
    
    if stack == []:
        return '*'
    
    visited = [None] + [0] * num_vertexes
    min_value = values[stack[-1]]
    
    while stack != []:
        vertex = stack.pop()
        
        if values[vertex] < min_value:
            min_value = values[vertex]
        
        visited[vertex] = 1
        stack.extend([v for v in graph.predecessors(vertex) if not visited[v]])

    return min_value    


def main(N, M, I):
    graph = DiGraph()
    K = (None,) + tuple(map(int, input().split())) # vertexes ages

    for m in range(M):
        X, Y = map(int, input().split()) 
        # edge X -> Y
        graph.add_edge((X, Y))

    for i in range(I):
        buffer_read = input().split()
        if buffer_read[0] == 'T':
            code, vertex1, vertex2 = buffer_read
            graph.exchange_vertexes(int(vertex1), int(vertex2))
        else: # == 'P'
            code, vertex1 = buffer_read
            print(get_min_reachable(graph, int(vertex1), K, N))


if __name__ == '__main__':
    for buffer_read in stdin:
        N, M, I = map(int, buffer_read.split()) # N vertexes, M edges
        main(N, M, I)