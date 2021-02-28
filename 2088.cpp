#include <iostream>
#include <iomanip>
#include <utility>
#include <cmath>
#include <map>
#include <list>
#include <vector>
#include <algorithm>

using namespace std;


#define MAX_SIZE 16


double distance2d(pair<int, int> &p0, pair<int, int> &p1) {
    
    int x0 = p0.first;
    int y0 = p0.second;
    int x1 = p1.first;
    int y1 = p1.second;

    return sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2));

}


unsigned int encode(list<int> S) {
    
    unsigned int code = 0;

    for (list<int>::iterator it = S.begin(); it != S.end(); it++) {
        code |= 1 << *it;
    }

    return code;

}


void combination_recursive(int* arr, int n, int r, int index, int* data, int i, list<list<int>> &result) { 
	
    // Current combination is ready
	if (index == r) { 
        list<int> current_result;
		for (int j = 0; j < r; j++) {
			current_result.push_back(data[j]); 
        }
        result.push_back(current_result);
		return; 
	} 

	// When no more elements are there to put in data[]
	if (i >= n) {
		return; 
    }

	// current is included, put next at next location 
	data[index] = arr[i]; 
	combination_recursive(arr, n, r, index + 1, data, i + 1, result); 

	// current is excluded, replace it with next (Note that 
	// i+1 is passed, but index is not changed) 
	combination_recursive(arr, n, r, index, data, i+1, result); 

} 


list<list<int>> combinations(list<int> set, int size) {
    
    int set_length = set.size();
    int data[size];
    int arr[set_length];
    int i = 0;
    
    for (list<int>::iterator it = set.begin(); it != set.end(); it++, i++) {
        arr[i] = *it;
    }

    list<list<int>> result;
    
    combination_recursive(arr, set_length, size, 0, data, 0, result); 

    return result;

}


list<int> range(int start, int end) {

    list<int> result;
    for (int i = start; i < end; i++) {
        result.push_back(i);
    }
    return result;

}


double get_min(list<double> set) {

    list<double>::iterator min = set.begin();

    for (list<double>::iterator it = set.begin(); it != set.end(); it++) {
        if (*it < *min) {
            min = it;
        }
    }

    return *min;

}


double held_karp(double d[MAX_SIZE][MAX_SIZE], int n) {

    //  https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm

    //  C: cost
    //  S: subset
    //  d: distance

    //  In pseudo-code (wikipedia) index starts at 1, 
    //  but the code below starts at 0.

    map<pair<unsigned int, int>, double> C;

    for (int k = 1; k < n; k++) {
        list<int> S;
        S.push_back(k);
        C[make_pair(encode(S), k)] = d[0][k];
    }

    for (int s = 2; s < n; s++) {
        
        list<list<int>> combinations_set = combinations(range(1, n), s);
        
        for (list<list<int>>::iterator S = combinations_set.begin(); S != combinations_set.end(); S++) {
        
            for (list<int>::iterator k = S->begin(); k != S->end(); k++) {
        
                list<int> S_minus_k(*S);
                S_minus_k.remove(*k);

                list<double> all_possibilities;

                for (list<int>::iterator m = S->begin(); m != S->end(); m++) {
                    if (*m != *k) {
                        all_possibilities.push_back( C[make_pair(encode(S_minus_k), *m)] + d[*m][*k] );
                    }
                }

                C[make_pair(encode(*S), *k)] = get_min(all_possibilities);

            }

        }

    }

    list<double> all_possibilities;

    for (int k = 1; k < n; k++) {
        all_possibilities.push_back( C[make_pair(encode(range(1, n)), k)] + d[k][0] );
    }

    return get_min(all_possibilities);

}


double main_call(pair<int, int>* coords, int size) {

    double distances_matrix[MAX_SIZE][MAX_SIZE] = {0};

    // Initialize all peer-to-peer distances
    // It's like an Ajacency Matrix of an undirected graph
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < i; j++) {
            double d = distance2d(coords[i], coords[j]);
            distances_matrix[i][j] = d;
            distances_matrix[j][i] = d;
        }
        
    }

    return held_karp(distances_matrix, size);

}


int main() {

    int N, x, y;
    pair<int, int> coords[MAX_SIZE];

    cin >> N;
    
    while (N != 0) {
        
        for (int i = 0; i < N + 1; i++) {
            cin >> x >> y;
            coords[i] = make_pair(x, y); // Joao is in coords[0]
        }

        cout << fixed << setprecision(2) << main_call(coords, N) << endl;
        
        cin >> N;

    }

    return 0;

}