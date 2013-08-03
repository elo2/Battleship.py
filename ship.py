# new ships

from random import randint

board = []

for x in range(20):
    board.append(["O"] * 20)

def print_board(board):
    for row in board:
        print " ".join(row)

#def new_ship(x, y):
#	new_boat = [[x,y]]
	

#	for num in range(1,length):
#		new_boat.append([x,y+num])
#	return new_boat


#def rand_list_o_ships():
	#new_list = []
	#for ships in range(0, 3): # for 3 ships


#		new_list.append(ship)
#		new_list.sort()
#	return new_list

length = randint(1,4) # can be between 1 and 4 in length
direction = randint(1,4) # 1 = N, 2 = E, 3 = S, 4 = W


#list_o_ships = rand_list_o_ships()
length = randint(1,4) # can be between 1 and 4 in length
direction = randint(1,4) # 1 = N, 2 = E, 3 = S, 4 = W
def ship_point(length, direction, board):
	print "length", length
	print "direction", direction
 	if direction == 1:
		x = randint(0,len(board)-1) # fix if direction==1
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
		x = randint(0, len(board)-1)
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
		return [x,y]
	else:
		print "wtf mate"


def new_ship(length, direction, board):
	ship_start = ship_point(length,direction,board)
	ship_points = []
 	if direction == 1:
 		for i in range(0,length):
 			ship_points.append([ship_start[0],ship_start[1]-i])
 		return ship_points
	elif direction == 2:
		for i in range(0,length):
			ship_points.append([ship_start[0], ship_start[1]+i])
		return ship_points
	elif direction == 3:
		for i in range(0,length):
			ship_points.append([ship_start[0]+i, ship_start[1]])
		return ship_points
	elif direction == 4:
		for i in range(0,length):
			ship_points.append([ship_start[0]-i,ship_start[1]])
		return ship_points
	else:
		"new_ship is not able to return a valid ship"

def ships(num_ships,board):
	ship_list = []
	for i in range(0,num_ships):
		ship_len = randint(1,4)
		ship_dir = randint(1,4)
		ship_list.append(new_ship(ship_len, ship_dir, board))
	return ship_list

number_o_ships = randint(1,4)
list_o_ships = ships(number_o_ships, board)
#print ship_point(length, direction, board)
print print_board(board)

#def valid_ship_placement(x, y, length, direction, ships):


# assume you have a ship list already
# ship_list = [ [[0,0],[0,1]] ]
# def valid_ship(x,y,ship_length,ship_direction,existing_ships):
# check if the ship goes out of bounds
# check if the ship hits any points in ship_list