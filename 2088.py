from itertools import combinations
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
        C[(encode([k]), k)] = d[0][k]

    for s in range(2, n):
        for S in combinations(range(1, n), s):
            code = encode(S)
            for k in S:
                prev_code = code & ~encode([k])
                C[(code, k)] = min([ (C[(prev_code, m)] + d[m][k]) for m in S if m != k ])

    code = encode(range(1, n))
    
    return min([ (C[(code, k)] + d[k][0]) for k in range(1, n) ])


def main(coords):
    distances_matrix = [[0] * len(coords) for i in range(len(coords))]

    # Initialize all peer-to-peer distances
    # It's like an Ajacency Matrix of an undirected graph
    for i in range(len(coords)):
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
            x, y = map(int, input().split()) # Joao's home
            coords.append((x, y)) # Joao is in coords[0]

            for i in range(N):
                x, y = map(int, input().split()) # Others' houses
                coords.append((x, y))
            
            print(f'{main(coords):.2f}')
        else:
            exit(0)
