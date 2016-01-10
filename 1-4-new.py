n = input()
numbers = [int(s) for s in raw_input().split()]
lower_bound = input()
index = len(numbers)
for i in range(len(numbers)) :
	if lower_bound <= numbers[i] :
		index = i
		break
print index