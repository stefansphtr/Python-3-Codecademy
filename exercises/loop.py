def main():
    # Print a message 10 times
    for iteration in range(10):
        print(f"This is the {iteration + 1}th time I'm printing this.")

    print("\n")

    # List of dog breeds available for adoption
    dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
    dog_breed_I_want = "dalmatian"

    # Check if the desired dog breed is available
    for dog_breed in dog_breeds_available_for_adoption:
        print(dog_breed)
        if dog_breed == dog_breed_I_want:
            print("They have the dog I want!")
            break

if __name__ == "__main__":
    main()

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
    if i <= 0:
        continue
    print(i)
    
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  for number in location:
    scoops_sold += number

print(scoops_sold)
        
grades = [90, 88, 62, 76, 74, 89, 48, 57]
# Sort the values in decending order
grades.sort(reverse=True)
# Add 10 pom for each item in grades variable and insert into scaled_grades variable with list comprehensive
scaled_grades = [grade + 10 for grade in grades]
# Print the result
print(scaled_grades)

numbers = [2, -1, 79, 33, -45]

# I wanted to double only negative numbers
doubled_numbers = [num * 2 for num in numbers if num < 0]
print(doubled_numbers)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

no_if = [num * 2 for num in numbers]
if_only = [num * 2 for num in numbers if num < 0]
if_else = [num * 2 if num  < 0 else num * 3 for num in numbers]

single_digits = list(range(10))
print(single_digits)

squares = []

for digit in single_digits:
    squares.append(digit**2)
    print(digit)

print(squares)

cubes = [digit ** 3 for digit in single_digits]

print(cubes)


list_decrease = [i-1 for i in range(5)]
print(list_decrease)
