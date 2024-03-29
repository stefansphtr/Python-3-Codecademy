# Basic Function

# 1. Tenth Power

"""Write a function named tenth_power() that has one parameter named num.

The function should return num raised to the 10th power."""

# Answer

def tenth_power(num):
  return num**10

# Checks the results

print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

# 2. Square Root

"""Write a function named square_root() that has one parameter named num.

Use exponents (**) to return the square root of num."""

# Answer

def square_root(num):
  return int(num**(1/2))

# Checks the results

print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

# 3. Win Percentage

"""Create a function called win_percentage() that takes two parameters named wins and losses.

This function should return out the total percentage of games won by a team based on these two numbers."""

# Answer

def win_percentage(wins, losses):
  total_games = wins + losses
  ratio_win = wins / total_games
  ratio_win *= 100
  return int(ratio_win)

# Check the results

print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

# 4. Average

"""Write a function named average() that has two parameters named num1 and num2.

The function should return the average of these two numbers."""

# Answer

# Solution 1
def average(*args):
    return sum(args) / len(args)

# Solution 2
def average(num1, num2):
  sum = num1 + num2
  avg = sum / 2
  return avg

# Check the results

print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

# 5. Remainder

"""Write a function named remainder() that has two parameters named num1 and num2.

The function should return the remainder of twice num1 divided by half of num2."""

# Answer

def remainder(num1, num2):
  # Multiply the first input by 2
  new_num1 = num1 * 2
  # Divide the second input by 2
  new_num2 = num2 / 2
  # Calculate the remainder from modified first by second input
  return new_num1 % new_num2

# Checks the results

print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

# Advanced Function

# 1. First Three Multiplies

"""Write a function named first_three_multiples() that has one parameter named num.

This function should print the first three multiples of num. Then, it should return the third multiple.

For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21."""

# Answer

def first_three_multiples(num):
  print(num*1)
  print(num*2)
  print(num*3)
  return num*3

# Checks the results

first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

# 2. Tip

"""Create a function called tip() that has two parameters named total and percentage.

This function should return the amount you should tip given a total and the percentage you want to tip."""

# Answer

# Solution 1
# def tip(total, percentage):
#     return total*(percentage/100)

# Solution 2
def tip(total, percentage):
    tip_amount = total * (percentage/100)
    return tip_amount

# Checks the results

print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

# 3. Bond, James Bond

"""Write a function named introduction() that has two parameters named first_name and last_name.

The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name."""

# Answer

# Solution 1
# def introduction(first_name, last_name):
#   return f"{last_name}, {first_name} {last_name}"

# Solution 2
def introduction(first_name, last_name):
  return str(last_name) + ", " + str(first_name) + " " + str(last_name)

# Checks the results

print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

# 4. Dog Years

"""Some say that every one year of a human’s life is equivalent to seven years of a dog’s life.

Write a function named dog_years() that has two parameters named name and age.

The function should compute the age in dog years and return the following string:

"{name}, you are {age} years old in dog years"

Test this function with your name and your age!"""

# Answer

# Solution 1
# def dog_years(name, age):
#   return str(name) + ', ' + 'you are ' + str(age * 7) + " years old in dog years" 

# Solution 2
def dog_years(name, age):
  return f"{name}, you are {age * 7} years old in dog years"

# Checks the results

print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

# 5. All Operations

"""Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d.

The function should print 3 lines and return 1 value.

First, print the sum of a and b.

Second, print c minus d.

Third, print the first number printed, multiplied by the second number printed.

Finally, return the third number printed modulo a."""

# Answer

def lots_of_math(a, b, c, d):
  first_operation = a + b
  second_operation = c - d
  third_operation = first_operation * second_operation
  final_operation = third_operation % a
  print(first_operation)
  print(second_operation)
  print(third_operation)
  return final_operation

# Checks the results
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0