n=input()
index=[]
for i in range(0,n) :
	index.append(input())

cnt=0
compare=input()
for i in range(0,n) :
	if (index[i]>=compare) :
		print i+1
		cnt+=1
		break
if(cnt==0) :
	print n+1