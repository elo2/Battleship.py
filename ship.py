# new ships

from random import randint
def new_ship(x, y):
	length = randint(1,4)
	direction = randint(1,4)
	print length
	new_boat = [[x,y]]
	for num in range(1,length):
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
length = randint(1,4) # can be between 1 and 4 in length
direction = randint(1,4) # 1 = N, 2 = E, 3 = S, 4 = W
new_boat = []
def ship_shit(length, direction):
 	if direction == 1:
		y = randint(0,9)
		if length == 1:
			x = randint(0,9)
			for num in range (1, length):
				new_boat.append([x, y])
		if length == 2:
			x = randint(1,9)
			for num in range (1, length):
				new_boat.append([x-1, y])
		if length == 3:
			x = randint(2,9)
			for num in range (1, length):
				new_boat.append([x-1, y])
		if length == 4:
			x = randint(3,9)
			for num in range (1, length):
				new_boat.append([x-1, y])
		return new_boat
	
	if direction == 2:
		x = randint(0, 9)
		if length == 1:
			y = randint(0,9)
			for num in range (1, length):
				new_boat.append([x, y])
		if length == 2:
			y = randint(0,8)
			for num in range (1, length):
				new_boat.append([x, y+1])
		if length == 3:
			y = randint(0,7)
			for num in range (1, length):
				new_boat.append([x, y+1])
		if length == 4:
			y = randint(0,6)
			for num in range (1, length):
				new_boat.append([x, y+1])
		return new_boat
	
	if direction == 3:
		y = randint(0,9)
		if length == 1:
			x = randint(0,9)
			for num in range (1, length):
				new_boat.append([x, y])
		if length == 2:
			x = randint(0,8)
			for num in range (1, length):
				new_boat.append([x+1, y])
		if length == 3:
			x = randint(2,7)
			for num in range (1, length):
				new_boat.append([x+1, y])
		if length == 4:
			x = randint(0,6)
			for num in range (1, length):
				new_boat.append([x+1, y])
		return new_boat

	if direction == 4:
		x = randint(0, 9)
		if length == 1:
			y = randint(0,9)
			for num in range (1, length):
				new_boat.append([x, y])
		if length == 2:
			y = randint(1,9)
			for num in range (1, length):
				new_boat.append([x, y-1])
		if length == 3:
			y = randint(2,9)
			for num in range (1, length):
				new_boat.append([x, y-1])
		if length == 4:
			y = randint(3,9)
			for num in range (1, length):
				new_boat.append([x, y-1])
		return new_boat
	print new_boat

print ship_shit(length, direction)
		