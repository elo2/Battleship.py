# Battleshits

from random import randint
import os

board = []

for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print " ".join(row)

print "~~~~~~ \nLet's play Battleshits! \nThis is a single-player game. \nYou have 20 guesses to hit %s ships. \nGood Luck, and don't fuck it up! \n~~~~~~"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def random_dir():
	return 2 
	#return randint(0, 3) # N = 0, E = 1, S = 2, W = 3

#ship_row = random_row(board)
#ship_col = random_col(board)


def new_ship(x, y):
	length = randint(1,4)
	print length
	new_boat = [[x,y]]
	for num in range(1,length):
		#this has to give the right number of coordinates for length
		new_boat.append([x,y+num])
	return new_boat


def rand_list_o_ships():
	new_list = []
	for ships in range(0, 3): # for 3 ships
		x = randint(0, 9)
		y = randint(0, 7)
		ship = new_ship(x,y)
		new_list.append(ship)
		new_list.sort()
	return new_list


list_o_ships = rand_list_o_ships()

#ships = [[[2,3],[2,4],[2,5], [[6,7],[6,8],[6,9]]]
def ship_hit(x, y, ships):
	for ship in ships:
		for pos in ship:
			if [x, y] == pos:
				return True
	return False

hit_list = []

print list_o_ships #debug


for turn in range(20):
    guess_hit = raw_input("~~~~~ \nGuess where my shit is [x, y]")
    [x,y] = guess_hit.split(",")
    x = int(x)
    y = int(y)
    guess_hit = [x,y]
    guess_hit_x = x
    guess_hit_y = y
    print ship_hit(guess_hit_x, guess_hit_y, list_o_ships) #debug

    if ship_hit(guess_hit_x, guess_hit_y, list_o_ships) == True and guess_hit not in hit_list:
        print "~~~~~ \nCongratulations! You hit my battleshit! \n~~~~~"
        board[guess_hit_x][guess_hit_y] = "*"
        hit_list.append([guess_hit[0], guess_hit[1]])
        hit_list.sort()
        print_board(board)
        print hit_list #debug
        for ship in list_o_ships:
        	print ship #debug

    else:
        if (guess_hit > [9,9]):
            print "~~~~~ \nWhoa, buddy, keep it in your pants. \n~~~~~"
        elif (board[guess_hit[0]][guess_hit[1]] == "*"):
   			print "~~~~~ \nBeen there, done that. \n~~~~~"
        else:
            print "~~~~~ \nHaha. NO. \n~~~~~"
            board[guess_hit[0]][guess_hit[1]] = "X"
        print_board(board)

    print hit_list #debug
    print list_o_ships #debug
    print list_o_ships[0] + list_o_ships[1] #debug
    # list_o_ships should be one list of lists instead of a list of lists of lists 
    if hit_list == list_o_ships[0] + list_o_ships[1]: # only works with 2 ships!
    #needs to somehow work for multiple ships (no matter how many)
        print "~~~~~ \nCongratulations!! You sank my battleshits! \n~~~~~"
        break

    print "~~~~~ \nYou're on turn: \n~~~~~"
    print turn + 1
    if turn == 20:
        print "~~~~~ \nGame Over! \n~~~~~"
        print "~~~~~ \nHere's where the battleshit was '@':"
        board[list_o_ships[0][0][0]][list_o_ships[0][0][1]] = "@"
        board[list_o_ships[0][1][0]][list_o_ships[0][1][1]] = "@"
        board[list_o_ships[0][2][0]][list_o_ships[0][2][1]] = "@"
        print_board(board)

