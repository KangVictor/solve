#-*- encoding:utf-8 -*-
#n-queen prob
#대각선 일치->a-b=c-d or a-b=d-c
#세로줄 일치->b=d
queen=[]#[i]줄 queen[i]번
field=[]
cnt=0
n=0
def qp(l) :
	global queen
	global cnt
	flag=0
	for i in range(n) :
		#검사
		for j in range(l) :
			if(i==queen[j]) :
				flag=1
			elif(l-j==i-queen[j]) :
				flag=1
			elif(j-l==i-queen[j]) :
				flag=1
		#검사끝
		if(flag==0) :
			queen[l]=i
			if(l+1==n) :
				cnt+=1
				return
			else :
				qp(l+1)

n=input()
#n-queen solve method start

for i in range(n) :
	queen[0]=i
	qp(1)