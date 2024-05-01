def hash_function(value):
    sum_of_chars = 0
    for char in value:
        print(ord(char), '========')
        sum_of_chars += ord(char)


    print(sum_of_chars, '==========')
    return sum_of_chars % 10

print("'Bob' has hash code:",hash_function('Bob'))
