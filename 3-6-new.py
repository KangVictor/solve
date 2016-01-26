# 5 mok game
# input: 0 = no stone, 1 = white stone, 2= black stone
# output: if white win->print 1 if black win->print 2 else->print 0
# output: first stone

l = 0 #l is length of field
field = []
allowed_range = 0
#function check
#input: way_X, way_Y, white or black, coordinate to start
#contents: each time (with for() method) check if same as input stone color
#output: if 5mok, print x, y & if not, return False
def check (way_X, way_Y,stone_color, x, y) :
	copy_x = x
	copy_y = y
	for i in range(5) :
		copy_x += way_X
		copy_y += way_Y
		if field[copy_x][copy_y] != stone_color :
			return False
	print x,
	print y
	return True

#just for search
def search (x, y, stone_color) :
	#left diagnal way
	if field[x - 1][y + 1] == stone_color :
		return [-1, 1]
	#right diagnal way
	elif field[x + 1][y + 1] == stone_color :
		return [1, 1]
	#horiazntal
	elif field[x][y + 1] == stone_color :
		return [0, 1]
	#vertical
	elif field[x + 1][y] == stone_color :
		return [1, 0]
	else :
		return [-1, -1]

#function execute is method to read file input
def execute(filename):
	with open(filename, "r") as text:
		basic_form = text.read().split()
		l = len(basic_form)

		flag = False
		for i in range(5, 20) :
			if i*i == l :
				#because field is n*n size form
				l = i 
				flag = True
			if flag :
				break

		global allowed_range
		allowed_range = l - 5
		#sucess until here
		global field
		for i in range(l) :
			field[i] = basic_form[l*i:l*i+l-2]
		print l
		for i in field :
			for j in field[i] :
				print j,
			print( )
		# #start finding
		# flag = False
		# for i in range(allowed_range) :
		# 	for j in range(allowed_range) :
		# 		if field[i][j] == 1 or field[i][j] == 2 :
		# 			a = search(i, j, field[i][j])
		# 			if a[0] != -1 and a[1] != -1 :
		# 				if check(a[0], a[1], field[i][j], i, j) :
		# 					flag = True
		# 		if flag :
		# 			return
		# 	if flag :
		# 		return
		# if flag == False :
		# 	print(0)

#this is first way to input
# field = []
# field = ([int(a) for i in raw_input.split()])
#n = len(field)
#however it is a hassle to type the field each time when execute so lets use file input
if __name__ == "__main__" :
	execute(raw_input("Enter filename to execute: "))