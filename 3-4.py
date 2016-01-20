#input: size of pond (vertical only)
#				size of net (vertical only)
#				fish's price
#out put: max cost of fish that can catch with net

length_of_pond=input()
size_of_net=input()
fish=([int(a) for a in raw_input().split()])
# earn=0
maximum_price=0
for i in range(length_of_pond - size_of_net + 1) :
	earn = sum(fish[i:i+size_of_net])
	# for j in range(i, i + size_of_net) :
	# 	earn += fish[j]
	if maximum_price < earn :
		maximum_price = earn
	# earn=0
print maximum_price