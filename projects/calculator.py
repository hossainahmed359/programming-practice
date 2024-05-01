print('========= PYTHON CALCULATOR ============')

input_one = float(input('Enter first number:'))
input_two = float(input('Enter second number:'))

print("""
Enter 1 for + or Addition /n
Enter 2 for - or Subtraction /n
Enter 3 for X or Multiplication /n
Enter 4 for / or Division""")

input_three = int(input('Enter a number from 1 - 4:'))


if input_three == 1 :
    print(f'The output of {input_one} + {input_two} = {input_one + input_two}')

if input_three == 2 :
    print(f'The output of {input_one} - {input_two} = {input_one - input_two}')

if input_three == 3 :
    print(f'The output of {input_one} X {input_two} = {input_one * input_two}')

if input_three == 4 :
    print(f'The output of {input_one} / {input_two} = {input_one / input_two}')