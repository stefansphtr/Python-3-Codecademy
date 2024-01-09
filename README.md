# <img src="./src/img/GIF Codecademy.gif" width=50> My Python3 Learning Journey <img src="./src/img/GIF Codecademy.gif" width=50>

<p align="center">
  <a href="#">
    <img src="https://badges.pufler.dev/visits/stefansphtr/Python-3-Codecademy" alt="Visits Badge">
    <img src="https://badges.pufler.dev/updated/stefansphtr/Python-3-Codecademy" alt="Updated Badge">
    <img src="https://badges.pufler.dev/created/stefansphtr/Python-3-Codecademy" alt="Created Badge">
    <img src="https://img.shields.io/github/contributors/stefansphtr/Python-3-Codecademy" alt="Contributors Badge">
    <img src="https://img.shields.io/github/last-commit/stefansphtr/Python-3-Codecademy" alt="Last Commit Badge">
    <img src="https://img.shields.io/github/commit-activity/m/stefansphtr/Python-3-Codecademy" alt="Commit Activity Badge">
    <img src="https://img.shields.io/github/repo-size/stefansphtr/Python-3-Codecademy" alt="Repo Size Badge">
  </a>
</p>

## 📃 Description
This repository documents my journey learning Python3 from [Codecademy](https://www.codecademy.com/) and other resources. I've organized my work into three directories: [code-challenges](code-challenges/), [exercises](exercises/), and [mini-project](mini-project/). In the [code-challenges](code-challenges/) directory, I've worked on various Python concepts like classes, control flow, dictionaries, functions, lists, loops, and strings. In the [exercises](exercises/) directory, I've practiced more Python concepts. In the [mini-project](mini-project/) directory, I've applied what I've learned in small projects. I've also included a [resources](resources/) directory with links to helpful resources. I hope you find this repository useful. Thank you for visiting!

## 📚 Table of Contents
- [ My Python3 Learning Journey ](#-my-python3-learning-journey-)
  - [📃 Description](#-description)
  - [📚 Table of Contents](#-table-of-contents)
  - [💡 Code Challenges](#-code-challenges)
  - [🏋️‍♀️ Exercises](#️️-exercises)
  - [🎯 Mini Projects](#-mini-projects)
  - [🤝 Contributing](#-contributing)

## 💡 Code Challenges
In the [code-challenges](code-challenges/) directory, I've worked on various Python concepts like classes, control flow, dictionaries, functions, lists, loops, and strings. For example, in [list.py](code-challenges/list.py), I implemented a function called `double_index` that takes two parameters: a list and an index. The function should return a new list where all elements are the same as in the original list except for the element at the given index. The element at the given index should be double the value of the element at the given index of the original list. If the index is not a valid index, the function should return the original list. For example, `double_index([1, 2, 3, 4], 2)` should return `[1, 2, 6, 4]` because the element at index 2 has been doubled. After writing the function, I tested it with different inputs to make sure it works as expected.

## 🏋️‍♀️ Exercises
In the [exercises](exercises/) directory, I've practiced more Python concepts. For instance, in [strings.py](exercises/strings.py), I worked with string manipulations such as `len()`, `lower()`, `upper()`, `str()`, `print()`, `format()`, `split()`, `join()`, `strip()`, `replace()`, `find()`, `index()`, `isalpha()`, `isdigit()`, `islower()`, `isupper()`, `startswith()`, and `endswith()`. For example, I wrote a function called `username_generator` that takes two inputs, `first_name` and `last_name`, and returns a username. The username is made up of the first three letters of `first_name` and the first four letters of `last_name`. If `first_name` is less than three letters or `last_name` is less than four letters, the function should return an empty string. For example, `username_generator("Abe", "Simpson")` should return `"AbeSimp"`.

## 🎯 Mini Projects
In the [mini-project](mini-project/) directory, I've applied what I've learned in small projects. For example, in [hacking-the-fender.py](mini-project/hacking-the-fender.py), I simulated a hacking scenario where I had to retrieve a list of compromised usernames and passwords from a text file. I wrote a function called `read_file` that takes one parameter, `filename`, and returns a list of lines from that file. I also wrote a function called `decrypt` that takes one parameter, `message`, and decrypts it using the Caesar Cipher. The function should return the decrypted message. I then wrote a function called `hack` that takes one parameter, `message`, and returns a decrypted version of that message by calling `decrypt` for each line in the file. Finally, I wrote a function called `user_passwords` that takes one parameter, `hack_list`, and returns a new list with just the username and password for each line in the hack list. The username should be the first 10 characters of the line and the password should be the characters between the 11th and 21st character of the line. For example, `user_passwords(hack("passwords.txt"))` should return `["kenneth", "password123"]`.

## 🤝 Contributing
I welcome any suggestions or feedback. Feel free to fork this repository and submit a pull request. Thank you for your support!