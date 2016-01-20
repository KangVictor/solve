#input index of #
#output max number&its coordinate
max=0
x=-1
y=-1
for i in range(9) :
	index=[int(a) for a in raw_input().split()]
	for j in range(9) :
		if max<index[j] :
			x=i
			y=j
			max=index[j]
print max			
print y+1,x+1