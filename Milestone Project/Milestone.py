def display_game(ttt):
	print("Here is the current list: ")
	for item in ttt:
		print("\t" + ' | '.join(str(x) for x in item))
		print("\t" + "---------")

def row_position():

	choice = "Wrong"
	acceptable_values = ['1','2','3','4','5','6','7','8','9']
    
	while choice not in acceptable_values:
		choice = input("Pick a postion (1-9): ")

		if choice not in acceptable_values:
			print("Invalid Entry. Please enter (1-9): ")
	return int(choice)


def checking_input(ttt, row):

	for x in range(0, len(ttt)):
		for y in range(0, len(ttt)):
			if 1 <= row <= 3:
				y = row - 1
				x = 2
				if ttt[x][y] == 'X' or ttt[x][y] == 'O':
					print("There exists an entry here already")
					return True

			elif 4 <= row <= 6:
				y = row - 4
				x = 1
				if ttt[x][y] == 'X' or ttt[x][y] == 'O':
					print("There exists an entry here already")
					return True

			elif 7 <= row <= 9:
				y = row - 7
				x = 0
				if ttt[x][y] == 'X' or ttt[x][y] == 'O':
					print("There exists an entry here already")
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
	
def tic_tac1(ttt, row, replacement):
	po = 0
	for x in range(0, len(ttt)):
		for y in range(0, len(ttt)):
			if 1 <= row <= 3:
				ttt[2][row - 1] = replacement

			elif 4 <= row <= 6:
				ttt[1][row - 4] = replacement

			elif 7 <= row <= 9:
				ttt[0][row - 7] = replacement
	return ttt

def game_over_row(ttt):

	r1 = ['X','X','X']
	r2 = ['O','O','O']

	return any((i == r1 or i == r2)for i in ttt) 

def game_over_col_diag(ttt):

	for x in range(0, len(ttt), 1):
		for y in range(0, len(ttt),1):
			#Row
			if (ttt[x][y] == 'X' and ttt[x][y+1] == 'X' and ttt[x][y+2] == 'X') or (ttt[x][y] == 'O' and ttt[x][y+1] == 'O' and ttt[x][y+2] == 'O'):
				#print("Row Won")
				return True

			#Diagonal Right
			elif (ttt[x][y] == 'X' and ttt[x+1][y+1] == 'X' and ttt[x+2][y+2] == 'X') or (ttt[x][y] == 'O' and ttt[x+1][y+1] == 'O' and ttt[x+2][y+2] == 'O'):
				#print(f"DR Won {x} {y}")
				return True

			#Diagonal Left
			elif (ttt[x][y+2] == 'X' and ttt[x+1][y+1] == 'X' and ttt[x+2][y] == 'X') or (ttt[x][y+2] == 'O' and ttt[y+1][y+1] == 'O' and ttt[x+2][y] == 'O'):
				#"CL Won"
				return True

			#Column 1
			elif (ttt[x][y] == 'X' and ttt[x+1][y] == 'X' and ttt[x+2][y] == 'X') or (ttt[x][y] == 'O' and ttt[x+1][y] == 'O' and ttt[x+2][y] == 'O'):
				#print("COL Won")
				return True

			#Column 2
			elif (ttt[x][y+1] == 'X' and ttt[x+1][y+1] == 'X' and ttt[x+2][y+1] == 'X') or (ttt[x][y+1] == 'O' and ttt[x+1][y+1] == 'O' and ttt[x+2][y+1] == 'O'):
				#print("COL Won")
				return True

			#Column 3
			elif (ttt[x][y+2] == 'X' and ttt[x+1][y+2] == 'X' and ttt[x+2][y+2] == 'X') or (ttt[x][y+2] == 'O' and ttt[x+1][y+2] == 'O' and ttt[x+2][y+2] == 'O'):
				#print("COL Won")
				return True

			else:
				return False

def game_over_draw(ttt):

	count = 0
	for x in range(0, len(ttt)):
		for y in range(0, len(ttt)):
			if (ttt[x][y] == 'X' or ttt[x][y] == 'O'):
				#print("Draw Check")
				count+=1
				#print(count)

	if count == 9:
		print("Game was a draw")
		return True

	


ttt = [[' ',' ', ' '],[' ',' ', ' '],[' ',' ', ' ']]

player =0
game_on = True

while(game_on):
	display_game(ttt)
	player+=1

	if (player % 2 == 1):
		print("\nPlayer 1's Turn")

	elif (player % 2 == 0):
		print("\nPlayer 2's Turn")


	row = row_position()
	check_check = checking_input(ttt,row)

	while check_check:
		row = row_position()
		check_check = checking_input(ttt,row)

	replacement = x_or_o()

	ttt = tic_tac1(ttt,row,replacement)
	gaming = game_over_row(ttt)
	gaming2 = game_over_col_diag(ttt)
	draw = game_over_draw(ttt)

	if gaming or gaming2:
		display_game(ttt)

		if (player % 2 == 1):
			print("\nPlayer 1 Wins")

		elif (player % 2 == 0):
			print("\nPlayer 2 Wins")

		game_on = False

	elif gaming == False and gaming2 == False and draw:
		display_game(ttt)
		print("Draw. No one wins (Sad Face)")
		game_on = False

