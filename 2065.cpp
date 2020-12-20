#include <iostream>
#include <utility>
// #include <sstream>
using namespace std;


class MinHeap {

	private:

		pair<int, int>* heap;
		int capacity;
		int size;

		inline int parent(int i) { 
			return (i - 1) / 2; 
		}

		inline int left(int i) { 
			return (i * 2) + 1; 
		}

		inline int right(int i) { 
			return (i * 2) + 2; 
		}

		void sift_down(int i) {
			int index_lowest = i;
			if (left(i) < size and (heap[i].first > heap[left(i)].first or (heap[i].first == heap[left(i)].first and heap[i].second > heap[left(i)].second))) {
				index_lowest = left(i);
			}
			if (right(i) < size and (heap[index_lowest].first > heap[right(i)].first or (heap[index_lowest].first == heap[right(i)].first and heap[index_lowest].second > heap[right(i)].second))) {
				index_lowest = right(i);
			}
			if (index_lowest != i) {
				pair<int, int> tmp = heap[i];
				heap[i] = heap[index_lowest];
				heap[index_lowest] = tmp;
				sift_down(index_lowest);
			}
		}

		void sift_up(int i) {
			pair<int, int> aux;
			bool ok = false;
			
			while (not ok) {
				if (heap[i].first < heap[parent(i)].first or (heap[i].first == heap[parent(i)].first and heap[i].second < heap[parent(i)].second)) {
					aux = heap[i];
					heap[i] = heap[parent(i)];
					heap[parent(i)] = aux;
					i = parent(i);
				}
				else {
					ok = true;
				}
			}
		}

	public:

		MinHeap(int max_capacity) {
			capacity = max_capacity;
			size = 0;
			heap = new pair<int, int>[capacity];
		}

		~MinHeap() {
			delete[] heap;
		}

		// string str() {
		// 	stringstream output;
		// 	output << "[";
		// 	if (size != 0) {
		// 		output << "(" << heap[0].first << ", " << heap[0].second << ")";
		// 		for (int i = 1; i < size; i++) {
		// 			output << ", (" << heap[i].first << ", " << heap[i].second << ")";
		// 		}
		// 	}
		// 	output << "]";
		// 	return output.str();
		// }

		bool push(pair<int, int> d) {
			if (size < capacity) {
				heap[size++] = d;
				sift_up(size-1);
				return true;
			}
			else {
				return false; // full
			}
		}

		pair<int, int>* pop() {
			if (size > 1) {
				pair<int, int>* output = new pair<int, int>;
				*output = heap[0];
				heap[0] = heap[--size];
				sift_down(0);
				return output;
			}
			else if (size == 1) {
				pair<int, int>* output = new pair<int, int>;
				*output = heap[0];
				size = 0;
				return output;
			}
			else {
				return NULL; // empty
			}
		}

		// int is_full() {
		// 	return size == capacity;
		// }
		
		int is_empty() {
			return size == 0;
		}

		// int length() {
		// 	return size;
		// }

		void update(int decrease_value) {
			for (int i = 0; i < size; i++) {
				heap[i].first -= decrease_value;
			}
		}

};


void allocate_client_to_cashier(int time_spend, int cashier_index, MinHeap &cashiers) {
	cashiers.push(make_pair(time_spend, cashier_index));
}

int get_next_cashier_avaliable(MinHeap &cashiers, int &global_time) {
	pair<int, int>* popped = cashiers.pop();
    global_time += popped->first;
    cashiers.update(popped->first);
    return popped->second;
}

void initialize_cashiers(MinHeap &cashiers, int* clients_queue, int* employees_list, int employees_list_length, int &next_client) {
    for (int i = 0; i < employees_list_length; i++) {
        int time = clients_queue[next_client++] * employees_list[i];
        cashiers.push(make_pair(time, i));
	}
}


int main() {

	// Global control
	int global_time = 0, next_client = 0;
	
	// Input...

	int N, M; // Number of: employees (N), clients (M)
	cin >> N >> M;

	int V[N], C[M]; 

	for (int i = 0; i < N; i++) {
		cin >> V[i];
	}

	for (int j = 0; j < M; j++) {
		cin >> C[j];
	}

	// All data read!

	MinHeap cashiers(N);

	initialize_cashiers(cashiers, C, V, N, next_client);

	while (next_client < M) {
		int index = get_next_cashier_avaliable(cashiers, global_time);
		int time = C[next_client++] * V[index]; // Seconds spent to process all the itens
		allocate_client_to_cashier(time, index, cashiers); // Client goes to the lowest cashier number 
	}
	
	while (not cashiers.is_empty()) {
		get_next_cashier_avaliable(cashiers, global_time);
	}

	cout << global_time << endl;

}
