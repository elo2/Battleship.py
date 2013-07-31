# new ships

from random import randint

def new_ship(x, y):
	new_boat = [[x,y]]
	

	for num in range(1,length):
		new_boat.append([x,y+num])
	return new_boat


def rand_list_o_ships():
	new_list = []
	for ships in range(0, 3): # for 3 ships


		new_list.append(ship)
		new_list.sort()
	return new_list

length = randint(1,4) # can be between 1 and 4 in length
direction = randint(1,4) # 1 = N, 2 = E, 3 = S, 4 = W


list_o_ships = rand_list_o_ships()
length = randint(1,4) # can be between 1 and 4 in length
direction = randint(1,4) # 1 = N, 2 = E, 3 = S, 4 = W
def ship_shit(length, direction):
	print "length"
	print length
	print "direction"
	print direction
 	if direction == 1:
		y = randint(0,9)
		if length == 1:
			x = randint(0,9)
		if length == 2:
			x = randint(1,9)
		if length == 3:
			x = randint(2,9)
		if length == 4:
			x = randint(3,9)
		return [x, y]
	
	if direction == 2:
		x = randint(0, 9)
		if length == 1:
			y = randint(0,9)
		if length == 2:
			y = randint(0,8)
		if length == 3:
			y = randint(0,7)
		if length == 4:
			y = randint(0,6)
		return [x,y]
	
	if direction == 3:
		y = randint(0,9)
		if length == 1:
			x = randint(0,9)
		if length == 2:
			x = randint(0,8)
		if length == 3:
			x = randint(2,7)
		if length == 4:
			x = randint(0,6)
		return [x,y]

	if direction == 4:
		x = randint(0, 9)
		if length == 1:
			y = randint(0,9)
		if length == 2:
			y = randint(1,9)
		if length == 3:
			y = randint(2,9)
		if length == 4:
			y = randint(3,9)
		return [x,y]

print ship_shit(length, direction)
		