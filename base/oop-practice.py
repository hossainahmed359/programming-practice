# ********** CONCEPTS OF OOP **********

# ============== CLASS ==============
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"name={self.name} ,age={self.age}"

    def custom_func(self) :
        return self.age * 2



# ============== INHERITANCE ==============
class Inherited_Person(Person):
    pass

# ============== USAGE OF SUPER ==============
class Student(Person):
    def __init__(self, name, age, college, roll) -> None:
        # FIRST
        # Person.__init__(self, name, age)

        # SECOND
        super().__init__(name, age)
        self.college = college
        self.roll = roll

    def __str__(self) -> str:
        return f"""
        name={self.name},
        age={self.age},
        college={self.college},
        roll={self.roll}"""

# ============== INSTANCES  ==============
per_one = Person('Alex', 26)
per_two = Inherited_Person('Max ', 66)
student_one = Student('John', 16, "Dhaka Residential", 4531)

# ============== PRINTS  ==============
print(student_one)


# ============== DICTIONARY  ==============
""" dict = {
    'name': 'Hossain Ahmed Madani',
    'age': 26,
}

print(dict) """