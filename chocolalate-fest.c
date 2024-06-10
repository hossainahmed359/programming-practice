#include <stdio.h>

int main() {
    
    int n,w,t;
    
    n = 100;
    w = n;
    
    while(w>=4){
        int result;
        result = (w/4);
        t += result;
        w = result + (w%4);
    }
    
    printf("total extra chocolates =  %d",t);
    
    return 0;
}
