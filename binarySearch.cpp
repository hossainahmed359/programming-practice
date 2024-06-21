#include <bits/stdc++.h>

using namespace std;

int main() {
    
    int arr[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110};
    int target = 110;
    
    int n, mid, low, high;
    
    n = sizeof(arr)/sizeof(arr[0]);
    low = 0;
    high = n - 1;
    
    while(low <= high) {
        
        mid = (low + high) / 2;
        
        if(arr[mid] == target) {
           cout << "Found target at index " << mid;
           break;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    
    if (low > high) {
        cout << "Target not found";
    }

    return 0;
}

