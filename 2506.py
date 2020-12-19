from sys import stdin

# clock indexes
HOUR = 0
MINUTE = 1

# pacient indexes
ARRIVAL_TIME = 0
CRITICAL_TIME = 1


def attend_pacient(clock_now, arrival_time, critical_time):
    # return 1 if the critical time got exceeded, 0 otherwise.
    elapsed_time = (clock_now[HOUR] -  arrival_time[HOUR]) * 60 + clock_now[MINUTE] - arrival_time[MINUTE]
    if elapsed_time < 0:
        syncronize_clock(clock_now, arrival_time)
        return attend_pacient(clock_now, arrival_time, critical_time)
    else:
        return 1 if elapsed_time > critical_time else 0


def increase_30min(clock_now):
    # self explanatory.
    if clock_now[MINUTE] == 0:
        clock_now[MINUTE] += 30
    else:
        clock_now[MINUTE] = 0
        clock_now[HOUR] += 1


def syncronize_clock(clock_now, arrival_time):
    # Set the time when the first pacient will be attended.
    clock_now[HOUR] = arrival_time[HOUR]
    if arrival_time[MINUTE] == 0:
        clock_now[MINUTE] = 0
    elif arrival_time[MINUTE] <= 30:
        clock_now[MINUTE] = 30
    else:
        clock_now[MINUTE] = 0
        clock_now[HOUR] += 1


if __name__ == '__main__':

    for N in stdin:
        N = int(N) # Number of pacients
        queue = []

        # Fill the queue
        for i in range(N):
            H, M, C = map(int, input().split()) # Hour, Minutes and Critical time (Priority)
            pacient = ((H, M), C)
            queue.append(pacient)
        
        critical_exceeded = 0 # Final output
        clock = [7, 0] # Start at 7:00 AM
        
        while queue != []:
            pacient = queue.pop(0)
            critical_exceeded += attend_pacient(clock, pacient[ARRIVAL_TIME], pacient[CRITICAL_TIME])
            increase_30min(clock)
        
        print(critical_exceeded)       
