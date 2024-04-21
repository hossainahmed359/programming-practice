import random
unsorted_list = [1, 2, 0, 3, 6, 11, 5]
big_unsorted_list = [random.randint(1,100000) for _ in range(100000)]

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        arr = quick_sort(arr, low, pivot_index - 1)
        arr = quick_sort(arr, pivot_index+1, high)
    return arr

sorted_arr = quick_sort(unsorted_list)
print(sorted_arr)