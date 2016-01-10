index=[]
n=input()
for i in range(0,n) :
	index.append(input())

num=input()
cnt=0
for i in range(0,n) :
	if(index[i]==num):
		print i+1
		break
		cnt+=1
if(cnt==n):
	print("-1")