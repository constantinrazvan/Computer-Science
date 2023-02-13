letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#combining the two lists
letters_to_points = {}
for key, value in zip(letters, points):
  letters_to_points[key] = value
#print(letters_to_points)

#adding a blank tile to our dictionary
letters_to_points[" "] = 0

#function that will take in a word an return how many points that word in worth.
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letters_to_points[letter]
  return point_total

#Let’s test this function! 
brownie_points = score_word("BROWNIE")
print(brownie_points)

#Create a dictionary called player_to_words that maps players to a list of the words they have played.
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words :
    player_points += score_word(word)
    player_to_points[player] = player_points
      
print(player_to_points)


#play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played

def play_word(player, word):
  if player in player_to_words:
    player_to_words[player].append(word)
  else:
    print("This player doesn't exist!")
    
play_word("player1", "RACKET")
print(player_to_words)