unsorted_list = [7, 12, 5, 11, 3, 1, 0]

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        arr = quick_sort(arr, low, pivot_index - 1)
        arr = quick_sort(arr, pivot_index+1, high)

    return arr

sortedArr = quick_sort(unsorted_list)
print(sortedArr)