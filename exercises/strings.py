# Exercise 1

def get_length(str):
  count = 0
  for word in str:
    count += 1
  return print(count)

first_name = "Azarya Yehezkiel"
get_length(first_name)

# Exercise 2

def letter_check(word, letter):
    if letter.lower() in word.lower():
        return True
    else:
        return False
    
print(letter_check("Building", "b"))

# Exercise 3

def contains(big_string, little_string):
  if little_string.lower() in big_string.lower():
    return True
  else:
    return False
contains("watermelon", "melon")

# Exercise 4

def common_letters(string_one, string_two):
  # Convert both strings to lower case to make the comparison case-insensitive
  string_one = string_one.lower()
  string_two = string_two.lower()

  # Initialize an empty list to hold the common letters
  common = []

  # Iterate over each letter in the first string
  for letter in string_one:
    # If the letter is in the second string and not already in the common list, add it
    if letter in string_two and letter not in common:
      common.append(letter)

  return common

  print(common_letter("bAnAna", "cReam"))
  
# Exercise 5

# Solution 1
# def password_generator(user_name):
#   password = user_name[-1] + user_name[:-1]
#   return password

# Solution 2
def password_generator(user_name):
  # Initialize an empty string to hold the upcoming password
  password = ""

  # Iterate over the indices of user_name
  for index in range(len(user_name)):
    # Add the letter at the previous index of user_name to password
    password += user_name[index - 1]
    
def print_some_characters(word):
  for i in range(len(word)):
    if i % 2 == 0:
      print(word[i])

print_some_characters("watermelon")