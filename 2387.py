class Appointment:

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.duration = end - begin
    
    def __lt__(self, o):
        return self.begin < o.begin


if __name__ == '__main__':

    N = int(input())

    X, Y = map(int, input().split())
    current = Appointment(X, Y)
    no_overlap_count = 1

    for i in range(N-1):
        X, Y = map(int, input().split())
        next = Appointment(X, Y)
        if current.end <= next.begin:
            no_overlap_count += 1
            current = next
        elif current.duration > next.duration:
            current = next

    print(no_overlap_count)
