myArray = [3, 7, 6, -10, 15, 23.5, 55, -13]

def merge(arr1, arr2):
    merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    arr1_tail , arr2_tail = arr1[i:], arr2[j:]

    return merged + arr1_tail + arr2_tail

def merge_sort(arr):
    if len(arr) <= 1 :
        return arr

    mid = len(arr) // 2
    left, right = arr[:mid] , arr[mid:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    sorted_arr = merge(left_sorted, right_sorted)

    return sorted_arr

sortedArr = merge_sort(myArray)
print(sortedArr)