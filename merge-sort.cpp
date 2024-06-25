#include <bits/stdc++.h>

using namespace std;

// MERGE
void merge(vector<int>& arr, int left, int mid, int right)
{
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<int> leftHalf(n1);
    vector<int> rightHalf(n2);

    for(int i = 0; i < n1; i++)
        leftHalf[i] = arr[left + i];
    for(int i = 0; i < n2; i++)
        rightHalf[i] = arr[mid + 1 + i];

    int i = 0, j = 0, k = left;

    while(i < n1 && j < n2) {
        if(leftHalf[i] <= rightHalf[j]) {
            arr[k] = leftHalf[i];
            i++;
        } else {
            arr[k] = rightHalf[j];
            j++;
        }
        k++;
    }

    while(i < n1) {
        arr[k] = leftHalf[i];
        i++;
        k++;
    }

    while(j<n2) {
        arr[k] = rightHalf[j];
        j++;
        k++;
    }
}

// MERGE SORT
void mergeSort(vector<int>& arr, int left, int right)
{
    if(left < right) {
        int mid = left + (right - left) /2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid+1, right);

        merge(arr, left, mid, right);
    }
}


int main() {

    vector<int> arr = {12, 11, 13, 5, 6, 7};
    int len = arr.size();

    mergeSort(arr, 0, len-1);

    cout << "\nSorted array is \n";
    for (int i = 0; i < len; i++)
        cout << arr[i] << " ";


    return 0;
}
