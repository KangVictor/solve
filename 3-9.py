# prime number that is still prime number when cut right side
# input: number of n sipher (n is input)
# output: all of them
# check_if_prime
# input: num that you want to check if it is prime number
# output: True if right, False if wrong (as boolean type)
import math
n = 0
cnt = 0

def check_if_prime(num) :
	if num < 10 :
		if num == 2 or num == 3 or num == 5 or num == 7 :
			return True
	else : 
		ran = int(math.sqrt(num))
		if ran != math.sqrt(num) :
			ran += 1
		if num%2 == 0 :
			return False
		for i in range(3, ran, 2) :
			if num%i == 0 :
				return False
		return True
# check_if_right_number
# input: number that you want to check, sipher
# output: boolean
def check_if_right_number(num, sipher) :
	if sipher == 0 :
		return True
	if check_if_prime(num) :
		# if cut right side of number -> (num - num%10)/10
		return check_if_right_number((num - num%10)/10, sipher - 1)
	else:
		return False

#make odd odd odd number (ex: 3597)
def make_possible_num (sipher, num) :
	global cnt
	if sipher == -1 :
		# print num
		# return
		# maked possible number
		# check if this number is what we want
		if check_if_right_number(num, n) :
			print num
			cnt += 1
		return
	if sipher == (n - 1) :
		# at start the number should not be 1, 9 because 1, 9 != prime number
		# there should be 2 too
		make_possible_num(sipher - 1, num + 2*pow(10, sipher))
		for i in range(3, 8, 2) :
			make_possible_num(sipher - 1, num + i*pow(10, sipher))
	else :
		# ther should be no 5
		for i in range(1, 5, 2) :
			make_possible_num(sipher - 1, num + i*pow(10, sipher))
		for i in range(7, 10, 2) :
			make_possible_num(sipher - 1, num + i*pow(10, sipher))

# check_if_prime 
# input: num
# output: True or False (as boolean type)
n = input()
# range: 10^n ~ 10^(n + 1) - 1 
# lessen time: range -> +=2 only odd numbers
if n == 1 :
	print(2)
	print(3)
	print(5)
	print(7)
else :
	make_possible_num(n - 1, 0)