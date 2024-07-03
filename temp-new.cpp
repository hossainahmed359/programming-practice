#include <bits/stdc++.h>

using namespace std;

vector<int> merge_sort (vector<int> arr) {
    int n = arr.size();

    // RECURSION END
    if(n <= 1)
        return arr;


    // DIVIDE
    int mid = n / 2;
    vector<int> left_half, right_half;

    for (int i = 0; i < mid; i++)
        left_half.push_back(arr[i]);
    for(int j = mid; j < n ; j++)
        right_half.push_back(arr[j]);


    // CONQUER
    vector<int> sorted_arr;
    int idx1 = 0, idx2 = 0;

    vector<int> left_sorted = merge_sort(left_half);
    vector<int> right_sorted = merge_sort(right_half);

    for(int i = 0; i < n; i++){
        if(left_sorted[idx1]== left_sorted.size()) {
            sorted_arr.push_back(right_sorted[idx2]);
            idx2++;
        }
        else if (right_sorted[idx2] == right_sorted.size()) {
            sorted_arr.push_back(left_sorted[idx1]);
            idx1++;
        }
        else if (left_sorted[idx1] < right_sorted[idx2]) {
            sorted_arr.push_back(left_sorted[idx1]);
            idx1++;
        }
        else {
            sorted_arr.push_back(right_sorted[idx2]);
            idx2++;
        }
    }



    // DESIRED OUTPUT RETURN
    return sorted_arr;
}


int main () {

    vector<int> unsorted_arr = {12, 11, 13, 5, 6, 7};
    int len = unsorted_arr.size();

    vector<int> new_sorted_arr = merge_sort(unsorted_arr);

    for(int i = 0; i < len; i++) {
        cout << new_sorted_arr[i] << " ";
    }


    return 0;
}
