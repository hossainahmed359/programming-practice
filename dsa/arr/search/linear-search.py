myArray = [3, 7, 6, -10, 15, 23.5, 55, -13]

def linear_search(arr, target_val):
    for i in range(len(arr)):
        if arr[i] == target_val:
            return i
    return -1

print(linear_search(myArray, -13))