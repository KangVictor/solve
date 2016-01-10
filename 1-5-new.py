n = input()
raw = [int(s) for s in raw_input().split()]
target = input()
length=len(raw)
for i in range(length) :
	if starget<raw[i] :
		length = i
print length