# Battleshits

from random import randint

board = []

for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleshits!"
print_board(board)

def random_col_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def random_dir():
	return 2 
	#return randint(0, 3) # N = 0, E = 1, S = 2, W = 3

#ship_row = random_row(board)
#ship_col = random_col(board)


def new_ship(x, y):
	length = 3
	direct = random_dir()
	boat = [[x, y],[x, y +1],[x, y + 2]]
	return boat

def rand_list_o_ships():
	new_list = []
	x = randint(0, 9)
	y = randint(0, 6) # ship is len(3) in dir(S)
	ship = new_ship(x, y)
	new_list.append(ship)
	return new_list

list_o_ships = rand_list_o_ships()

#ships = [[[0, 0], [0, 1]]]
def ship_hit(x, y, ships):
	ship = ships[0]
	# ship = [[0, 0], [0, 1]]
	for pos in ship:
		if [x, y] == pos:
			return True
	return False
hit_list = []

def get_coords():
  coords = raw_input("What's the coordinate point you'd like to hit? x,y : ")
  coords.split(",")
  # Gotta how big the split is
  if(len(coords.split(",")) == 2):
    # Python can extra lists using =
    x_str,y_str = coords.split(",")
    try:
      x = int(x_str)
    except ValueError:
      print("Woops, Please enter only integer coordinates in form x,y")
      return get_coords()
      #
    try:
      y = int(y_str)
    except ValueError:
      print("Woops, Please enter only integer coordinates in form x,y")
      return get_coords()
      # 
    return x,y
  else:
    print("Please enter only integer coordinates in form x,y")
    return get_coords()

get_coords()    
print list_o_ships #debug

for turn in range(4):
    guess_hit_x,guess_hit_y = get_coords()

    if ship_hit(guess_hit_x, guess_hit_y, list_o_ships) == True:
        print "Congratulations! You hit my battleshit!"
        board[guess_hit_x][guess_hit_y] = "*"
        hit_list.append([guess_hit[0], guess_hit[1]])
        print_board(board)
        print hit_list #debug
        print list_o_ships[0] #debug
    	
    else:
        if ([guess_hit_x, guess_hit_y] > [9,9]):
            print "Whoa, buddy, keep it in your pants."
        elif(board[guess_hit[0]] == "X") or (board[guess_hit[1]] == "X"):
            print "Been there, done that."
        else:
            print "Haha. NO."
            board[guess_hit[0]][guess_hit[1]] = "X"
        print_board(board)

    if hit_list == list_o_ships[0]:
        	print "Congratulations!! You sank my battleshit!"
        	break

    print "You're on turn:"
    print turn + 1
    if turn == 3:
        print "Game Over!"
        print "Here's where the battleshit was @:"
        board[list_o_ships[0][0][0]][list_o_ships[0][0][1]] = "@"
        board[list_o_ships[0][1][0]][list_o_ships[0][1][1]] = "@"
        board[list_o_ships[0][2][0]][list_o_ships[0][2][1]] = "@"
        print_board(board)

