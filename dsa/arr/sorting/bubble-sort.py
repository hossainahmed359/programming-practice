# Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

# How it works:

# 1.Go through the array, one value at a time.
# 2.For each value, compare the value with the next value.
# 3.If the value is higher than the next one, swap the values so that the highest value comes last.
# 4.Go through the array as many times as there are values in the array.

# unsorted_list = [7, 12, 5, 11, 3, 1, 0]

unsorted_list = [40, 99, 50, 42, 67, 7, 52, 11, 96, 19, 31, 4, 26, 88, 63, 12, 53, 77, 82, 85, 24, 64, 65, 55, 91, 23, 27, 43, 1, 29, 66, 61, 92, 79, 98, 69, 8, 75, 94, 38, 78, 41, 59, 36, 34, 60, 68, 89, 62, 33, 45, 10, 73, 44, 46, 17, 21, 15, 18, 74, 47, 37, 95, 2, 6, 30, 51, 13, 81, 97, 71, 28, 14, 84, 86, 54, 100, 20, 56, 70, 49, 76, 35, 32, 39, 80, 57, 58, 87, 48, 5, 3, 72, 93, 9, 16, 25, 90, 83, 22]

# Implementation

# 1.An array with values to sort.
# 2.An inner loop that goes through the array and swaps values if the first value is higher than the next value. This loop must loop through one less value each time it runs.
# 3.An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.

def bubble_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n-1):
        swapped = False
        j = 0
        while j < n-i-1 :
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            j+=1
        if not swapped:
            break
    return arr

def bubble_sort_w3_schools(unsorted_list):
    n = len(unsorted_list)

    for i in range(n-1):
        swapped = False

        for j in range(n-i-1) :
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
                swapped = True

        if not swapped:
            break

    return unsorted_list


sorted_list = bubble_sort_w3_schools(unsorted_list)
print(sorted_list)