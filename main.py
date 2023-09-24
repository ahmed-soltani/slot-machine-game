MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
	while True:
		amount = input("What would you like to deposit? $")
		if amount.isdigit():
			amount = int(amount) #by default amount will be a string
			if amount > 0:
				break
			else:
				print("Amount must be greater than 0.")
		else:
			print("Please enter a number.")

	return amount

def get_number_of_lines():
	while True:
		#lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
		lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})\n")
		if lines.isdigit():
			lines = int(lines) 
			if 1 <= lines <= MAX_LINES:
				break
			else:
				print("Enter a valid number of lines.")
		else:
			print("Please enter a number.")

	return lines

def get_bet():
	while True:
		amount = input("What would you like to bet? $")
		if amount.isdigit():
			amount = int(amount) #by default amount will be a string
			if MIN_BET <= amount <= MAX_BET:
				break
			else:
				print(f"Amount must be between {MIN_BET} and {MAX_BET}.")
		else:
			print("Please enter a number.")

	return amount

def main():
	balance = deposit()
	lines = get_number_of_lines()
	bet = get_bet()
	print(balance,lines)

main()