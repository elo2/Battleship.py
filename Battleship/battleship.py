# Battleshits

from random import randint
import os

def print_board(board):
    for row in board:
        print " ".join(row)

def ship_point(length, direction, board):
    #this creates a starting point for the ship using a length and direction
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
    elif direction == 2:
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
    elif direction == 3:
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
    elif direction == 4:
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
        print "wtf mate, how did you get here?"

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
        print "hrmmm, I was unable to return a valid ship"

def ships(num_ships,board):
    #takes the number of ships you want and puts the randomized ships into list
    ship_list = []
    for i in range(num_ships):
        ship_len = randint(1,4)
        print "Length of ship #", i+1, "=", ship_len
        ship_dir = randint(1,4)
        ship_list.append(new_ship(ship_len, ship_dir, board))
    ship_list.sort()
    return ship_list

def ship_hit(x, y, ships):
	for ship in ships:
		for pos in ship:
			if [x, y] == pos:
				return True
	return False

def guess_hit():
    guess_hit_input = raw_input("~~~~~ \nGuess where my ship is [x, y] :")
    guess_hit_input.split(",")
    if (len(guess_hit_input.split(",")) == 2):
        x_str,y_str = guess_hit_input.split(",")
        try:
            guess_hit_x = int(x_str)
        except ValueError:
            print "Nice try, please enter a valid coordinate"
            return guess_hit()
        try:
            guess_hit_y = int(y_str)
        except ValueError:
            print "Nice try, please enter a valid cordinate"
            return guess_hit()
        return guess_hit_x,guess_hit_y
    else:
        print "Nice try, please enter a valid coordinate in form x,y :"
        return guess_hit()


#Does not work for when out of board range? FIX PLEASE


## :: Functions above :: Game play below ::

board = []

for x in range(20):
    board.append(["O"] * 20)

number_o_ships = randint(2,5)

print "~~~~~~ \nLet's play Battleship!"
print "This is (for now) a single-player game."
print "Good Luck, and don't mess it up! \n~~~~~~"
print "You have", number_o_ships * 6, "guesses to hit %s ships.\n" %number_o_ships
length = randint(1,4) # can be between 1 and 4 in length
direction = randint(1,4) # 1 = N, 2 = E, 3 = S, 4 = W
list_o_ships = ships(number_o_ships, board)

print "\n**** For debugging purposes only ****\nlist o' ships", list_o_ships, "\n" #debug

print_board(board)
hit_list = []
    
single_list = []
for a in list_o_ships:
    for lists in a:
        single_list.append(lists)
        single_list.sort()

for turn in range(20):
    guess_hit_x, guess_hit_y = guess_hit()
    guess_hit_coord = [guess_hit_x, guess_hit_y]

    if ship_hit(guess_hit_x, guess_hit_y, list_o_ships) == True:
        if guess_hit_coord not in hit_list:
            print "~~~~~ \nCongratulations! You hit my battleshit! \n~~~~~"
            board[guess_hit_x][guess_hit_y] = "*"
            hit_list.append([guess_hit_coord[0], guess_hit_coord[1]])
            hit_list.sort()
            print_board(board)
            print hit_list #debug
            for ship in list_o_ships:
                print ship #debug
        else:
            print "You already hit that!"

    #### How to know when someone sinks a ship??? ###

    else:
        if (guess_hit_coord > [len(board)-1, len(board)-1]): #This might be a bug, test this
            print "~~~~~ \nWhoa, buddy, keep it in your pants. \n~~~~~"
        elif (board[guess_hit[0]][guess_hit[1]] == "*"):
    	        print "~~~~~ \nBeen there, done that. \n~~~~~"
        else:
            print "~~~~~ \nHaha. NO. \n~~~~~"
            board[guess_hit_coord[0]][guess_hit_coord[1]] = "X"
        print_board(board)

    if hit_list == single_list:
        print "~~~~~ \nCongratulations!! You sank my battleshits! \n~~~~~"
        print "~~~~~ \nGame Over! \n~~~~~"
        print_board(board)
        

    print "~~~~~ \nYou're on turn: \n~~~~~", turn + 1
    if turn == (number_o_ships * 6):
        print "~~~~~ \nGame Over! You ran out of turns :( \n~~~~~"
        print "~~~~~ \nHere's where the battleshit was '@':"
