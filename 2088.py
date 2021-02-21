# https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm

from sys import stdin


def distance2d(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5


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
