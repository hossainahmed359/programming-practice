my_array = [ 2, 3, 7, 7, 11, 15, 25]

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1


    return -1

target_index = binary_search(my_array, 25)
print(target_index)