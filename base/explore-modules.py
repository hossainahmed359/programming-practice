import platform
import datetime

# x = platform.system()
# y = platform.architecture()
# print(x, y)


# test_module.print_test('Echo 001')

z = datetime.datetime.now()
# print(z)
# print(z.year)
# print(z.strftime("%A"))

import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
# print(json.loads(x))
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))


l = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# print(l)
# print(json.dumps(l,  indent=4 , separators=(". ", " = ")))


username = input("Enter username:")
print("Username is: " + username)