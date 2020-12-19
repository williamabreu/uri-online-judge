# Baseline from https://thealgorithms.github.io/


def kruskal(num_nodes: int, edges: 'list[tuple(int, int, int)]') -> int:
    edges = sorted(edges, key=lambda edge: edge[2])

    parent = list(range(num_nodes))

    def find_parent(i):
        if i != parent[i]:
            parent[i] = find_parent(parent[i])
        return parent[i]

    minimum_spanning_tree_cost = 0

    for edge in edges:
        parent_a = find_parent(edge[0])
        parent_b = find_parent(edge[1])
        if parent_a != parent_b:
            minimum_spanning_tree_cost += edge[2]
            parent[parent_a] = parent_b

    return minimum_spanning_tree_cost



if __name__ == "__main__":
    
    N, M = map(int, input().split()) # Number of vertex (corener) / edges (street)

    while not (N == M == 0):
        
        edges = []
        edges_negative = []

        for i in range(M):
            X, Y, C = map(int, input().split()) # Edge (X, Y) with weight C
            edges.append((X-1, Y-1, C))
            edges_negative.append((X-1, Y-1, -C))
        
        minimum =   kruskal(N, edges)
        maximum = - kruskal(N, edges_negative)

        print(maximum - minimum)

        # URI bugged - trying to resolve the bug:
        # ---------------------------------------
        # Traceback (most recent call last):
        # File "Main.py", line 46, in 
        #     N, M = map(int, input().split()) # Next
        # ValueError: not enough values to unpack (expected 2, got 0)
        # ---------------------------------------
        line_read = list(map(int, input().split())) # Next
        while line_read == []:
            line_read = list(map(int, input().split())) # Next
        N, M = line_read
