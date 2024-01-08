# Basic Loop

# 1. Divisible by Ten

"""Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

Return the count of how many numbers in the list are divisible by 10."""

# Answer
def divisible_by_ten(nums):
    count = 0
    for num in nums:
        if num % 10 == 0:
            count +=1
    return count

# Checks the result
print(divisible_by_ten([20, 25, 30, 35, 40]))

# 2. Greetings

"""Create a function named add_greetings() which takes a list of strings named names as a parameter.

In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' 

in front of each name in names and append the greeting to the list.

Return the new list containing the greetings."""


# Answer
def add_greetings(names):
    list = []
    for name in names:
        greeting = f"Hello, {name}"
        list.append(greeting)
    return list

# Checks the result
print(add_greetings(["Owen", "Max", "Sophie"]))


# 3. Delete starting Even NUmbers

"""Write a function called delete_starting_evens() that has a parameter named my_list.

The function should remove elements from the front of my_list until the front of the list is not even. 

The function should then return my_list.

For example if my_list started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(my_list) should return [11, 12, 15].

Make sure your function works even if every element in the list is even!"""

# Answer

# Solution 1
# def delete_starting_evens(my_list):
#     while len(my_list) > 0 and my_list[0] % 2 == 0 :
#         my_list = my_list[1:]
#     return my_list

# Solution 2
def delete_starting_evens(my_list):
  # Find the index of the first odd number
  for i in range(len(my_list)):
    if my_list[i] % 2 != 0:
      return my_list[i:]
  # If no odd number is found, return an empty list
  return []

# Check the result
print(delete_starting_evens([4, 8 ,10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# 4. Odd Indices

"""Create a function named odd_indices() that has one parameter named my_list.

The function should create a new empty list and add every element from my_list that has an odd index.

The function should then return this new list.

For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2]."""

# Answer

# Solution 1
# def odd_indices(my_list):
#   new_list = []
#   for i in range(len(my_list)):
#     if i % 2 != 0:
#       new_list.append(my_list[i])
#   return new_list

# Soultion 2
def odd_indices(my_list):
  return [my_list[i] for i in range(len(my_list)) if i % 2 != 0]

# Checks the result 
print(odd_indices([4, 3, 7, 10, 11, -2]))


# 5. Exponents

"""Create a function named exponents() that takes two lists as parameters named bases and powers. 

Return a new list containing every number in bases raised to every number in powers.

For example, consider the following code.

exponents([2, 3, 4], [1, 2, 3])

the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. 

Then two to the second. Then two to the third, and so on."""

# Answer

# Solution 1
# def exponents(bases, powers):
#   new_list = []
#   for base in bases:
#     for power in powers:
#       new_list.append(base ** power)
#   return new_list

# Solution 2
def exponents(bases, powers):
  return [base ** power for base in bases for power in powers]

# Checks the result
print(exponents([2, 3, 4], [1, 2, 3]))


# Adavnced Loop

# 1. Larger Sum

"""Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

The function should return the list whose elements sum to the greater number. 

If the sum of the elements of each list are equal, return lst1."""

# Answer

# Solution 1
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for num1 in lst1:
    sum1 += num1
  for num2 in lst2:
    sum2 += num2
  if sum1 >= sum2:
    return lst1
  else:
    return lst2

# Solution 2
def larger_sum(lst1, lst2):
  if sum(lst1) >= sum(lst2):
    return lst1
  else:
    return lst2
    
# Checks the result
print(larger_sum([1, 9, 5], [2, 3, 10]))


# 2. Over 9000

"""Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

The function should sum the elements of the list until the sum is greater than 9000. 

When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000,

the function should return total sum of all the elements. If the list is empty, the function should return 0.

For example, if lst was [8000, 900, 120, 5000], then the function should return 9020."""

# Answer

def over_nine_thousand(lst):
  sum = 0
  for item in lst:
    sum += item
    if sum > 9000:
      break
  return sum

# Checks the result
print(over_nine_thousand([8000, 900, 120, 5000]))

# 3. Max Num

"""Create a function named max_num() that takes a list of numbers named nums as a parameter.

The function should return the largest number in nums"""

# Answer

# Solution 1
# def max_num(nums):
#   # Get the list in descending order
#   nums.sort(reverse=True)

#   # Return the first list element
#   return nums[0]

# Solution 2
def max_num(nums):
  # Set default value
  max_value = nums[0]
  # Loop through nums
  for num in nums:
    # Set condition to compare and replace the max_value with elements inside the nums
    if num > max_value:
      max_value = num
  # Return the max number
  return max_value

# Checks the solution
print(max_num([50, -10, 0, 75, 20]))

# 4. Same Values

"""Write a function named same_values() that takes two lists of numbers of equal size as parameters.

The function should return a list of the indices where the values were equal in lst1 and lst2.

For example, the following code should return [0, 2, 3]

same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
"""

# Answer

def same_values(lst1, lst2):
  # Create an empty new list
  new_list = []
  # We Need to search the same elements in list 1 and list 2 index
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
  # Append the index with the same values in both list into new list
      new_list.append(index)
  # Return the new list
  return new_list

# Checks the result
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


# 5. Reversed List

"""Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True."""


# Answer
def reversed_list(lst1, lst2):
    # Loop through each index in the range of the length of lst1
    for i in range(len(lst1)):
        # If the element in lst1 at the current index is not equal to
        # the element in lst2 at the corresponding index from the end
        if lst1[i] != lst2[-i - 1]:
            # Return False because the lists are not reversed
            return False

    # If we've gone through the entire loop and haven't returned False,
    # then the lists are reversed of each other
    return True
  
# Checks the result
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
