def sublists(main_list):
    # Given a list, returns all sequencial sublists (including unitary).
    # E.g. [0, 2, 3, 4, 7, 11, 12] -> [[0], [2, 3, 4], [7], [11, 12]]

    sub_lists = []
    i = 0

    while i < len(main_list):

        j = i + 1

        while j < len(main_list) and main_list[j] == main_list[j-1] + 1:
            j += 1

        sub_lists.append(main_list[i:j])
        i = j

    return sub_lists


def count_matches(adj_list, number):
    # Check neighbourhood "palitos".
    
    counter = 0

    for node_index in adj_list:

        neighbours = adj_list[node_index]

        for ordered_sublist in sublists(neighbours):
            if len(ordered_sublist) >= number:
                counter += 1
    
    return counter


if __name__ == '__main__':
    
    # FIRST
    P, N, C = map(int, input().split()) # READ

    while not (P == N == C == 0):

        # Printed at the end.
        counter = 0

        # Bipartite graph, with the P nodes indexed and 
        # the N nodes into adjacent list.
        p_adj_list = {p_index: [] for p_index in range(P)}
        
        # Bipartite graph, with the P nodes indexed and 
        # the N nodes into adjacent list.
        # n_adj_list = {n_index: [] for n_index in range(N)}

        # Building the adjancent lists...
        for n_index in range(N):
            
            row = map(int, input().split()) # READ
            
            # zip format: [(value, p_index), ...]
            p_index_zip = zip(row, [p_index for p_index in range(P)])
            
            filtered = filter(lambda x: x[0] == 1, p_index_zip)
            
            for value, p_index in filtered:
                # Add the n node to p node adjacents.
                p_adj_list[p_index].append(n_index)
                # And vice-versa...
                # n_adj_list[n_index].append(p_index)

        # building done!
        
        # Count in vertical way.
        counter = count_matches(p_adj_list, C) # + count_matches(n_adj_list, C)

        print(counter) # OUTPUT
            
        # NEXT
        P, N, C = map(int, input().split()) # READ
