#include <stdio.h> 
  
int main() 
{ 
    int rows,i,j,k;
    rows = 10;
    
    // Right Half Pyramid Pattern
    printf("Right Half Pyramid Pattern \n");
    
    for(i=0;i<rows;i++){
        for(j=0;j<=i;j++){
            printf("* ");
        }
        
        printf("\n");
    }
    
    // Left Half Pyramid Pattern
    printf("Left Half Pyramid Pattern \n");
     
    for(i=0;i<rows;i++){
        for(j=0;j < 2 * (rows - i) -1;j++){
            printf(" ");
        }
        
        for(k=0;k<=i;k++){
            printf("* ");
        } 
         
        printf("\n");
    }
    
    // Full Pyramid Pattern
    printf("Full Pyramid Pattern \n");
    
    for(i=0;i<rows;i++){
        
        for(j=0;j< 2 * (rows - i) -1;j++){
            printf(" ");
        }
        
        for(k=0;k<2*i+1;k++){
            printf("* ");
        }
        
        printf("\n");
    }

    // Hollow Square Pattern
    printf("Hollow Square Pattern \n");
    
    for(i=0;i<rows;i++){
        for(j=0;j<rows;j++){
            if(i > 0 && i != rows - 1 && j > 0 && j != rows - 1){
                printf("  ");
            } else {
                printf("* ");
            }
        }
        
        printf("\n");
    }
  
    
    return 0; 
}
