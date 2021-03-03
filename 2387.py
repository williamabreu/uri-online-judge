class Appointment:

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.duration = end - begin
    

if __name__ == '__main__':

    N = int(input())
    appointments = []

    for i in range(N):
        X, Y = map(int, input().split())
        appointments.append(Appointment(X, Y))    
    
    appointments.sort(key=lambda x: (x.begin, x.duration))

    current = appointments[0]
    no_overlap_count = 1

    for i in range(1, N):
        next = appointments[i]
        if current.end <= next.begin:
            no_overlap_count += 1
            current = next
        elif current.duration > next.duration and current.begin != next.begin:
            current = next

    print(no_overlap_count)
