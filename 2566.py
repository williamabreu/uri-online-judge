from sys import stdin
from heapq import heappop, heappush


class Constants:    
    BUS = 0
    AIRPLANE = 1


class DiGraph:
    def __init__(self):
        # Using dict (hash table) to save memory
        # Format: 'vertex1' -> 'vertex2' with cost 'weight' 
        #         { vertex1: [ (vertex2, weight), ... ] }
        self.__adj_list = {}
    
    def neighbourhood(self, vertex):
        if vertex in self.__adj_list:
            return self.__adj_list[vertex]
        else:
            return []

    def add_edge(self, edge, weight):
        vertex1, vertex2 = edge
        if vertex1 in self.__adj_list:
            self.__adj_list[vertex1].append((vertex2, weight))
        else:
            self.__adj_list[vertex1] = [(vertex2, weight)]


def dijkstra(graph, num_vertexes, start, end):
    minheap = [(0, start)] # Format: [(weight: int, vertex: int), ...]
    visited = [None] + [False] * num_vertexes

    while minheap != []:
        weight, vertex = heappop(minheap)

        if not visited[vertex]:
            visited[vertex] = True

            if vertex == end:
                return weight

            for neigh_vertex, neigh_weight in graph.neighbourhood(vertex):
                if not visited[neigh_vertex]:
                    heappush(minheap, (weight + neigh_weight, neigh_vertex))
    
    return float('inf')


def main():
    # N cities (i=1 source, i=N destination)
    # M paths
    for line in stdin:
        N, M = map(int, line.split())

        mapping = {
            Constants.BUS: DiGraph(),
            Constants.AIRPLANE: DiGraph(),
        }

        for i in range(M):
            # Move from A -> B with cost R 
            A, B, T, R = map(int, input().split())
            mapping[T].add_edge((A, B), R)
        
        mincost = min([dijkstra(graph, N, 1, N) for graph in mapping.values()])

        print(mincost)


if __name__ == '__main__':
    main()