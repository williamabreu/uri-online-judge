from sys import stdin


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
            buffer = input().split()
            # Move from A -> B with cost R 
            A, B, T = map(int, buffer[:3])
            R = float(buffer[3])
            mapping[T].add_edge((A, B), R)
        
        # ;;;;;;;
        # import json
        # class Encode(json.JSONEncoder):
        #     def default(self, o):
        #         return o.__dict__
        # print(json.dumps(mapping, cls=Encode, indent=2))
        # ;;;;;;;


if __name__ == '__main__':
    main()