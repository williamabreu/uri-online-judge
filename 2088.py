from itertools import combinations
from heapq import heappush
from sys import stdin


def distance2d(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5


def encode(S):
    code = 0
    for i in S:
        code |= 1 << i
    return code


def held_karp(d):
    # https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm

    # C: cost
    # S: subset
    # d: distance

    # In pseudo-code (wikipedia) index starts at 1, 
    # but the code below starts at 0.
    
    n = len(d)
    C = {}

    for k in range(1, n):
        code = encode([k])
        C[code] = {}
        C[code][k] = d[0][k]

    for s in range(2, n):
        for S in combinations(range(1, n), s): # TODO: optimize this!
            code = encode(S)
            for k in S:
                prev_code = code & ~encode([k])
                minheap = []
                for m in S:
                    if m != k:
                        heappush(minheap, C[prev_code][m] + d[m][k])
                if code not in C:
                    C[code] = {}
                C[code][k] = minheap[0]

    code = encode(range(1, n))
    minheap = []

    for k in range(1, n):
        heappush(minheap, C[code][k] + d[k][0])
    
    return minheap[0]


def main(coords):
    n = len(coords)
    distances_matrix = []

    # Initialize all peer-to-peer distances
    # It's like an Ajacency Matrix of an undirected graph
    for i in range(n):
        distances_matrix.append([0] * n)
        for j in range(i):
            d = distance2d(coords[i], coords[j])
            distances_matrix[i][j] = d
            distances_matrix[j][i] = d
    
    return held_karp(distances_matrix)


if __name__ == '__main__':
    for N in stdin:
        N = int(N)

        if N != 0: 
            coords = []
            for i in range(N + 1):
                x, y = map(int, input().split()) # # Joao is in coords[0]
                coords.append((x, y))
            
            print('{:.2f}'.format( main(coords) ))
        else:
            exit(0)
