from math import sqrt

n = input()
sum_of_factor = 0
for i in range(1, int(sqrt(n))+1) : 
	if n % i == 0 :
		sum_of_factor += i
		if i != n/i :
			sum_of_factor += n/i
print sum_of_factor