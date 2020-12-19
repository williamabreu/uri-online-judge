# Constants.
NUMBER = 0
NAME = 1


def get_position(number, position, length):
    # Brute force... (Modular arithmetic got wrong)

    if number % 2 == 0:
        # even - clockwise (-)
        j = (position - 1) % length
        for i in range(number - 1):
            j = (j - 1) % length
        return j

    else:
        # odd - anticlockwise (+)
        j = position % length
        for i in range(number - 1):
            j = (j + 1) % length
        return j


if __name__ == '__main__':

    N = int(input()) # FIRST

    while N != 0:

        # Circular list.
        circle = [] # format: [(card_number, child_name), ...]
        

        # Fill the circle.
        for _ in range(N):
            name, number = input().split() # READ
            circle.append((int(number), name)) 
        
        # Circle filled.

        # First move.
        number = circle[0][NUMBER]
        position = 0

        if number % 2 == 0:
            # even - clockwise (-)
            position = -number % len(circle) 

        else:
            # odd - anticlockwise (+)
            position = number % len(circle)

        if len(circle) > 1:
            number = circle.pop(position)[NUMBER]

        # Next move.
        while len(circle) > 1:
            position = get_position(number, position, len(circle))
            number = circle.pop(position)[NUMBER]

        # Announce the winner.
        print('Vencedor(a):', circle[0][NAME])

        N = int(input()) # NEXT
