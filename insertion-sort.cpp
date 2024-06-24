#include <bits/stdc++.h>

using namespace std;

int main() {
    
    int arr[] = {3, 1, 7, 5, 6, 19, 10, 15, 11, 12, 8};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    for (int i = 1; i < n; i++) {
        for (int j = i - 1; j >= 0; j--) {
            if(arr[j]  > arr[j+1] ) {
                swap(arr[j], arr[j+1]);
            }
        }
    }
    
    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    

    return 0;
}
