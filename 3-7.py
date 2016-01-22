#input: n = # of area(n<=10), m =  diffrent ways to goto another area, cost
#interpretation: 1 = GSHS, college A = n
#output: minimum cost to goto GSHS from college A
n = 0
m = 0
area = []

def GSHS_finder(current_location, cost) :
	if current_location  == n :
		return cost
	minimum_cost = 99999
	for i in range (m) :
		if area[n][0] == current_location :
			returned_cost = GSHS_finder(area[n][1], cost + area[n][2])
			if returned_cost < minimum_cost :
				minimum_cost = returned_cost

		if area [n][1] == current_location :
			returned_cost = GSHS_finder(area[n][0], cost + area[n][2])
			if returned_cost < minimum_cost :
				minimum_cost = returned_cost
	#if no way to go out -> minimum_cost = 99999 -> can't be the minimum cost
	return minimum_cost

#file input part(you can see this as main)
def execute(file_to_execute) :
	with open(file_to_execute, "r") as data_input :
		basic_input_of_file = data_input.read().split()
		#print basic_input_of_file[:]
		global n
		global m
		global area
		n = int(basic_input_of_file[0])
		m = int(basic_input_of_file[1])
		modified_input_of_file = basic_input_of_file[2:]
		cnt = 0
		index = []

		for i in range(3) :
			index.append(0)

		#isinstance(modified_input_of_file, int)
		
		a = -1
		for i in range(m) :
			a += 1
			index[a] = modified_input_of_file[i]
			print a,cnt
			if cnt%3 == 2 :
				a = -1
				area.append(index)
			cnt += 1

		#this part is for checking if input is currect
		print 
		print n, m
		print 
		for i in range(m) :
			for j in range(3) :
				print area[i][j],
			print 
		#input part end

		#finding starts
		#print GSHS_finder(1, 0)

#input part
#I'll use file input
if __name__ == "__main__" :
	execute(raw_input("file name to execute: "))