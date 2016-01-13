#input n
#output sum of n's factor
n=input()
sum_of_factor=0
for i in range(1,n/2) :
	if n%i==0 :
		sum_of_factor += i
		sum_of_factor += n/i
print sum_of_factor