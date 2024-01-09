# Basic Challenges Control Flow

# 1. Not Sum to Ten
"""You are given two numbers stored in num1 and num2. 
If the sum of num1 and num2 is NOT equal to 10, then 
store True into a variable called not_ten, 
otherwise store False in not_ten."""

num1 = 6
num2 = 3

# Answer
if num1 + num2 != 10:
    not_ten = True
else:
    not_ten = False

# Uncomment the below lines to show the result
print(f"Does the sum of the numbers equal 10? {not_ten}")

# 2. Over Budget

"""You are given a monthly budget and some expenses and need to check if the sum of the expenses goes over budget!

First, store the total of all expenses into a variable called total.

Next, check if the total is greater than the budget. If it is, store True into a variable called over_budget, 

otherwise store False in over_budget."""

# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculate the total amount of expene
total = food_bill + electricity_bill + internet_bill + rent

# Check if the total is greater than budget and store the result in over_budget
if total > budget:
    over_budget = True
else:
    over_budget = False

# Check the result

print(f"Total: {total}")
print(f"Is it over budget? {over_budget}")


# 3. Large Power

"""Create a function named large_power() that takes two parameters named base and exponent.

If base raised to the exponent is greater than 5000, return True, otherwise return False"""

# Answer


def large_power(base, exponent):
    if base**exponent > 5000:
        return True
    else:
        return False


# 4. Twice as Large

"""Create a function named twice_as_large() that has two parameters named num1 and num2.

Return True if num1 is more than double num2. Return False otherwise."""

# Answer


def twice_as_large(num1, num2):
    if num1 > num2 * 2:
        return True
    else:
        return False


# Check the result

print(twice_as_large(10, 5))
print(twice_as_large(11, 5))

# Divisible by Ten

"""Create a function called divisible_by_ten() that has one parameter named num.

The function should return True if num is divisible by 10, and False otherwise. 

Consider using modulo operator % to check for divisibility."""

# Amswer


def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


# Check the result
print(divisible_by_ten(20))  # This should print True
print(divisible_by_ten(25))  # This should print False


# Advanced Challenges Control Flow

# 1. In Range

"""Create a function named in_range() that has three parameters named num, lower, and upper.

The function should return True if num is greater than or equal to lower and less than or equal to upper. 

Otherwise, return False."""


# Answer
def in_range(num, lower, upper):
    if (num >= lower) and (num <= upper):
        return True
    else:
        return False


# Check the result
print(in_range(10, 10, 10))  # This should print True
print(in_range(5, 10, 20))  # This should print False

# 2. Same Name

"""Create a function named same_name() that has two parameters named your_name and my_name.

If our names are identical, return True. Otherwise, return False."""


# Answer
def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False


# Check the result
print(same_name("Colby", "Colby"))  # This should return True
print(same_name("Tina", "Amber"))  # This should return False

# 3. Always False

"""Create a function named always_false() that has one parameter named num.

Using an if statement, your variable num, and the operators >, and <, 

make it so your function will return False no matter what number is stored in num.

An if statement that is always false is called a contradiction. 

You will rarely want to do this while programming, 

but it is important to realize it is possible to do this."""

# Answer

# Solution 1
# def always_false(num):
#     if num >= 0 or num < 0:
#         return False
#     else:
#         return True

# Solution 2

# def always_false(num):
#     if num >= 0:
#         return False
#     elif num < 0:
#         return False
#     else:
#         return True

# Solution 3


def always_false(num):
    if num > 0 and num < 0:
        return True
    else:
        return False


# Check the result
print(always_false(0))  # This should return False
print(always_false(-1))  # This should return False
print(always_false(1))  # This should return False

# 4. Movie Review

"""Create a function named movie_review() that has one parameter named rating.

If rating is less than or equal to 5, return "Avoid at all costs!". 

If rating is between 5 and 9, return "This one was fun.".

If rating is 9 or above, return "Outstanding!"""

# Answer


def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating >= 5 and rating < 9:
        return "This one was fun."
    else:
        return "Outstanding!"


# Check the result

print(movie_review(9))  # This should return Outstanding!
print(movie_review(4))  # Avoid at all costs!
print(movie_review(6))  # This one was fun.


# 5. Max Number

"""Create a function called max_num() that has three parameters named num1, num2, and num3.

The function should return the largest of these three numbers. 

If any of two numbers tie as the largest, you should return "It's a tie!"."""


def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "It's a tie!"


# Check the result

print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))
