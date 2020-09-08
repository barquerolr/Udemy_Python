def display_game(tic_tac_toe):
	print("\t" + tic_tac_toe[7] + " | " + tic_tac_toe[8] + " | " + tic_tac_toe[9])
	print("\t--|---|---")
	print("\t" + tic_tac_toe[4] + " | " + tic_tac_toe[5] + " | " + tic_tac_toe[6])
	print("\t--|---|---")
	print("\t" + tic_tac_toe[1] + " | " + tic_tac_toe[2] + " | " + tic_tac_toe[3])

def player_x_or_o():

	marker = ' '
	while marker != 'X' and marker != 'O':
		marker = input("\nPlayer 1, choose  X or O: ")

	player1 = marker
	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'
	return (player1, player2)

def row_position(tic_tac_toe):
	choice = "Wrong"
	acceptable_values = ['1','2','3','4','5','6','7','8','9']
    
	while choice not in acceptable_values:
		choice = input("Pick a postion (1-9): ")

		if choice not in acceptable_values:
			print("Invalid Entry. Please enter (1-9): ")
	return int(choice)

def input_check(tic_tac_toe, row):
	if tic_tac_toe[row] == 'X' or tic_tac_toe[row] == 'O':
		print("There already exists an entry here")
		return True

	else:
		return False

def ttt(tic_tac_toe, row, player_marker):
	tic_tac_toe[row] = player_marker
	return tic_tac_toe

def game_over_row(tic_tac_toe):

	for x in range(1,len(tic_tac_toe),1):
		for y in range(1, len(tic_tac_toe), 3):
			if (tic_tac_toe[y] == 'X' and tic_tac_toe[y+1] == 'X' and tic_tac_toe[y+2] == 'X') or (tic_tac_toe[y] == 'O' and tic_tac_toe[y+1] == 'O' and tic_tac_toe[y+2] == 'O'):
				return True


def game_over_col_diag(tic_tac_toe):

	count = 0
	count2 = 0
	count3 = 0
	count4 = 0
	count5 = 0
	count6 = 0
	count7 = 0
	count8 = 0
	count9 = 0
	count10 = 0

	for x in range(1, len(tic_tac_toe),4):
		if (tic_tac_toe[x] == 'X'):
			count+=1
			if count == 3:
				return True

		elif (tic_tac_toe[x] == 'O'):
			count2+=1
			if count2 == 3:
				return True

	for x in range(7, 1, -2):
		if (tic_tac_toe[x] == 'X'):
			count3+=1
			if count3 == 3:
				return True

		elif (tic_tac_toe[x] == 'O'):
			count4+=1
			if count4 == 3:
				return True

	for x in range(1, len(tic_tac_toe), 3):
		if (tic_tac_toe[x] == 'X'):
			count5+=1
			if count5 == 3:
				return True

		elif (tic_tac_toe[x] == 'O'):
			count6+=1
			if count6 == 3:
				return True

	for x in range(2, len(tic_tac_toe), 3):
		if (tic_tac_toe[x] == 'X'):
			count7+=1
			if count7 == 3:
				return True

		elif (tic_tac_toe[x] == 'O'):
			count8+=1
			if count8 == 3:
				return True

	for x in range(3, len(tic_tac_toe), 3):
		if (tic_tac_toe[x] == 'X'):
			count9+=1
			if count9 == 3:
				return True

		elif (tic_tac_toe[x] == 'O'):
			count10+=1
			if count10 == 3:
				return True



	#elif (tic_tac_toe[1] == 'X' and tic_tac_toe[4] == 'X' and tic_tac_toe[7] == 'X') or (tic_tac_toe[1] == 'O' and tic_tac_toe[4] == 'O' and tic_tac_toe[7] == 'O'):
		#return True
	#elif (tic_tac_toe[2] == 'X' and tic_tac_toe[5] == 'X' and tic_tac_toe[8] == 'X') or (tic_tac_toe[2] == 'O' and tic_tac_toe[5] == 'O' and tic_tac_toe[8] == 'O'):
		#return True
	#if (tic_tac_toe[3] == 'X' and tic_tac_toe[6] == 'X' and tic_tac_toe[9] == 'X') or (tic_tac_toe[3] == 'O' and tic_tac_toe[6] == 'O' and tic_tac_toe[9] == 'O'):
		#return True

def game_over_draw(tic_tac_toe):
	count = 0
	for x in range(0, len(tic_tac_toe)):
		if tic_tac_toe[x] == 'X' or tic_tac_toe[x] == 'O':
			count+=1
			#print("Draw counter")
	if count == 9:
		print("Draw")
		return True

tic_tac_toe = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_game(tic_tac_toe)
player1_marker , player2_marker = player_x_or_o()
player = 0
game_on = True
while game_on:
	player+=1
	display_game(tic_tac_toe)
	row = row_position(tic_tac_toe)
	check = input_check(tic_tac_toe, row)

	while(check):
		row = row_position(tic_tac_toe)
		check = input_check(tic_tac_toe, row)

	if player % 2 == 1:
		tic_tac_toe = ttt(tic_tac_toe, row, player1_marker)

	elif player % 2 == 0:
		tic_tac_toe = ttt(tic_tac_toe, row, player2_marker)

	gaming = game_over_row(tic_tac_toe)
	gaming2 = game_over_col_diag(tic_tac_toe)
	draw = game_over_draw(tic_tac_toe)

	if gaming or gaming2:
		display_game(tic_tac_toe)

		if (player % 2 == 1):
			print("\nPlayer 1 Wins")

		elif (player % 2 == 0):
			print("\nPlayer 2 Wins")

		game_on = False

	elif draw:
		display_game(tic_tac_toe)
		print("Draw. No one wins (Sad Face)")
		game_on = False
