n=input()
index=[]
for i in range(0,n):
	index.append(input())
compare=input()
ans=n+1
for i in range(0,n):
	if(index[i]>compare):
		ans=i
print ans