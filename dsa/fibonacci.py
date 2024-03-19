# Fibonacci Series -> 0,1,1,2,3,5,8,13,21,34,55,89

# =============  USING LOOP ===============
""" a = 0
b = 1
fibonacci_series = [0, 1]

for i in range(18):
    new_fibonacci_value = a + b
    fibonacci_series.append(new_fibonacci_value)
    a = b
    b = new_fibonacci_value

print(fibonacci_series) """

# =============  USING RECURSION =============
def fibonacci (a, b, fibonacci_series_list, count, max_length) :
    new_fibonacci_value = a + b
    fibonacci_series_list.append(new_fibonacci_value)
    a = b
    b = new_fibonacci_value

    if count < max_length :
        count += 1
        fibonacci(a, b, fibonacci_series_list, count, max_length)
    else:
        print(fibonacci_series_list)
        return


# fibonacci(0, 1, [0,1], 0, 18)

# ============= FINDING THE nth ==================
count=0

def F(n):
    if n <= 1:
        return n
    else:
        global count
        count += 1
        print(f'Recursion Call {count}')
        return F(n-2) + F(n-1)


n = 20
print(f"The {n}th Fibonacci number is {F(n)}")