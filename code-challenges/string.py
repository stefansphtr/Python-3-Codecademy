# Basic Strings

# 1. Count Letters

"""Write a function called unique_english_letters that takes the string word as a parameter. 

The function should return the total number of unique letters in the string. 

Uppercase and lowercase letters should be counted as different letters.

We've given you a list of every uppercase and lower case letter in the English alphabet. 

It will be helpful to include that list in your function."""

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


# Answer
def unique_english_letters(word):
    count = 0
    for letter in letters:
        if letter in word:
            count += 1
    return count


# Checks the result
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# 2. Count X

"""Write a function named count_char_x that takes a string named word and a single character named x as parameters. 

The function should return the number of times x appears in word."""


# Answer
def count_char_x(word, x):
    count = 0
    for letter in word:
        if x == letter:
            count += 1
    return count


# Checks the result
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# 3. Count Multi X

"""Write a function named count_multi_char_x that takes a string named word and a string named x.

This function should do the same thing as the count_char_x function you just wrote - it should 

return the number of times x appears in word. However, this time,

make sure your function works when x is multiple characters long.

For example, count_multi_char_x("Mississippi", "iss") should return 2"""


# Answer
def count_multi_char_x(word, x):
    split_word = word.split(x)
    count = len(split_word) - 1
    return count


# Checks the result
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# 4. Substring Between

"""Write a function named substring_between_letters that takes a string named word, a single character named start, 

and another character named end. This function should return the substring between the first occurrence of start and end in word. 

If start or end are not in word, the function should return word.

For example, substring_between_letters("apple", "p", "e") should return "pl"."""


# Answer
def substring_between_letters(word, start, end):
    """Return the substring between the first occurrence of start and end in word.

    Args:
        word (str): The string to search within.
        start (str): The character marking the start of the substring.
        end (str): The character marking the end of the substring.

    Returns:
        str: The substring between start and end. If start or end are not in word, return the original word.
    """
    if start in word and end in word:
        return word[word.find(start) + 1 : word.find(end)]
    else:
        return word


# Cheks the result
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

# 5. X Length

"""Create a function called x_length_words that takes a string named sentence and an integer

named x as parameters. This function should return True if every word in sentence

has a length greater than or equal to x."""

# Answer

# First Solution
# def x_length_words(sentence, x):
#   for word in sentence.split(" "):
#     if len(word) >= x:
#       return True
#     else:
#       return False


# Second Solution
def x_length_words(sentence, x):
    words = sentence.split(" ")
    for word in words:
        if len(word) < x:
            return False
        else:
            return True


# Checks the result
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

# Advanced Strings

# 1. Check Name

"""Write a function called check_for_name that takes two strings as parameters named 

sentence and name. The function should return True if name appears in sentence in 

all lowercase letters, all uppercase letters, or with any mix of uppercase and 

lowercase letters. The function should return False otherwise.

For example, the following three calls should all return True:

check_for_name("My name is Jamie", "Jamie")
check_for_name("My name is jamie", "Jamie")
check_for_name("My name is JAMIE", "Jamie")"""

# Answer

# Solution 1
# def check_for_name(sentence, name):
#   if name.lower() in sentence.lower():
#     return True
#   else:
#     return False


# Solution 2
def check_for_name(sentence, name):
    return name.lower() in sentence.lower()


# Check the result
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

# 2. Every other Letter

"""Create a function named every_other_letter that takes a string 

named word as a parameter. The function should return a string containing 

every other letter in word."""

# Answer

# First Solution
# def every_other_letter(word):
#   other_letter = ""
#   for i in range(0,len(word),2):
#     other_letter += word[i]
#   return other_letter


# Second Solution
def every_other_letter(word):
    return word[::2]


# Checks the result
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print

# 3. Reverse

"""Write a function named reverse_string that has a string named word as a parameter. 

The function should return word in reverse."""

# Answer


# First Solution
def reverse_string(word):
    reverse_word = ""
    for i in range(len(word) - 1, -1, -1):
        reverse_word += word[i]
    return reverse_word


# Second Solution
def reverse_string(word):
    reverse_word = ""
    for i in range(len(word)):
        reverse_word += word[-i - 1]
    return reverse_word


# Checks the reuslt
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# 4. Make Spoonerism

"""Write a function called make_spoonerism that takes two strings as parameters named 

word1 and word2. Finding the first syllable of a word is a difficult task, so for our function,

we're going to switch the first letters of each word. Return the two new words as a single string

separated by a space."""

# Answer

# Solution 1
# def make_spoonerism(word1, word2):
#   return word2[0] + word1[1:] + " " + word1[0] + word2[1:]


# Solution 2
def make_spoonerism(word1, word2):
    first_word = word1.replace(word1[0], word2[0])
    second_word = word2.replace(word2[0], word1[0])
    result = f"{first_word} {second_word}"
    return result


# Check the result
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# 5. Add Exclamation

"""Create a function named add_exclamation that has one parameter named word.

This function should add exclamation points to the end of word until word is 20 characters long.

If word is already at least 20 characters long, just return word."""


# Answer
def add_exclamation(word):
    while len(word) < 20:
        word += "!"
    else:
        return word


# Checks the result
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
