#include <bits/stdc++.h>

using namespace std;

vector<int> quick_sort(vector<int> &arr) {
    if(arr.size() <= 1)
        return arr;

    // DIVIDE
    // int pivot = arr.size() - 1;
    //int pivot = arr.size() / 2;

    int pivot = rand()%(arr.size());

    vector<int>b,c;

    for(int i = 0; i < arr.size(); i++) {
        if(i == pivot) {
            continue;
        } else if (arr[i] <= arr[pivot]) {
            b.push_back(arr[i]);
        } else {
            c.push_back(arr[i]);
        }
    }

    vector<int> sorted_b = quick_sort(b);
    vector<int> sorted_c = quick_sort(c);

    // CONQUER
    vector<int> sorted_arr;

    for(int i = 0; i < sorted_b.size(); i++)
        sorted_arr.push_back(sorted_b[i]);

    sorted_arr.push_back(arr[pivot]);

    for(int j = 0; j < sorted_c.size(); j++)
        sorted_arr.push_back(sorted_c[j]);

    return sorted_arr;

}

int main() {

    vector<int>arr = {5, 3, 7, 1, 8, 9};
    vector<int> sorted_arr = quick_sort(arr);

    for(int i = 0; i < sorted_arr.size(); i++){
        cout << sorted_arr[i] << " ";
    }

    return 0;
}
