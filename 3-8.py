#input: current temp, hoping temp
#output: minimum click
cnt = 0
def change(temp, button) :
	global cnt
	if temp >= button :
		a = temp/button
		cnt += a
		return temp - (a)*button
	else :
		return temp
data = raw_input().split()
dif_temp = int(data[1]) - int(data[0])
dif_temp = int(abs(dif_temp))
dif_temp = change(dif_temp, 10)
dif_temp = change(dif_temp, 5)
dif_temp = change(dif_temp, 1)
print cnt