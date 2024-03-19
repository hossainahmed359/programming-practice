unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3, 12]

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1


    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr


sorted_arr = counting_sort(unsortedArr)
print(sorted_arr)