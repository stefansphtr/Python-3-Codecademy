# Basic Dictionary

# 1. Sum Values

"""Write a function named sum_values that takes a dictionary named my_dictionary as a parameter.

The function should return the sum of the values of the dictionary"""

# Answer

# Solution 1
# def sum_values(dictionary):
#   return sum(dictionary.values())


# Solution 2
def sum_values(dictionary):
    sum = 0
    for num in dictionary.values():
        sum += num
    return sum


# checks the result

print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# should print 10
print(sum_values({10: 1, 100: 2, 1000: 3}))
# should print 6

# 2. Even Keys

"""Create a function called sum_even_keys that takes a dictionary named my_dictionary,

with all integer keys and values, as a parameter. This function should return 

the sum of the values of all even keys."""

# Answer

# Solution 1
# def sum_even_keys(dict):
#   sum = 0
#   for key in dict.keys():
#     if key % 2 == 0:
#       sum += dict[key]
#   return sum


# Solution 2
def sum_even_keys(dict):
    return sum({dict[key] for key in dict.keys() if key % 2 == 0})


# Checks the result
print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
# should print 6

# 3.Add Ten

"""Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter.

The function should add 10 to every value in my_dictionary and return my_dictionary"""


# Answer
def add_ten(my_dictionary):
    for key in my_dictionary:
        my_dictionary[key] += 10
    return my_dictionary


# Checks the result
print(add_ten({1: 5, 2: 2, 3: 3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10: 1, 100: 2, 1000: 3}))
# should print {10:11, 100:12, 1000:13}

# 4. Values that are Keys

"""Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 

This function should return a list of all values in the dictionary that are also keys."""

# Answer

# Solution 1
# def values_that_are_keys(my_dictionary):
#   values_and_keys = []
#   for value in my_dictionary.values():
#     if value in my_dictionary.keys():
#       values_and_keys.append(value)
#   return values_and_keys


# Solution 2
def values_that_are_keys(my_dictionary):
    return [value for value in my_dictionary.values() if value in my_dictionary.keys()]


# Cheks the result
print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# should print ["a"]

# 5. Largest value

"""Write a function named max_key that takes a dictionary named my_dictionary as a parameter.

The function should return the key associated with the largest value in the dictionary."""

# Answer

# Solution 1
# def max_key(my_dictionary):
#   largest_key = float("-inf")
#   largest_value = float("-inf")
#   for key,value in my_dictionary.items():
#     if value > largest_value:
#       largest_value = value
#       largest_key = key
#   return largest_key


# Solution 2
def max_key(my_dictionary):
    largest_key = None
    largest_value = None
    for key, value in my_dictionary.items():
        if largest_value is None or value > largest_value:
            largest_value = value
            largest_key = key
    return largest_key


# Checks the result
print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# should print 1
print(max_key({"a": 100, "b": 10, "c": 1000}))
# should print "c"


# Advanced Dictionary

# 1. Word Length Dict

"""Write a function named word_length_dictionary that takes a list of strings named words as a parameter.

The function should return a dictionary of key/value pairs where every key is a word in words and 

every value is the length of that word."""

# Answer
# Solution 1
# def word_length_dictionary(words):
#   dict = {}
#   for word in words:
#     dict[word] = len(word)
#   return dict


# Solution 2
def word_length_dictionary(words):
    return {word: len(word) for word in words}


# Checks the result
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# 2. Frequency Count

"""Write a function named frequency_dictionary that takes a list of elements named words as a parameter.

The function should return a dictionary containing the frequency of each element in words."""


# Answer
def frequency_dictionary(words):
    freq_word = {}
    for word in words:
        if word in freq_word:
            freq_word[word] += 1
        else:
            freq_word[word] = 1
    return freq_word


# Checks the result
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0]))
# should print {0:5}

# 3. Unique Values

"""Create a function named unique_values that takes a dictionary named my_dictionary as a parameter.

The function should return the number of unique values in the dictionary."""

# Answer

# Solution 1
# def unique_values(my_dictionary):
#   """Count the number of unique values in the given dictionary"""
#   unique = []
#   unique_val = 0
#   for value in my_dictionary.values():
#     if value not in unique:
#       unique.append(value)
#       unique_val += 1
#   return unique_val


# Solution 2
def unique_values(my_dictionary):
    """Count the number of unique values in the given dictionary"""
    unique = []
    for value in my_dictionary.values():
        if value not in unique:
            unique.append(value)
    return len(unique)


# Cheks the result
print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
# should print 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
# should print 1

# 4. Count First Letter

"""
Create a function named count_first_letter that takes a dictionary named names as a parameter.

names should be a dictionary where the key is a last name and the value is a list of first names.

For example, the dictionary might look like this:

names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}

The function should return a new dictionary where each key is the first letter of a last name, 

and the value is the number of people whose last name begins with that letter.

So in example above, the function would return:

{"S" : 4, "L": 3}  
"""

# Answer


def count_first_letter(names):
    # Initialize an empty dictionary to store the counts
    first_letter_counts = {}

    # Iterate over each key (name) in the input dictionary
    for key in names:
        # Get the first letter from the key
        first_letter = key[0]

        # If the first letter is not already a key in the dictionary, add it with a count of 0
        if first_letter not in first_letter_counts:
            first_letter_counts[first_letter] = 0

        # Add the count of names associated with the current name to the count for this first letter
        first_letter_counts[first_letter] += len(names[key])

    # Return the dictionary of counts
    return first_letter_counts


# Checks the result
print(
    count_first_letter(
        {
            "Stark": ["Ned", "Robb", "Sansa"],
            "Snow": ["Jon"],
            "Lannister": ["Jaime", "Cersei", "Tywin"],
        }
    )
)
# should print {"S": 4, "L": 3}
print(
    count_first_letter(
        {
            "Stark": ["Ned", "Robb", "Sansa"],
            "Snow": ["Jon"],
            "Sannister": ["Jaime", "Cersei", "Tywin"],
        }
    )
)
# should print {"S": 7}
