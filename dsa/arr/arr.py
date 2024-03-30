unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]

def merge(arr1, arr2):
    merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1

    arr1_tail = arr1[i:]
    arr2_tail = arr2[j:]

    return merged + arr1_tail + arr2_tail

def merge_sort(arr):
    if len(arr) <= 1 : return arr

    mid = len(arr) // 2
    left, right= arr[:mid],  arr[mid:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    sorted_arr = merge(left_sorted, right_sorted)

    return sorted_arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j], = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low= 0, high = None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        arr = quick_sort(arr, low, pivot_index - 1)
        arr = quick_sort(arr, pivot_index + 1, high)
    return arr

def bubble_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n-1):
        j = 0
        swapped = False
        while j < n-i-1:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            j+=1
        if not swapped:
            break
    return arr


def selection_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n-1):
        min_index = i
        j = i + 1
        while j < n:
            if arr[j] < arr[min_index]:
                min_index = j
            j += 1
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

def selection_sort_alt(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1, n):
        insert_value = arr[i]
        j = i - 1
        while j >= 0 and insert_value < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = insert_value
    return arr

def insertion_sort_alt(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1, n):
        insert_value = arr[i]
        j = i
        while j > 0 and insert_value < arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr


def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)

    while len(arr) > 0:
        value = arr.pop(0)
        count[value] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr

new_arr = counting_sort(unsortedArr)
print(new_arr)