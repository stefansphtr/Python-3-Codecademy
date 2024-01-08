def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = (hotel_rate * trip_time) - 10
  print(f"The list of expenses: \n for car rent: ${car_rental_total} \n for hotel: ${hotel_total} \n for the ticket plane: ${plane_ticket_price}")
  print(f"The sum of expenses will be: ${car_rental_total + hotel_total + plane_ticket_price}")

calculate_expenses(200, 100, 100, 5)

def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print(f"First, we will stop in {first_destination}, then {second_destination}, and lastly {final_destination}")

# Positional arguments
trip_planner("France", "Germany", "Denmark")

trip_planner("Denmark", "France", "Germany")

# Keyword arguments 
trip_planner(first_destination="Iceland", second_destination="India", final_destination="Germany")

# Default arguments
trip_planner("Brooklyn", "Queens")

# Diference between return and print in function

# Example 1: Basic function

def print_value(value):
  print(value)

def return_value(value):
  return value

print_value("Hello from print_value function")  # This will print: Hello from print_value function
result = return_value("Hello from return_value function")
print(result)  # This will print: Hello from return_value function

# Example 2: Function in a Calculation

def print_value(value):
  print(value)

def return_value(value):
  return value

# Trying to use the function in a calculation
result = print_value(5) + 10  # This will raise an error
result = return_value(5) + 10  # This will work and result will be 15

# Example 3: Function in a Conditional Statement
def print_value(value):
  print(value)

def return_value(value):
  return value

# Trying to use the function in a conditional statement
if print_value("Hello"):  # This will not execute the if block
  print("This won't print")

if return_value("Hello"):  # This will execute the if block
  print("This will print")
  
# Explanation: In this example, `if print_value("Hello"):` doesn't execute the if block because `print_value("Hello")`
# doesn't return a value that can be evaluated as True. On the other hand, 
# `if return_value("Hello"):` executes the if block because `return_value("Hello")` returns "Hello", 
# which is evaluated as True in the conditional statement.