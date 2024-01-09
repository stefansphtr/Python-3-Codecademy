"""Making the Menus"""

# Import necessary modules
from datetime import datetime, time


# Task 1 -2
class Menu:
    """A class representing a restaurant menu."""

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = datetime.strptime(start_time, "%H:%M").time()
        self.end_time = datetime.strptime(end_time, "%H:%M").time()

    # Task 7
    def __repr__(self):
        return f"\n The {self.name} menu will available from {self.start_time} - {self.end_time}. Thank you! \n"

    # Task 9
    def calculate_bill(self, purchased_items):
        """Calculate the total bill for the purchased items."""
        return sum(self.items[item] for item in purchased_items if item in self.items)


# Task 12 - 13
class Franchise:
    """A class representing a restaurant franchise."""

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    # Task 15
    def __repr__(self):
        return f"These are the addresses of our restaurants: {self.address}"

    # Task 16
    def available_menus(self, time):
        """Return the available menus at given time."""
        time = datetime.strptime(time, "%H:%M").time()
        return [
            menu
            for menu in self.menus
            if time >= menu.start_time and time <= menu.end_time
        ]


# Task 19 - 20
class Business:
    """A class representing a busniess with multiple franchises."""

    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# Task 3
brunch_items = {
    "pancakes": 7.50,
    "waffles": 9.00,
    "burger": 11.00,
    "home fries": 4.50,
    "coffee": 1.50,
    "espresso": 3.00,
    "tea": 1.00,
    "mimosa": 10.50,
    "orange juice": 3.50,
}


# Task 4
early_bird_items = {
    "salumeria plate": 8.00,
    "salad and breadsticks (serves 2, no refills)": 14.00,
    "pizza with quattro formaggi": 9.00,
    "duck ragu": 17.50,
    "mushroom ravioli (vegan)": 13.50,
    "coffee": 1.50,
    "espresso": 3.00,
}


# Task 5
dinner_items = {
    "crostini with eggplant caponata": 13.00,
    "caesar salad": 16.00,
    "pizza with quattro formaggi": 11.00,
    "duck ragu": 19.50,
    "mushroom ravioli (vegan)": 13.50,
    "coffee": 2.00,
    "espresso": 3.00,
}


# Task 6
kids_items = {
    "chicken nuggets": 6.50,
    "fusilli with wild mushrooms": 12.00,
    "apple juice": 3.00,
}

brunch_menu = Menu("brunch", brunch_items, "11:00", "16:00")
early_bird_menu = Menu("early bird", early_bird_items, "15:00", "18:00")
dinner_menu = Menu("dinner", dinner_items, "17:00", "23:00")
kids_menu = Menu("kids", kids_items, "11:00", "21:00")

# Task 8
print(kids_menu, dinner_menu, early_bird_menu, brunch_menu)

# Task 10
customer1_bill = brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"])
print(f"\n Total bill for the first customer: {customer1_bill}\n")

# Task 11
customer2_bill = early_bird_menu.calculate_bill(
    ["salumeria plate", "vegan mushroom ravioli"]
)
print(f"\n Total bill for the second customer: {customer2_bill}\n")

"""Creating the Franchises"""

# Task 14

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

# Check the address of the flagship store
print(flagship_store)

# Add the new line
print("\n")

# Check the address of the new installment store
print(new_installment)

# Add the new line
print("\n")

# Test out the available menu
available_menu_at_8pm = flagship_store.available_menus("20:00")
available_menu_at_12pm = flagship_store.available_menus("12:00")
available_menu_at_5pm = flagship_store.available_menus("17:00")

print(f"The available menus at 8pm are: {available_menu_at_8pm}")

# Add the new line
print("\n")

print(f"The available menus at 12pm are: {available_menu_at_12pm}")

# Add the new line
print("\n")

print(f"The available menus at 5pm are: {available_menu_at_5pm}")

# Add the new line
print("\n")

"""Creating Businesses"""

# Task 21
first_business = Business(
    "Basta Fazoolin' with my Heart", [flagship_store, new_installment]
)

# Print the first menu in flagship store wich is one of the business basta's franchises
print(first_business.franchises[0].menus[0])

# Task 22
arepas_items = {
    "arepa pabellon": 7.00,
    "pernil arepa": 8.50,
    "guayanes arepa": 8.00,
    "jamon arepa": 7.50,
}

arepas_menu = Menu("Take a' Arepa", arepas_items, "10:00", "20:00")

# Task 23
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Task 24 - 25
second_business = Business("Take a' Arepa", [arepas_place])

# Test out the franchise address
print(second_business.franchises[0].menus[0])
