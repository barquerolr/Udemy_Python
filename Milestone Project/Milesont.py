def display_game(row1, row2, row3):

	print("Here is the current list: ")
	print("\t" + " | ".join(row1))
	print("\t---------")
	print("\t" + " | ".join(row2))
	print("\t---------")
	print("\t" + " | ".join(row3))

def row_position():

	choice = "Wrong"
	acceptable_values = ['0', '1', '2']

	while choice not in acceptable_values:
		choice = input("Pick a row (0,1,2): ")

		if choice not in acceptable_values:
			print("Invalid Entry. Please enter (0,1,2): ")
	return int(choice)


def check_row(row, row1, row2, row3):
	
	count = 0
	count1 = 0
	count2 = 0

	for element in row1:
		if element == 'X' or element == 'O':
			count+=1

	for elem in row2:
		if elem == 'X' or elem == 'O':
			count1+=1

	for el in row3:
		if el == 'X' or el == 'O':
			count2+=1

	if ((row == 0) and count == 3):
		print("Row 1 has all columns filled")
		return True

	elif ((row == 1) and count1 == 3):
		print("Row 2 has all columns filled")
		return True

	elif ((row == 2) and count2 == 3):
		print("Row 3 has all columns filled")
		return True

	else:
		return False

def column_position():

	cc = 0
	ch = "Wrong"
	col = False
	acceptable_values = ['0', '1', '2']

	while ch not in acceptable_values or col:
		ch = input("Pick a columnm (0,1,2): ")

		if ch not in acceptable_values:
			print("Invalid Entry. Please enter (0,1,2):")

	return int(ch)

def checking_input(row, col):

	if(row[col] == 'X' or row[col] == 'O'):
		print("There already exists an entry.")
		return True
	else:
		return False

def x_or_o():

	choose = "WRONG"
	user_choice = ['X', 'O']
	while choose not in user_choice:
		choose = input("Enter X or O: ")

		if choose not in user_choice:
			print("Invalid Entry: Please enter X or O")

	return choose

def tic_tac1(row, col, rep):

	row[col] = rep
	return row

def game_over_row(ro, ro2, ro3):

	r1 = ['X', 'X', 'X']
	r2 = ['O', 'O', 'O']

	if ro == r1 or ro == r2:
		return True

	elif ro2 == r1 or ro2 == r2:
		return True

	elif ro3 == r1 or ro3 == r2:
		return True
	
	else:
		return False
	

def game_over_col_diag(ro1,ro2,ro3):
	
	game = False

	for i in range(0, len(ro1)):
		for j in range(0, len(ro2)):
			for k in range(0, len(ro3)):
				if (i == j and j == k and i == k):
					if(ro1[i] == 'X' and ro2[j] == 'X' and ro3[k] == 'X') or (ro1[i] == 'O' and ro2[j] == 'O' and ro3[k] == 'O'):
						#print("Column Check")
						game = True
				elif(j == i + 1 and k == i + 2):
					if(ro1[i] == 'X' and ro2[j] == 'X' and ro3[k] == 'X') or (ro1[i] == 'O' and ro2[j] == 'O' and ro3[k] == 'O'):
						#print("Diagonal Right Check")
						game = True
				elif(i == k + 2 and j == k + 1):
					if(ro1[i] == 'X' and ro2[j] == 'X' and ro3[k] == 'X') or (ro1[i] == 'O' and ro2[j] == 'O' and ro3[k] == 'O'):
						#print("Diagonal Left Check")
						game = True
	return game

def game_over_draw(r1, r2, r3):

	r1x = r1.count('X')
	r1o = r1.count('O')

	r2x = r2.count('X')
	r2o = r2.count('O')

	r3x = r3.count('X')
	r3o = r3.count('O')

	if ((r1x == 2 and r1o == 1) or (r1o == 2 and r1x == 1)) and ((r2x == 2 and r2o == 1) or (r2o == 2 and r2x == 1)) and ((r3x == 2 and r3o == 1) or (r3o == 2 and r3x == 1)):
		return True

	else:
		return False


row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

game_on = True
gaming = False #Checking for Rows
gaming2 = False #Checking for Columns and Diagonals
gaming3 = False #Checking for a Draw
draw = False #If a draw exists, draw = True
player = 0 #Player is used to determine turn, and also who wins

while game_on:
	display_game(row1, row2, row3)
	player+=1

	if (player % 2 == 1):
		print("\nPlayer 1's Turn")

	elif (player % 2 == 0):
		print("\nPlayer 2's Turn")

	row = row_position()
	check = check_row(row,row1,row2,row3)

	while(check):
		row = row_position()
		check = check_row(row,row1,row2,row3)

	if row == 0:
		column = column_position() 
		check_check = checking_input(row1,column)

		while check_check:
			column = column_position()
			check_check = checking_input(row1, column)

		replacement = x_or_o()
		row1 = tic_tac1(row1, column, replacement)
		
	if row == 1:
		column = column_position() 
		check_check = checking_input(row2,column)

		while check_check:
			column = column_position()
			check_check = checking_input(row2, column)

		replacement = x_or_o()
		row2 = tic_tac1(row2, column, replacement)

	if row == 2:
		column = column_position() 
		check_check = checking_input(row3,column)

		while check_check:
			column = column_position()
			check_check = checking_input(row3, column)
		replacement = x_or_o()
		row3 = tic_tac1(row3, column, replacement)
	
	gaming = game_over_row(row1, row2, row3)
	gaming2 = game_over_col_diag(row1, row2, row3)
	gaming3 = game_over_draw(row1,row2,row3)

	if(gaming or gaming2):
		game_on = False
		display_game(row1, row2, row3)

		if (player % 2 == 1):
			print("\nPlayer 1 Wins!")
		elif (player % 2 == 0):
			print("\nPlayer 2 Wins!")

	elif gaming == False and gaming2 == False and gaming3:
		game_on = False
		display_game(row1, row2, row3)
		print("\nDraw")
