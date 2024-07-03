#include <bits/stdc++.h>

using namespace std;

vector<int> quick_sort(vector<int> arr) {

    int n = arr.size();

    // RECURSION END
    if (n <= 1) {
        return arr;
    }

    // DIVIDE
    int pivot = n / 2;
    vector<int> left_half, right_half;

    for(int i = 0; i < n; i++) {
        if (i == pivot) {
            continue;
        } else if (arr[i] < arr[pivot]) {
            left_half.push_back(arr[i]);
        } else {
            right_half.push_back(arr[i]);
        }
    }


    vector<int> left_sorted = quick_sort(left_half);
    vector<int> right_sorted = quick_sort(right_half);

    // CONQUER
    vector<int> sorted_arr;


    for (int i = 0; i < left_sorted.size(); i++) {
        sorted_arr.push_back(left_sorted[i]);
    }

    sorted_arr.push_back(arr[pivot]);

    for (int i = 0; i < right_sorted.size(); i++) {
        sorted_arr.push_back(right_sorted[i]);
    }


    // DESIRED OUTPUT

    return sorted_arr;
}

int main () {

    vector<int> my_array = {5, 3, 7, 1, 8, 9};

    vector<int> new_sorted_arr = quick_sort(my_array);

    for(int i = 0; i < new_sorted_arr.size(); i++)
        cout << new_sorted_arr[i] << " ";

    return 0;
}
