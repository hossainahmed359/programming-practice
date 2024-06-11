#include <stdio.h>

int main() {
    
    // Explore the 2d arr
    
    int row = 3, col = 3;
    int a[row][col]; 
    
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            // printf("%d,%d  ",i,j);
            scanf("%d", &a[i][j]);
            
        }
        
        // printf("\n");
    }
    
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            printf("%d ",a[i][j]);
        }
        
        printf("\n");
    }
    

    return 0;
}
