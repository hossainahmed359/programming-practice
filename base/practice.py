""" a = 5
b = 2
if a * b > 20:
    print(f'a X b = {a * b} , a X b  > 20')
else :
    print(f'a X b = {a * b} , a X b  < 20')

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

def myFunc() :
    print('null and void')
    return 2

print(myFunc()) """

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # def __str__(self):
        # return self.name


    def my_new_fun(self, x, y):
        return f"{self.name} is {x} and {y}"

p1 = Person("John", 36, 'boy')

test_str = p1.my_new_fun('23', '33')
print(test_str)