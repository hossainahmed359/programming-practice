myArray = [170, 44, 75, 90, 802, 24, 2, 66]

def radix_sort(arr):
    radix_arr = [[],[],[],[],[],[],[],[],[],[]]
    max_value = max(arr)
    exp = 1

    while max_value // exp > 0:
        while len(arr) > 0:
            value = arr.pop(0)
            radix_index = (value // exp) % 10
            radix_arr[radix_index].append(value)

        for bucket in radix_arr:
            while len(bucket) > 0:
                value = bucket.pop(0)
                arr.append(value)

        exp *= 10

    return arr

sorted_arr = radix_sort(myArray)
print(sorted_arr)

