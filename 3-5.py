#put & put2 is only for input
put = [int(a) for a in raw_input().split()]
n = put[0]
m = put[1]
put2 = [int(b) for b in raw_input().split()]
w = put2[0]
h = put2[1]
pond=[]
for i in range(n) :
	pond.append([int(a) for a in raw_input().split()])
print pond
maximum = 0
for i in range(n - w + 1) :
	for j in range(m - h + 1) :
		sub_array = [s[j:j+h] for s in pond[i:i + w]]
		sum_of_sub_array=sum(map(sum, sub_array))
		print sub_array
		if sum_of_sub_array > maximum :
			maximum = sum_of_sub_array
print maximum