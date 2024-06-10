// https://phitron.io/ph232/video/ph232-5-2-chocolate-problem-my-favorite-

#include <stdio.h>

int main() {
    
    int choc,pack;
    
    choc = 100;
    pack = choc;
    
    while(pack>=4) {
        choc += (pack/4);
        pack = (pack/4) + (pack%4);
    }
    
    printf("total amount of chocolates =  %d",choc);
    
    return 0;
}
