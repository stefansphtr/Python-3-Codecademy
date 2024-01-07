hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

""" Prices and Cuts """

# Task 1
total_price = 0

# Task 2
for price in prices:
  total_price += price

print(total_price)

# Task 3
average_price = round(total_price/len(prices), 2)
print(average_price)

# Task 4
print(f"Average Haircut Price: ${average_price}")
# print("Average Haricut Price: ", average_price)

print("\n")

# Task 5
print(f"This is the list of prices: \n {prices}")

print("\n")

new_prices = [price - 5 for price in prices]

# Task 6
print(f"This is the list of new prices: \n {new_prices}")

print("\n")

""" Revenue """

# Task 7
total_revenue = 0

# Task 8
for i in range(len(hairstyles)):
# Task 9
  total_revenue += (prices[i] * last_week[i])

# Task 10
print(f" Total Revenue: ${total_revenue}")

# Task 11
average_daiy_revenue = int(total_revenue / 7)

print("\n")

print(f"Average Daily Revenue: ${average_daiy_revenue}")

# Task 12
print("\n")

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print("The list of haircuts that are under 30: {0}".format(cuts_under_30))

print("\n")

print(f"The list of haircuts that are under 30: {cuts_under_30}")

