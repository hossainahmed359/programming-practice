parent_list = [64, 34, 25, 12, 22, 11, 90, 5]



def insertion_sort_w3_schools(unsorted_list):
    n = len(unsorted_list)
    for i in range(1, n):
        insert_index = i
        current_value = unsorted_list[i]
        for j in range(i-1, -1, -1):
            if unsorted_list[j] > current_value:
                unsorted_list[j+1] = unsorted_list[j]
                insert_index = j
            else:
                break
        unsorted_list[insert_index] = current_value
    return unsorted_list


def insertion_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(1, n):
        current_value = arr[i]
        j = i - 1
        while j >= 0 and current_value < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current_value
    return arr

# new_list = insertion_sort(parent_list)
# print(new_list)


def insertion_sort_alt(arr):
    n = len(arr)
    for i in range(1,n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

# new_list_alt = insertion_sort_alt(parent_list)
# print(new_list_alt)