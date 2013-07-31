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
def ship_shit(length, direction, board):
	print "length"
	print length
	print "direction"
	print direction
 	if direction == 1:
		y = randint(0,len(board)-1)
		if length == 1:
			x = randint(0,len(board)-1)
		if length == 2:
			x = randint(1,len(board)-1)
		if length == 3:
			x = randint(2,len(board)-1)
		if length == 4:
			x = randint(3,len(board)-1)
		return [x, y]
	
	if direction == 2:
		x = randint(0, len(board)-1)
		if length == 1:
			y = randint(0,len(board)-1)
		if length == 2:
			y = randint(0,len(board)-2)
		if length == 3:
			y = randint(0,len(board)-3)
		if length == 4:
			y = randint(0,len(board)-4)
		return [x,y]
	
	if direction == 3:
		y = randint(0,len(board)-1)
		if length == 1:
			x = randint(0,len(board)-1)
		if length == 2:
			x = randint(0,len(board)-2)
		if length == 3:
			x = randint(0,len(board)-3)
		if length == 4:
			x = randint(0,len(board)-4)
		return [x,y]

	if direction == 4:
		x = randint(0, len(board)-1)
		if length == 1:
			y = randint(0,len(board)-1)
		if length == 2:
			y = randint(1,len(board)-1)
		if length == 3:
			y = randint(2,len(board)-1)
		if length == 4:
			y = randint(3,len(board)-1)
		return [x,y]

print ship_shit(length, direction, board)

def valid_ship_placement(x, y, ships, length, direction):
# assume you have a ship list already
ship_list = [ [[0,0],[0,1]] ]

def valid_ship(x,y,ship_length,ship_direction,existing_ships):
  # check of the ship goes out of bounds
  # check if the ship hits any points in ship_list