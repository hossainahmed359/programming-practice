myArray = [3, 7, 6, -10, 15, 23.5, 55, -13]


# def merge(arr_one, arr_two):
#     merged = []
#     i, j = 0, 0

#     while i < len(arr_one) and j < len(arr_two):
#         if arr_one[i] < arr_two[j]:
#             merged.append(arr_one[i])
#             i+=1
#         else:
#             merged.append(arr_two[j])
#             j+=1

#     arr_one_tail, arr_two_tail = arr_one[i:], arr_two[j:]

#     return merged + arr_one_tail + arr_two_tail

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left, right = arr[:mid], arr[mid:]

#     left_sorted, right_sorted = merge_sort(left), merge_sort(right)
#     sorted_arr = merge(left_sorted, right_sorted)


#     return sorted_arr

# sorted_arr = merge_sort(myArray)
# print(sorted_arr)

# def merge(arr_one, arr_two):
#     merged = []
#     i, j = 0, 0

#     while i < len(arr_one) and j < len(arr_two):
#         if arr_one[i] < arr_two[j]:
#             merged.append(arr_one[i])
#             i += 1
#         else:
#             merged.append(arr_two[j])
#             j += 1

#     arr_one_tail, arr_two_tail = arr_one[i:], arr_two[j:]

#     return merged + arr_one_tail + arr_two_tail

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left, right = arr[:mid], arr[mid:]

#     left_sorted, right_sorted = merge_sort(left), merge_sort(right)
#     sorted_arr = merge(left_sorted, right_sorted)

#     return sorted_arr

# sorted_arr = merge_sort(myArray)
# print(sorted_arr)


# def merge(arr_one, arr_two):
#     merged = []
#     i, j = 0, 0

#     while i < len(arr_one) and j < len(arr_two):
#         if arr_one[i] < arr_two[j]:
#             merged.append(arr_one[i])
#             i+=1
#         else:
#             merged.append(arr_two[j])
#             j += 1

#     arr_one_tail, arr_two_tail = arr_one[i:], arr_two[j:]

#     return merged + arr_one_tail + arr_two_tail

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left, right = arr[:mid], arr[mid:]

#     left_sorted, right_sorted = merge_sort(left), merge_sort(right)
#     sorted_arr = merge(left_sorted, right_sorted)

#     return sorted_arr

# sorted_arr = merge_sort(myArray)
# print(sorted_arr)

# myArray = [3, 7, 6, -10, 15, 23.5, 55, -13]
# def merge(arr_one, arr_two):
#     merged = []
#     i, j = 0, 0

#     while i < len(arr_one) and j < len(arr_two):
#         if arr_one[i] < arr_two[j]:
#             merged.append(arr_one[i])
#             i += 1
#         else:
#             merged.append(arr_two[j])
#             j += 1

#     arr_one_tail, arr_two_tail = arr_one[i:], arr_two[j:]

#     return merged + arr_one_tail + arr_two_tail

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left, right = arr[:mid], arr[mid:]

#     left_sorted, right_sorted = merge_sort(left), merge_sort(right)
#     sorted_arr = merge(left_sorted, right_sorted)

#     return sorted_arr


# new_arr = merge_sort(myArray)
# print(new_arr)


# myArray = [3, 7, 6, -10, 15, 23.5, 55, -13]

def merge(arr_one, arr_two):
    merged = []
    i, j = 0, 0

    while i < len(arr_one) and j < len(arr_two):
        if arr_one[i] < arr_two[j]:
            merged.append(arr_one[i])
            i += 1
        else:
            merged.append(arr_two[j])
            j += 1

    arr_one_tail, arr_two_tail = arr_one[i:], arr_two[j:]

    return merged + arr_one_tail + arr_two_tail

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    sorted_arr = merge(left_sorted, right_sorted)

    return sorted_arr

new_arr = merge_sort(myArray)
# print(new_arr)
