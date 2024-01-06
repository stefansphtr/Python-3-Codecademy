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

# Exercise 6

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

# Split the authors name into a list of authors
authors_list = authors.split(",")
print(authors_list)

print("\n")

# Iterate over the list of authors
def get_last_words(list):
  # Get the last name
  last_names = []
  for author in list:
    # Split the author's name into a list of names 
    author_names = author.split(" ")
    # Get the last name from the list of names
    last_name = author_names[-1]
    # Append the last name into the list of last names
    last_names.append(last_name)
  return print(last_names)

# Add the last names of the poets in the new variable
author_last_names = get_last_words(authors_list)
print(author_last_names)

# Exericse 7

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = "\n".join(winter_trees_lines)
print(winter_trees_full)

print("\n")

winter_trees_one_line = " ".join(winter_trees_lines)
print(winter_trees_one_line)

# Exercise 8

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

# Solution with function

def clean_line(lines):
  new_line = []
  for line in lines:
    new_line.append(line.strip())
  cleaned_line = "\n".join(new_line)
  return print(cleaned_line)

clean_line(love_maybe_lines)

# Solution without function

# love_maybe_lines_stripped = []

# for line in love_maybe_lines:
#   love_maybe_lines_stripped.append(line.strip())

# print(love_maybe_lines_stripped)

# print("\n")

# love_maybe_full = "\n".join(love_maybe_lines_stripped)
# print(love_maybe_full)

# Exercise 9 

string = 'abababa long section without substring ababab'
target ='abab'

for i in range(len(string)):
   print(i, i+len(target), string[i:i+len(target)])

# Function to check every possible position target in string
def find_all(string, target):
  indices = []
  # Open the acces to each element in string variable
  for i in range(len(string)):
    # Check if the element is the same as desired target
    if string[i:i+len(target)] == target:
      indices.append(i)
  return print(indices)

find_all('abababa long section without substring ababab', 'abab')

# Exercise 10

# Solution 1

# def poem_title_card(title, poet):
#   poem_card = "The poem \"{}\" is written by {}".format(title, poet)
#   return print(poem_card)

# poem_title_card(title, poet)

# Solution 2

def poem_title_card(title, poet):
  return "The poem \"{}\" is written by {}.".format(title, poet)

print(poem_title_card("I Hear America Singing", "Walt Whitman"))

# Exercise 11

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)

# Final Exercise

# A string of poems, poets, and dates separated by colons and commas
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# Split the string into a list of strings at each comma
highlighted_poems_list = highlighted_poems.split(",")

# Print the original string
print(highlighted_poems)

print("\n")

# Print the list of strings
print(highlighted_poems_list)

# Create an empty list to hold the cleaned strings
highlighted_poems_stripped = []

# Iterate over the list of strings and remove leading and trailing whitespace from each, then add it to the cleaned list
for word in highlighted_poems_list:
  highlighted_poems_stripped.append(word.strip())

print("\n")

# Print the cleaned list
print(highlighted_poems_stripped)

# Create an empty list to hold the details of each poem
highlighted_poems_details = []

# Iterate over the cleaned list and split each string into a list at each colon, then add it to the details list
for word in highlighted_poems_stripped:
  highlighted_poems_details.append(word.split(":"))

print("\n")

# Print the details list
print(highlighted_poems_details)

# Create empty lists to hold the titles, poets, and dates
titles = []
poets = []
dates = []

# Iterate over the details list and add the title, poet, and date from each to the appropriate list
for list in highlighted_poems_details:
  titles.append(list[0])
  poets.append(list[1])
  dates.append(list[2])

print("\n FULL LIST \n")
# Print the details list
print(highlighted_poems_details)

print("\n TITLES \n")
# Print the titles list
print(titles)
print("\n POETS \n")
# Print the poets list
print(poets)
print("\n DATES \n")
# Print the dates list
print(dates)

print("\n FINAL RESULT: \n")

# Iterate over the indices of the details list and print a formatted string with the title, poet, and date at each index
for i in range(len(highlighted_poems_details)):
  print("The poem {title} was published by {poet} in {date}".format(title=titles[i] ,poet=poets[i] ,date=dates[i]))

# Alternative Iterator using enumerate
# for i, title in enumerate(titles):
#   print("The poem {title} was published by {poet} in {date}".format(title=title ,poet=poets[i] ,date=dates[i]))