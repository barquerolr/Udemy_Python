#print('Hello World')
#print('New')

from random import shuffle

def shuffle_list(mylist):
	shuffle(mylist)
	return mylist

def player_guess():
	guess = ''

	while guess not in['0', '1', '2']:
		guess = input("Guess a number: 0, 1, or 2 ")
	return int(guess)

def check_guess(mylist, guess):
	if mylist[guess] == 'O':
		print("Correct guess!")
	
	else:
		print("Wrong guess")
		print(mylist)

#Initial List
mylist = ['', 'O', '']

#Shuffle List
mixedlist = shuffle_list(mylist)

#User Guess
guess = player_guess()

#Check Guess
check_guess(mylist, guess)
