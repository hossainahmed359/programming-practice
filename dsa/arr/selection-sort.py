# The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.

# How it works:

# 1.Go through the array to find the lowest value.
# 2.Move the lowest value to the front of the unsorted part of the array.
# 3.Go through the array again as many times as there are values in the array.

# unsorted_list = [7, 12, 5, 11, 3, 1, 0]

# unsorted_list = [40, 99, 50, 42, 67, 7, 52, 11, 96, 19, 31, 4, 26, 88, 63, 12, 53, 77, 82, 85, 24, 64, 65, 55, 91, 23, 27, 43, 1, 29, 66, 61, 92, 79, 98, 69, 8, 75, 94, 38, 78, 41, 59, 36, 34, 60, 68, 89, 62, 33, 45, 10, 73, 44, 46, 17, 21, 15, 18, 74, 47, 37, 95, 2, 6, 30, 51, 13, 81, 97, 71, 28, 14, 84, 86, 54, 100, 20, 56, 70, 49, 76, 35, 32, 39, 80, 57, 58, 87, 48, 5, 3, 72, 93, 9, 16, 25, 90, 83, 22]


unsorted_list = [7, 12, 5, 11, 3, 1, 0]

def selection_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n-1):
        min_index = i
        j = i + 1
        while j < n :
            if arr[j] < arr[min_index]:
                min_index = j
            j +=1
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



def selection_sort_w3_schools(unsorted_list):
    n = len(unsorted_list)
    for i in range(n - 1) :
        min_index = i
        for j in range(i+1, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
        min_value = unsorted_list.pop(min_index)
        unsorted_list.insert(i, min_value)
    return unsorted_list


my_array = [64, 34, 25, 12, 22, 11, 90, 5]

def selection_sort_w3_schools_improved(unsorted_list):
    n = len(unsorted_list)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
        unsorted_list[i], unsorted_list[min_index] =  unsorted_list[min_index], unsorted_list[i]
    return unsorted_list

new_list = selection_sort_w3_schools_improved(my_array)
print(new_list)