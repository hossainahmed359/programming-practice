#include <bits/stdc++.h>

using namespace std;

int called = 0;
int save[100];

int fib (int n) {
    
    called++;
    
    if(n == 0) {
        return 0;
    }
    
    if (n == 1) {
        return 1;
    }
    
    if (save[n] != 0) {
        return save[n];
    }
    
    int x = fib(n-1) + fib(n-2);
    save[n] = x;
    return x;
}

int main() {
    // Write C++ code here
    
    int nth = fib(7);
    
    cout << nth << " Called -> "<< called << " times";

    return 0;
}

// Fibo -> 0, 1, 1, 2, 3, 5, 8, 13 ...
