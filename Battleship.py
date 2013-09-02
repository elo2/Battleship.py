# Battleship

from random import randint
import os


board = []
number_o_ships = randint(2,5)

for x in range(20):
    board.append(["O"] * 20)

def print_board(board):
    for row in board:
        print " ".join(row)

print "~~~~~~ \nLet's play Battleshits!"
print "This is a single-player game."
print "You have 20 guesses to hit %s ships." %number_o_ships
print "Good Luck, and don't fuck it up! \n~~~~~~"

print_board(board)

length = randint(1,4) # can be between 1 and 4 in length
direction = randint(1,4) # 1 = N, 2 = E, 3 = S, 4 = W
def ship_point(length, direction, board):
    #this creates a starting point for the ship using a length and direction
    print "length", length
    print "direction", direction
    if direction == 1:
        x = randint(0,len(board)-1)
        if length == 1:
            y = randint(0,len(board)-1)
        elif length == 2:
            y = randint(1,len(board)-1)
        elif length == 3:
            y = randint(2,len(board)-1)
        elif length == 4:
            y = randint(3,len(board)-1)
        else:
            print "that didn't work out right, did it, huh?"
        return [x, y]
    if direction == 2:
        x = randint(0, len(board)-1)
        if length == 1:
            y = randint(0,len(board)-1)
        elif length == 2:
            y = randint(0,len(board)-2)
        elif length == 3:
            y = randint(0,len(board)-3)
        elif length == 4:
            y = randint(0,len(board)-4)
        else:
            print "that didn't work out right, did it, huh?"
        return [x,y]
    if direction == 3:
        y = randint(0,len(board)-1)
        if length == 1:
            x = randint(0,len(board)-1)
        elif length == 2:
            x = randint(0,len(board)-2)
        elif length == 3:
            x = randint(0,len(board)-3)
        elif length == 4:
            x = randint(0,len(board)-4)
        else:
            print "that didn't work out right, did it, huh?"
        return [x,y]
    if direction == 4:
        y = randint(0, len(board)-1)
        if length == 1:
            x = randint(0,len(board)-1)
        elif length == 2:
            x = randint(1,len(board)-1)
        elif length == 3:
            x = randint(2,len(board)-1)
        elif length == 4:
            x = randint(3,len(board)-1)
        else:
            print "that didn't work out right, did it, huh?"
        return [x,y]
    else:
        print "wtf mate"


def new_ship(length, direction, board):
    #this takes point from ship_point and makes the boat using length and dir.
    ship_start = ship_point(length,direction,board)
    ship_points = []
    if direction == 1:
        for i in range(0,length):
            ship_points.append([ship_start[0],ship_start[1]-i])
        ship_points.sort()
        return ship_points
    elif direction == 2:
        for i in range(0,length):
            ship_points.append([ship_start[0], ship_start[1]+i])
        ship_points.sort()
        return ship_points
    elif direction == 3:
        for i in range(0,length):
            ship_points.append([ship_start[0]+i, ship_start[1]])
        ship_points.sort()
        return ship_points
    elif direction == 4:
        for i in range(0,length):
            ship_points.append([ship_start[0]-i,ship_start[1]])
        ship_points.sort()
        return ship_points
    else:
        print "new_ship is not able to return a valid ship"

def ships(num_ships,board):
    #takes the number of ships you want and puts the randomized ships into list
    ship_list = []
    for i in range(0,num_ships):
        ship_len = randint(1,4)
        ship_dir = randint(1,4)
        ship_list.append(new_ship(ship_len, ship_dir, board))
    ship_list.sort()
    return ship_list

list_o_ships = ships(number_o_ships, board)
print list_o_ships #debug

def ship_hit(x, y, ships):
	for ship in ships:
		for pos in ship:
			if [x, y] == pos:
				return True
	return False

hit_list = []

## made guess_hit a function. removed: 
def guess_hit_bitch():
    for turn in range(20): #gives them 20 turns
        guess_hit = raw_input("~~~~~ \nGuess where my shit is [x, y] :")
        try:
            int(guess_hit)
        except ValueError:
            print "Please enter a coordinate in the form of 'x,y'"
        guess_hit = [x,y]
        guess_hit_x = x
        guess_hit_y = y
        if ship_hit(guess_hit_x, guess_hit_y, list_o_ships) == True:
            if guess_hit not in hit_list:
                print "~~~~~ \nCongratulations! You hit my battleshit! \n~~~~~"
                board[guess_hit_x][guess_hit_y] = "*"
                hit_list.append([guess_hit[0], guess_hit[1]])
                hit_list.sort()
                print_board(board)
                print hit_list #debug
                for ship in list_o_ships:
                	print ship #debug

        else:
            print "You already hit that!"

    else:
        if (guess_hit > [len(board)-1, len(board)-1]):
            print "~~~~~ \nWhoa, buddy, keep it in your pants. \n~~~~~"
        elif (board[guess_hit[0]][guess_hit[1]] == "*"):
   			print "~~~~~ \nBeen there, done that. \n~~~~~"
        else:
            print "~~~~~ \nHaha. NO. \n~~~~~"
            board[guess_hit[0]][guess_hit[1]] = "X"
        print_board(board)

    print list_o_ships #debug
    single_list = []
    for a in list_o_ships:
        for list in a:
            single_list.append(list)
            single_list.sort()
    print "single list", single_list #debug

    if hit_list == single_list:
        print "~~~~~ \nCongratulations!! You sank my battleshits! \n~~~~~"
        print "~~~~~ \nGame Over! \n~~~~~"
        print "~~~~~ \nHere's where the battleshits were '@':"
        for s in single_list:
            board[single_list[0][0][0],single_list[0][0][1]] == "@"
            # gets a TypeError: list indices must be integers, not tuple
            #int object is not subscriptable
            # unsupported opperand, etc...
            #how to get different indices and mark them as a "@"    
            #but on the bright side IT SORT OF WORKS!!!!
        print_board(board)
        break

    print "~~~~~ \nYou're on turn: \n~~~~~", turn + 1
    if turn == 20:
        print "~~~~~ \nGame Over! You ran out of turns :( \n~~~~~"
        print "~~~~~ \nHere's where the battleshit was '@':"
        #for ship in single_list:
        # use same code as above for printing ending game board
        #print_board(board)

