import os
import subprocess
import random
import time
import colorama

puzzles = {
    "What are you doing?": [
        "FLYING A KITE", "CLOSING A WINDOW", "ADOPTING A PET", "ENJOYING LIFE",
        "JUMPING UP AND DOWN"
    ],
    "On the map": [
        "THE GOLDEN STATE", "BIG APPLE", "CHINATOWN", "HOLLYWOOD BOULEVARD",
        "THE CARIBBEAN SEA"
    ],
    "Event": [
        "BIRTHDAY PARTY", "A WEEKEND GETAWAY", "FOURTH OF JULY",
        "INAUGURATION DAY", "FAMILY PHOTOSHOOT"
    ],
    "Food & Drink": [
        "APPLES AND ORANGES", "CAULIFLOWER RICE",
        "FRESHLY SQUEEZED GRAPEFRUIT JUICE", "HOMEMADE CHOCOLATE CHIP COOKIES",
        "SWEET AND SOUR CHICKEN"
    ],
    "Around the house": [
        "HALLWAY CLOSET", "PLUSH COTTON TOWELS", "WALL MOUNTED TELEVISION",
        "BEDSIDE LAMP", "SOFA AND A LOUNGE CHAIR"
    ],
}

puzzles_list = list(puzzles.items())
random_category = random.choice(puzzles_list)
puzzle_to_be_played = list(random.choice(random_category[1]))
guessed_puzzle = []

wheel = [
    "Bankrupt", "Loose a Turn", "Jackpot", "Free Play", 50, 100, 250, 500, 750,
    1000, 2000
]


def clear():
	""" clears the console screen """

	if os.name in ('nt', 'dos'):
		subprocess.call("cls")
	elif os.name in ('linux', 'osx', 'posix'):
		subprocess.call("clear")
	else:
		print("\n") * 120


def clear_and_display(contestant, bank):
	clear()
	welcome_contestant(contestant)
	print()
	print("''", random_category[0], "''")
	print()
	print(listToString(guessed_puzzle))
	print()


def update_bank(bank, cash):
	""" updates the contestant's bank """

	if cash == -1:
		bank = 0
	else:
		bank = bank + cash
	return bank


def display_initial_welcome():
	""" display welcome message """

	print("Welcome to " + colorama.Fore.RED + "T" + colorama.Fore.GREEN + "H" +
	      colorama.Fore.WHITE + "E" + colorama.Fore.BLUE + " W" +
	      colorama.Fore.YELLOW + "H" + colorama.Fore.RED + "E" +
	      colorama.Fore.GREEN + "E" + colorama.Fore.WHITE + "L" +
	      colorama.Fore.BLUE + " O" + colorama.Fore.YELLOW + "F" +
	      colorama.Fore.RED + " F" + colorama.Fore.GREEN + "O" +
	      colorama.Fore.WHITE + "R" + colorama.Fore.BLUE + "T" +
	      colorama.Fore.YELLOW + "U" + colorama.Fore.RED + "N" +
	      colorama.Fore.GREEN + "E" + colorama.Fore.RESET)
	print()


def get_contestant_name():
	""" asks the contestant's name and returns it """

	name = input("Please enter your name > ")
	name = name.title()
	clear()
	return name


def welcome_contestant(contestant):
	""" display welcome message and the contestant name with a message """

	display_initial_welcome()
	print()
	print(f"{contestant} lets get started")
	print()
	print()
	return


def guessed_puzzle_to_show(puzzle):
	""" converts the selected puzzle to all dashes """

	i = 0
	while i < len(puzzle):
		if puzzle[i] != " ":
			guessed_puzzle.append("_")
			i = i + 1
		else:
			guessed_puzzle.append(" ")
			i = i + 1
	return guessed_puzzle


def listToString(input_list):
	""" converts a list to string """

	string = ""
	for ele in input_list:
		string = string + ele
	return string


def show_category(guessed_puzzle):
	""" shows the category & puzzle in dashes to the contestant """

	print("The category for this puzzle is")
	print("''", random_category[0], "''")
	print()
	print(listToString(guessed_puzzle))
	print()


def wheel_spin_progress_bar(contestant, bank):
	i = 0
	bar = ""
	while i < 10:
		clear_and_display(contestant, bank)
		bar = bar + "█ "
		i = i + 1
		print(bar)
		time.sleep(.5)


def puzzle_has_dashes(check_puzzle):
	""" checks if the puzzle still has dashes"""

	for ele in check_puzzle:
		if ele == "_":
			return True
	return False


def letter_already_called(letters_called, guessed_letter):
	""" checks if the letter has alraedy been called """

	for letter in letters_called:
		if letter == guessed_letter:
			return True
	return False


def is_vowel(check_letter):
	""" checks if the letter is a vowel or not """

	if check_letter == "A" or check_letter == "E" or check_letter == "I" or check_letter == "O" or check_letter == "U":
		return True
	else:
		return False


def remaining_vowels():
	""" checks if all the vowels have been called in the puzzle """

	i = 0
	while i < len(puzzle_to_be_played):
		if is_vowel(
		    puzzle_to_be_played[i]) == True and guessed_puzzle[i] == "_":
			return True
		i = i + 1
	return False


def remaining_consonants():
	""" checks if all the vowels have been called in the puzzle """

	i = 0
	while i < len(puzzle_to_be_played):
		if is_vowel(
		    puzzle_to_be_played[i]) == False and guessed_puzzle[i] == "_":
			return True
		i = i + 1
	return False


def wheel_spin(wheel_ind, contestant, bank):
	""" wheel spin lands on a perticular wedge and returns that value"""

	if wheel[wheel_ind] == "Bankrupt":
		clear_and_display(contestant, bank)
		print("Oh no you hit Bankrupt. Your bank is 0 now.")
		wheel_amount = 0
		return wheel_amount, wheel[wheel_ind]
	elif wheel[wheel_ind] == "Loose a Turn":
		clear_and_display(contestant, bank)
		print("Oh no you hit Loose a Turn.")
		wheel_amount = 0
		return wheel_amount, wheel[wheel_ind]
	elif wheel[wheel_ind] == "Jackpot":
		print(
		    "Yay you hit Jackpot. That is worth $5000 a piece if you get the next letter correct."
		)
		wheel_amount = 5000
		return wheel_amount, wheel[wheel_ind]
	elif wheel[wheel_ind] == "Free Play":
		if remaining_vowels() == True:
			print("Yay you get Free Play. You can call a vowel for free.")
		else:
			print("Yay you get Free Play.")
		wheel_amount = 250
		return wheel_amount, wheel[wheel_ind]
	else:
		print(
		    f"${wheel[wheel_ind]}. If you call the next letter correctly, ${wheel[wheel_ind]} a piece will be added to your total."
		)
		wheel_amount = wheel[wheel_ind]
		return wheel_amount, wheel[wheel_ind]


def guessed_letter_in_puzzle(guessed_letter):
	""" checks if the guessed letter is in the puzzle """

	i = 0
	count = 0
	while i < len(puzzle_to_be_played):
		if len(guessed_letter) > 1 or guessed_letter.isalpha() == False:
			count = -2
			i = len(puzzle_to_be_played)
		elif guessed_letter == guessed_puzzle[i]:
			count = -1
			i = len(puzzle_to_be_played)
		elif guessed_letter == puzzle_to_be_played[i]:
			guessed_puzzle[i] = guessed_letter
			count = count + 1
			i = i + 1
		else:
			i = i + 1
	return count


def guessed_consonant_in_puzzle(cash, wedge, guessed_letter, contestant, bank):
	""" checks if the guessed consonant is in the puzzle """

	count = guessed_letter_in_puzzle(guessed_letter)
	if count == -2:
		clear_and_display(contestant, bank)
		print(
		    f"Sorry, '{guessed_letter}' is not a valid letter. Only a single alphabet is accepted."
		)
		cash = 0
	elif count == -1:
		clear_and_display(contestant, bank)
		print(f"Sorry, {guessed_letter} was already called.")
	elif count == 1:
		clear_and_display(contestant, bank)
		print(f"Good call. We have {count} {guessed_letter} in the puzzle.")
	elif count > 1:
		clear_and_display(contestant, bank)
		print(f"Good call. We have {count} {guessed_letter}'s in the puzzle.")
		cash = cash + ((count - 1) * wedge)
	else:
		clear_and_display(contestant, bank)
		print(f"Sorry, there is no {guessed_letter} in the puzzle.")
		cash = 0
	return cash


def guessed_vowel_in_puzzle(vowel, contestant, bank):
	""" checks if the guessed vowel is in the puzzle """

	count = guessed_letter_in_puzzle(vowel)
	if count == -2:
		clear_and_display(contestant, bank)
		print(
		    f"Sorry, {vowel} is not a valid vowel. Only a single alphabet is accepted."
		)
		return False
	elif count == -1:
		clear_and_display(contestant, bank)
		print(f"Sorry, {vowel} was already called.")
		return False
	elif count == 1:
		clear_and_display(contestant, bank)
		print(f"Good call. We have {count} {vowel} in the puzzle.")
		return True
	elif count > 1:
		clear_and_display(contestant, bank)
		print(f"Good call. We have {count} {vowel}'s in the puzzle.")
		return True
	else:
		clear_and_display(contestant, bank)
		print(f"Sorry, there is no {vowel} in the puzzle.")
		return True


def next_move(contestant, letters_called, bank):
	""" checks the letter in the puzzle and appends it and updates the cash amount """

	print(f"Your total bank is --> {bank}")
	print()
	input("To spin the wheel please press enter > ")
	wheel_spin_progress_bar(contestant, bank)
	wheel_ind = random.randint(0, 10)

	cash, wedge = wheel_spin(wheel_ind, contestant, bank)
	if wedge == "Bankrupt":
		cash = -1
		return cash
	elif wedge == "Loose a Turn":
		return cash
	elif wedge == "Jackpot" or wedge == "Free Play" or wedge > 3:
		wedge_amount = 0
		i = 0
		while i < 1:
			while True:
				print()
				print("What letter would you like to call?")
				guessed_letter = input("> ")
				if len(guessed_letter) == 1:
					break
				print()
				print(
				    f"Sorry, '{guessed_letter}' is not a valid letter. Only a single alphabet is accepted."
				)
			print()
			guessed_letter = guessed_letter.upper()
			if is_vowel(guessed_letter) == True:
				clear_and_display(contestant, bank)
				print("You cannot call a vowel.")
				print("Please enter a consonant.")
				i = 0
			elif letter_already_called(letters_called, guessed_letter) == True:
				clear_and_display(contestant, bank)
				print(f"{guessed_letter} has already been called.")
				print("Please enter another letter.")
				i = 0
			else:
				letters_called.append(guessed_letter)
				if wedge == "Jackpot":
					wedge_amount = 5000
				elif wedge == "Free Play":
					wedge_amount = 250
				else:
					wedge_amount = wedge
				cash = guessed_consonant_in_puzzle(cash, wedge_amount,
				                                   guessed_letter, contestant,
				                                   bank)
				i = 1
		return cash


def buy_a_vowel(bank, contestant, letters_called):
	""" asks the contestant if they want to buy a vowel """

	cash = 0
	i = 1
	while i > 0 and bank >= 250 and remaining_vowels() == True:
		print()
		print("Would you like to buy a vowel? ")
		buy_vowel = input("Y/N -- > ")
		buy_vowel = buy_vowel.upper()
		print()
		if buy_vowel == "Y":
			print("What vowel would you like to buy?")
			vowel = input("> ")
			vowel = vowel.upper()
			clear_and_display(contestant, bank)
			vowel_status = guessed_vowel_in_puzzle(vowel, contestant, bank)
			if vowel_status == True:
				letters_called.append(vowel)
			cash = -250
			i = i + 1
			bank = update_bank(bank, cash)
		elif buy_vowel != "Y" and buy_vowel != "N":
			print("Please enter Y/N ")
			i = i + 1
		else:
			i = 0
			clear_and_display(contestant, bank)
	if remaining_vowels() == False:
		print()
		print("There are no more vowels in the puzzle")
	return bank


def checking_consonants_and_vowels(bank, contestant, letters_called):
	""" checks the consonants and the vowels in the puzzle and displays if the contestant won """

	puzzle_has_dashes(guessed_puzzle) == True
	puzzle_solved = True
	while puzzle_has_dashes(guessed_puzzle):
		if remaining_consonants() == False and remaining_vowels(
		) == True and bank < 250:
			print(
			    "Unfortunately you don't have enough money to buy more vowels. Better luck next time!"
			)
			puzzle_solved = False
			break
		elif remaining_consonants() == True and remaining_vowels() == True:
			cash = next_move(contestant, letters_called, bank)
			bank = update_bank(bank, cash)
			bank = buy_a_vowel(bank, contestant, letters_called)
		elif remaining_consonants() == False and remaining_vowels() == True:
			print()
			print("There are no more consonants in the puzzle.")
			bank = buy_a_vowel(bank, contestant, letters_called)
		elif remaining_consonants() == True and remaining_vowels() == False:
			print()
			print("There are no more vowels in the puzzle.")
			cash = next_move(contestant, letters_called, bank)
			bank = update_bank(bank, cash)
	if puzzle_solved == True:
		print()
		print(f"Congratulations {contestant}! You guessed the puzzle.")
		print(f"Your Total winnings are ${bank}")


def play_game():
	""" runs the Wheel of Fortune Game """

	bank = 0
	letters_called = []
	display_initial_welcome()
	contestant = get_contestant_name()
	welcome_contestant(contestant)
	guessed_puzzle_to_show(puzzle_to_be_played)
	show_category(guessed_puzzle)
	checking_consonants_and_vowels(bank, contestant, letters_called)


play_game()
