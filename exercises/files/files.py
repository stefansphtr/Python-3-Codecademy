# Exercise 1

with open("welcome.txt") as text_file:
    text_data = text_file.read()
print(text_data)

# Exercise 2

with open("how_many_lines.txt") as lines_doc:
    for line in lines_doc.readlines():
        print(line)

# Exercise 3

with open("just_the_first.txt") as first_line_doc:
    first_line = first_line_doc.readline()
    print(first_line)

# Exercise 4

# Read the cools_dogs.txt
with open("cool_dogs.txt") as cool_dogs_file:
    file_dog = cool_dogs_file.read()
    print(file_dog)

# Open the cools_dogs.txt in append mode and add Air Buddy to the text
with open("cool_dogs.txt", "a") as cool_dogs_file:
    cool_dogs_file.write("Air Buddy \n")

# Exercise 5

import csv
from datetime import datetime

list_of_cool_birthday = []

with open("cool_csv.csv") as cool_csv_file:
    cool_csv_dict = csv.DictReader(cool_csv_file)
    for row in cool_csv_dict:
        list_of_cool_birthday.append(row["Cool Birthday"])

print(list_of_cool_birthday)

# Convert string to datetime
for datestr in list_of_cool_birthday:
    datetime.strptime(datestr, "%d-%m-%y")

print(list_of_cool_birthday)

# Exercise 6

import csv

isbn_list = []

with open("books.csv") as books_csv:
    books_reader = csv.DictReader(books_csv, delimiter="@")
    for row in books_reader:
        isbn_list.append(row["ISBN"])

print(isbn_list)

# Exercise 7

# Import the csv module, which provides functionality to both read from and write to CSV files
import csv

# Define a list of dictionaries, where each dictionary represents a log entry
access_log = [
    {"time": "08:39:37", "limit": 844404, "address": "1.227.124.181"},
    {"time": "13:13:35", "limit": 543871, "address": "198.51.139.193"},
    {"time": "19:40:45", "limit": 3021, "address": "172.1.254.208"},
    {"time": "18:57:16", "limit": 67031769, "address": "172.58.247.219"},
    {"time": "21:17:13", "limit": 9083, "address": "124.144.20.113"},
    {"time": "23:34:17", "limit": 65913, "address": "203.236.149.220"},
    {"time": "13:58:05", "limit": 1541474, "address": "192.52.206.76"},
    {"time": "10:52:00", "limit": 11465607, "address": "104.47.149.93"},
    {"time": "14:56:12", "limit": 109, "address": "192.31.185.7"},
    {"time": "18:56:35", "limit": 6207, "address": "2.228.164.197"},
]

# Define the field names for the CSV file
fields = ["time", "address", "limit"]

# Open a CSV file in write mode ('w') as logger_csv
with open("logger.csv", "w") as logger_csv:
    # Create a csv.DictWriter object, which maps dictionaries onto output rows.
    # The fieldnames argument is a sequence of keys that identify the order in which values in the dictionary are written to the CSV file.
    log_writer = csv.DictWriter(logger_csv, fieldnames=fields)

    # Write the header to the CSV file
    log_writer.writeheader()
    # Iterate over each dictionary in the access_log list
    for item in access_log:
        # Write each dictionary to the CSV file as a row
        log_writer.writerow(item)

# Open the CSV file in the read mode
with open("logger.csv", "r") as csv_file:
    # Create a csv reader
    csv_reader = csv_file.read()
    print(csv_reader)
