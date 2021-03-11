#Setting up the graphics and game
import random
print("Welcome to the 'Rock, Papper, Scissors' game.")
rock = '''
      _______
___'    _____)
         (______)
         (______)
         (_____)
---,___(___)
'''
papper = '''
      _______
___'     _____)_
           ________)_
           __________)
           __________)
----,_________)
'''
scissors = '''
     ______
__'      ____)___
          _________)
          _________)
          (____)
---,___(___)
'''
computer_wins = 0
person_wins = 0
computer_choices = ["rock", "papper", "scissors"]


#Game function
def game (x,y,z):
	if x == y:
		z = "draw"
	elif (x == "rock") and (y == "papper"):
		z = "it"
	elif (x == "rock") and (y == "scissors"):
		z = "you"
	elif (x == "papper") and (y == "rock"):
		z = "you"
	elif (x == "papper") and (y == "scissors"):
		z = "it"
	elif (x == "scissors") and (y == "rock"):
		z = "it"
	elif (x == "scissors") and (y == "papper"):
		z = "you"
	return z


# Game graphics
def graphics(x,y):
	print(f"You played {x}.")
	if x == "rock":
		print(rock)
	elif x == "papper":
		print(papper)
	else:
		print(scissors)
	print(f"The computer played {y}")
	if y == "rock":
		print(rock)
	elif y == "papper":
		print(papper)
	else:
		print(scissors)
	
	
#Game loop to 5 wins   ?why does it work with <5 instead of < 6??
while (person_wins<5) and (computer_wins<5):
	result = ""
	person_choice = input("Choose between rock, papper and scissors or enter 'stop' if you do not want to play the game anymore.   ").lower()
	computer_choice = random.choice(computer_choices)
	if person_choice == "stop":
		print(f"You dont want to play anymore, so we are stoping. You have {person_wins} wins and the computer was victorius {computer_wins} ")
	if game(person_choice, computer_choice, result) == "draw":
		graphics(person_choice, computer_choice)
		print(f"It was a draw. Result: you - {person_wins} computer - {computer_wins}")
	elif game(person_choice, computer_choice, result) == "you":
		graphics(person_choice, computer_choice)
		person_wins += 1
		print(f"You win this round. Result: you - {person_wins} computer - {computer_wins}")
	elif game(person_choice, computer_choice, result) == "it":
		graphics(person_choice, computer_choice)
		computer_wins += 1
		print(f"You were bested, better luck next time. Result: you - {person_wins} computer - {computer_wins}")
	if person_wins == 5:
		print("You were victorios at the game")
	elif computer_wins == 5:
		print("Game over, the computer is the superior warrior")