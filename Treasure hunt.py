#Setting up the map
import random
row1 = ["😃", "😃", "😃"]
row2 = ["😃", "😃", "😃"]
row3 = ["😃", "😃", "😃"]
treasure_map = [row1, row2, row3]
print("Welcome to the treasure island! Your map suggests nine possible locations of your prize. Waste no time, go and find it!The map key is:\n ABC\n DEF\n GHI\n\n\n")
treasure_areas = "ABCDEFGHI"
treasure_location = random.choice(treasure_areas)


#Map's special effects function
def effects(treasure_map, x, y):
	if y == False:
		change = "X"
	else:
		change = "💰"
	if x == "A":
		treasure_map[0][0] = change
	elif x == "B":
		treasure_map[0][1] = change
	elif x == "C":
		treasure_map[0][2] = change
	elif x == "D":
		treasure_map[1][0] = change
	elif x == "E":
		treasure_map[1][1] = change
	elif x == "F":
		treasure_map[1][2] = change
	elif x == "G":
		treasure_map[2][0] = change
	elif x == "H":
		treasure_map[2][1] = change
	elif x == "I":
		treasure_map[2][2] = change
	return treasure_map


#Guessing loop
available_options = ["A","B","C","D","E","F","G","H","I"]
guesses = 1
victory = False
while not victory:
	print(f"Your eyes are gazing at the map, you feel lucky today. Choose between {available_options}\n{row1}\n{row2}\n{row3}\n\n")
	attempt = input().upper()
	map_change = False
	if attempt == treasure_location:
		map_change = True
		effects(treasure_map, attempt, map_change)
		print(f"Success, you found the treasure! It took you {guesses} attempts.\n{row1}\n{row2}\n{row3}")
		victory = True
	else:
		effects(treasure_map, attempt, map_change)
		print("Luck was not on your side, try again.\n\n")
		guesses += 1
		available_options.remove(attempt)