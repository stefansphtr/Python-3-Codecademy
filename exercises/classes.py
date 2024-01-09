# Exercise 2
class Facade:
    pass


# Exercise 2
class Grade:
    minimum_passing = 65


six_grade = Grade()

print(six_grade.minimum_passing)


# Exercise 3
class DistanceConverter:
    kms_in_a_mile = 1.609

    def how_many_kms(self, miles):
        return miles * self.kms_in_a_mile


converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)


# Exercise 4
class Circle:
    pi = 3.14

    def area(self, radius):
        return self.pi * radius**2


circle = Circle()

pizza_area = circle.area(12 // 2)
teaching_table_area = circle.area(36 // 2)
round_room_area = circle.area(11460 // 2)

print(pizza_area)
print(teaching_table_area)
print(round_room_area)


# Exercise 5
class Circle:
    pi = 3.14

    # Add constructor here:
    def __init__(self, diameter):
        print(f"New circle with diameter: {diameter}")


teaching_table = Circle(36)


# Exercise 6
class Shuoter:
    def __init__(self, phrase):
        if type(phrase) == str:
            print(phrase.upper())


shout1 = Shuoter("aal is gettng bigger and bigger")


# Exercise 7
class Store:
    pass


alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

# Join the strings together
store_string = "This is the first object with the same class: {}, and this is the second one {}".format(
    alternative_rocks.store_name, isabelles_ices.store_name
)

print(store_string)

# Exercise 8
can_we_count_it = [{"s": False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for item in can_we_count_it:
    if hasattr(item, "count"):
        print("{} has the count attribute!".format(str(type(item))))
    else:
        print("{} does not have the count attribute :(".format(str(type(item))))


# Exercise 9
class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:
        self.radius = diameter / 2

    def circumference(self):
        return 2 * self.pi * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())


# Exercise 10
dir(10)


def this_function_is_an_object(item):
    return "This is only for a test"


print(dir(this_function_is_an_object))

# Exercise 11

from datetime import datetime


class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
        self.attendance = {}

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)

    def get_average(self):
        return (
            sum(grade.score for grade in self.grades) / len(self.grades)
            if self.grades
            else 0
        )

    def add_attendance(self, date, is_present):
        self.attendance[date] = is_present


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def is_passing(self):
        return self.score >= self.minimum_passing


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


pieter.add_grade(Grade(100))
pieter.add_attendance(datetime.now().date(), True)

print(pieter.get_average())
print(pieter.attendance)

"""
Explanation for Exercsie 11:

The answer fro exercises 11 defines two classes: `Student` and `Grade`.

The `Student` class represents a student with properties like name, year, grades, and attendance. 

It has methods to add a grade, calculate the average grade, and record attendance.

The `Grade` class represents a grade with a score and a method to check if the grade is passing (score is 65 or above).

Here's a breakdown of what the code does:

1.  `from datetime import datetime`: This line imports the `datetime` module, which provides functions to work with dates and times.  

2.  `class Student:`: This line defines a new class named `Student`.  

3.  Inside the `Student` class, the `__init__` method is defined. This is a special method that gets called   
    when a new `Student` object is created. It initializes the properties of the student: name, year, grades (a list), 
    and attendance (a dictionary).  

4.  The `add_grade` method adds a `Grade` object to the student's grades list.  

5.  The `get_average` method calculates the average of the student's grades.  

6.  The `add_attendance` method records whether the student attended school on a specific date. 

7.  `class Grade:`: This line defines a new class named `Grade`.  

8.  Inside the `Grade` class, the `__init__` method initializes the score of the grade. The `is_passing` method checks 
    if the grade is passing (score is 65 or above).  

9.  Three `Student` objects are created: `roger`, `sandro`, and `pieter`. 

10   A `Grade` object with a score of 100 is added to `pieter`'s grades.  

11   `pieter`'s attendance is recorded for today's date.  

12   The average grade of `pieter` is printed.  

13   `pieter`'s attendance is printed.

"""
