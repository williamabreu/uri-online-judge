import heapq 


# Constants.
TIMEBOX = 0
CASHIER = 1

# global.
global_time = 0


def allocate_client_to_cashier(time_spend, cashier_index, cashiers):
    heapq.heappush(cashiers, [time_spend, cashier_index])


def get_next_cashier_avaliable(cashiers):
    global global_time

    time, cashier_index = heapq.heappop(cashiers)
    global_time += time
    
    for i in range(len(cashiers)):
        cashiers[i][TIMEBOX] -= time

    return cashier_index


def initialize_cashiers(cashiers, clients_queue, employees_list):
    for i in range(len(employees_list)):
        time = clients_queue.pop(0) * employees_list[i]
        heapq.heappush(cashiers, [time, i])


if __name__ == '__main__':

    N, M = map(int, input().split()) # Number of employees / clients
    V = list(map(int, input().split())) # Seconds spent to process a single client item by an employee
    C = list(map(int, input().split())) # queue - Amount of itens from a client

    cashiers = [] # min heap

    initialize_cashiers(cashiers, C, V)

    while C != []:
        index = get_next_cashier_avaliable(cashiers)
        time = C.pop(0) * V[index] # Seconds spent to process all the itens
        allocate_client_to_cashier(time, index, cashiers) # Client goes to the lowest cashier number 
    
    while cashiers != []:
        get_next_cashier_avaliable(cashiers)
    
    print(global_time)
    