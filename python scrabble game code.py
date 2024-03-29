# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 23:07:38 2024

@author: aoalj
"""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_lower = [letter.lower() for letter in letters]

# Create a dictionary to map both uppercase and lowercase letters to points
letter_to_points = {upper: point for upper, lower, point in zip(letters, letters_lower, points) for upper, lower in [(upper, lower), (lower, lower)]}

# Add an entry for an empty string
letter_to_points[""] = 0  
print(letter_to_points)
# Function to calculate points for a word
def score_word(word):
    point_total = 0
    for letter in word:  
        point_total += letter_to_points.get(letter, 0)  # Use get method to handle letters not in the dictionary
    return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], 
"wordNerd": ["EARTH", "EYES", "MACHINE"], 
"Lexi Con": ["ERASER", "BELLY", "HUSKY"],
"Prof Reader": ["ZAP", "COMA", "PERIOD"]}


def play_word(player, word):
  player_to_words[player].append(word)
play_word("player1", "GO")
print(player_to_words)
player_to_points = {}

for player in player_to_words:
  player_points = 0
  for word in player_to_words[player]:
    player_points += score_word(word)
  player_to_points.update({player:player_points})
print(player_to_points)