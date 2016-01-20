a = []
for i in range(10) :
	a.append(range(i*5, (i+1)*5))
print a # list
print a[2:7] # list
print [lst[3:5] for lst in a[2:7]]