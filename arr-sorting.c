// ======= BUBBLE SORT =======

#include <stdio.h>
#include <stdbool.h>

int main() {
    int arr[] = {15, 7, 3, 10, 5, 11, 9};
    int len = sizeof(arr) / sizeof(arr[0]);
    
    // printf("%d \n", len);
    
    for(int i = 0; i < len - 1; i ++) {
        int swapped = false;
        
        for(int j = i + 1; j < len; j++) {
            if(arr[i] > arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                swapped = true;
            }
        }
        
        if(swapped == false) {
            break;
        }
        
    }
    
    for(int i = 0; i < len ; i ++){
        printf("%d ", arr[i]);
    }

    return 0;
}


// ======= SELECTION SORT =======


#include <stdio.h>
#include <stdbool.h>

int main() {
    int arr[] = {15, 7, 3, 10, 5, 11, 9};
    int len = sizeof(arr) / sizeof(arr[0]);

    for(int i = 0; i < len - 1; i++) {
        int min_index = i;
        
        for(int j = i + 1; j < len; j++) {
            if (arr[j] < arr[min_index]){
                min_index = j;
            }
        }

        int temp = arr[i];
        arr[i] = arr[min_index];
        arr[min_index] = temp;
    }

    for(int i = 0; i < len; i++) {
        printf("%d ",arr[i]);
    }

    return 0;
}

























