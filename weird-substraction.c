
#include <stdio.h>

int main() {
    // THE WRONG SUBSTRACTION
    int n,k,s;
    
    scanf("%d %d", &n, &k);
    
    s = 0;
    
    while(k > 0){
        if(n%10==0) {
            s = n / 10;
        } else {
            s = n - 1;
        }
        
        n = s;
        k--;
    }
    
    printf("%d",s);

    return 0;
}
