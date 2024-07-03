#include <bits/stdc++.h>

using namespace std;


/* vector<int> merge_sort(vector<int> arr) {
    // Recursion End
    if(arr.size() <= 1)
        return arr;


    // DIVIDE
    int mid = arr.size() / 2;
    vector<int> left_half, right_half;

    for(int i = 0; i < mid; i++)
        left_half.push_back(arr[i]);

    for(int i = mid ; i < arr.size(); i++)
        right_half.push_back(arr[i]);

    vector<int> left_sorted = merge_sort(left_half),
                right_sorted = merge_sort(right_half);


    // CONQUER
    vector<int> sorted_arr;
    int idx1 = 0, idx2 = 0;

    for(int i = 0; i < arr.size(); i++) {
        if (idx1 == left_sorted.size()) {
            sorted_arr.push_back(right_sorted[idx2]);
            idx2++;
        } else if (idx2 == right_sorted.size()) {
            sorted_arr.push_back(left_sorted[idx1]);
            idx1++;
        } else if (left_sorted[idx1] < right_sorted[idx2]) {
            sorted_arr.push_back(left_sorted[idx1]);
            idx1++;
        } else {
            sorted_arr.push_back(right_sorted[idx2]);
            idx2++;
        }
    }

    return sorted_arr;
}

*/

vector<int> quick_sort(vector<int> a) {
    // Recursion End
    if(a.size() <= 1)
        return a;

    // DIVIDE
    int pivot = a.size() / 2;
    vector<int> left_half, right_half;

    for (int i = 0; i < a.size(); i++) {
        if(i == pivot) {
            continue;
        } else if (a[i] <= a[pivot]) {
            left_half.push_back(a[i]);
        } else {
            right_half.push_back(a[i]);
        }
    }

    vector<int> left_sorted = quick_sort(left_half),
                right_sorted = quick_sort(right_half);


    // CONQUER
    vector<int> sorted_arr;

    for (int i = 0; i < left_sorted.size(); i++) {
        sorted_arr.push_back(left_sorted[i]);
    }

    sorted_arr.push_back(a[pivot]);

    for (int i = 0; i < right_sorted.size(); i++) {
        sorted_arr.push_back(right_sorted[i]);
    }


    return sorted_arr;
}

int main() {

    vector<int>a = {5, 3, 7, 1, 8, 9};
    vector<int> s_arr = quick_sort(a);

    for(int i = 0; i < s_arr.size(); i++){
        cout << s_arr[i] << " ";
    }


    return 0;
}
