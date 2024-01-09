letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
points = [
    1,
    3,
    3,
    2,
    1,
    4,
    2,
    4,
    1,
    8,
    5,
    1,
    3,
    4,
    1,
    3,
    10,
    1,
    1,
    1,
    1,
    4,
    4,
    8,
    4,
    10,
]

"""Build your Point Dictionary"""

# Task 1
letter_to_points = {letter: point for letter, point in zip(letters, points)}
print(letter_to_points)

# Task 2
print("\n The letter to points after add element \n")
letter_to_points[" "] = 0
print(letter_to_points)

"""Score a Word"""


# Task 3 - 6
# Given the list of word, I want you to sum the score of each letter inside the word
def score_word(word):
    point_total = 0
    for letters in word:
        point_total += letter_to_points.get(letters, 0)
    return point_total


# Test the function score_word in a list
print("\n Score word of Stefan's name: \n")
print(score_word(["S", "T", "E", "F", "A", "N"]))

# Task 7 - 8: Test the function score_word in a string
brownie_points = score_word("BROWNIE")

print("\n Score word of BROWNIE: \n")
print(brownie_points)

"""Score a Game"""

# Task 9
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"],
}

# Task 10
player_to_points = {}

# Task 11 - 13
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

# Task 14
print("\n Score word of player wordNerd: \n")
print(player_to_points["player1"])
print(player_to_points["Lexi Con"])
print(player_to_points["Prof Reader"])
print(player_to_points["wordNerd"])

# Task 15

# Create a function play_world() that would take in a player and word, and add that word to the list of words they've played


def play_word(player, word):
    if player in player_to_words.keys():
        player_to_words[player].append(word)
    else:
        player_to_words[player] = [word]


print("\n This is the list of words from player1 after add the word DRAGUNOV: \n")

play_word("player1", "DRAGUNOV")
print(player_to_words["player1"])

# Turn the nested loops into a function update_point_totals() that can be call anytime a word is played

print("\n This is the dictionary of player_to_words: \n")
print(player_to_words)


def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points


update_point_totals()

print("\n This is the updated scores of player1: \n")
print(player_to_points)


# Make the letter_to_points dictionary able to handle lowercase inputs as well

letter_to_points = {letter.upper(): point for letter, point in zip(letters, points)}
letter_to_points.update(
    {letter.lower(): point for letter, point in zip(letters, points)}
)
letter_to_points[" "] = 0

# Test to soring the lowercase letter:
print("\n Score word of Stefan's name in uppercase: \n")
print(score_word("STEFAN"))

print("\n Score word of Stefan's name in lowercase: \n")
print(score_word("stefan"))

print("\n Score word of Stefan's name in titlecase: \n")
print(score_word("Stefan"))
