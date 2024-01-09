# Exercise 1

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

print("This is the key,value that we wanted to take: \n")

print(list(zip(drinks, caffeine)))

print(
    "\n Note that in this list of tupple each of the element in drinks and caffeine already in a pair but inside a tupple \n"
)

zipped_drinks = zip(drinks, caffeine)

print("This is the key, value pair after using dictionaries comprehension: \n")

drinks_to_caffeine = {key: value for key, value in zipped_drinks}

print(drinks_to_caffeine)

print("\n")

list_of_drinks = list(drinks_to_caffeine)
print(list_of_drinks)


# Exercise 2

songs = [
    "Like a Rolling Stone",
    "Satisfaction",
    "Imagine",
    "What's Going On",
    "Respect",
    "Good Vibrations",
]
playcounts = [78, 29, 44, 21, 89, 5]

zipped_play_song = zip(songs, playcounts)

plays = {song: playcount for song, playcount in zipped_play_song}

print(plays)

plays["Purple Haze"] = 1

print("\n Add Purple Haze song with song count 1: \n")
print(plays)

plays["Respect"] = 94

print("\n Add 5 song count for Respect: \n")
print(plays)

library = {"The Best Songs": plays, "Sunday Feelings": {}}


print("\n Create a new dictionary called library: \n")
print(library)

library["Sunday Feelings"] = {"Seafret": 21}
print("\n Add song and count to Sunday Feelings: \n")
print(library)

# Exercsie 3

user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384,
}
num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18,
}

users = user_ids.keys()
print(users)

lessons = num_exercises.keys()
lessons_list = list(num_exercises)
num_exercises["modules"] = 21

print(lessons)
print("\n")
print(lessons_list)


# Exercise 4

num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18,
}

total_exercises = 0

for num in num_exercises.values():
    total_exercises += num

print(total_exercises)

# Alternative solution with only one line
total_exercises = sum(num_exercises.values())

print(total_exercises)

# Exercise 5

pct_women_in_occupation = {
    "CEO": 28,
    "Engineering Manager": 9,
    "Pharmacist": 58,
    "Physician": 40,
    "Lawyer": 37,
    "Aerospace Engineer": 9,
}

for occupation, percentage in pct_women_in_occupation.items():
    print(f"Women make up {percentage} percent of {occupation}s.")

# Exercise 6

tarot = {
    1: "The Magician",
    2: "The High Priestess",
    3: "The Empress",
    4: "The Emperor",
    5: "The Hierophant",
    6: "The Lovers",
    7: "The Chariot",
    8: "Strength",
    9: "The Hermit",
    10: "Wheel of Fortune",
    11: "Justice",
    12: "The Hanged Man",
    13: "Death",
    14: "Temperance",
    15: "The Devil",
    16: "The Tower",
    17: "The Star",
    18: "The Moon",
    19: "The Sun",
    20: "Judgement",
    21: "The World",
    22: "The Fool",
}

spread = {}

spread["past"] = tarot[13]
tarot.pop(13)

print(f"The list of spread: {spread}")
print(f"\n Deck of Tarot after removing the card number 13: {tarot} \n")

spread["present"] = tarot.get(22, "No such card number foung, draw another card")
tarot.pop(22)
print(f" \n The deck of Tarot after removing the card number 22: {tarot}")

spread["future"] = tarot.get(10, "No such card number foung, draw another card")
tarot.pop(10)
print(f" \n The deck of Tarot after removing the card number 10: {tarot}")

print("\n The deck of card that already taken from tarot: \n")

for number, card in spread.items():
    print(f"Your {number} is the {card} card.")
