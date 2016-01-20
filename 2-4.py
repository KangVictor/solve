maze=[]
start=[]
end=[]
ans=[]
h=0
w=0
#function find
#input current (x,y) coordinate & cnt
#no output
def find (x,y,cnt,copy_of_maze) :
	#end condition
	if(x==end[0] and y==end[1]) :
		global ans
		ans.append(cnt)
		return 0
	#find way
	copy_of_maze[x][y]=0
	if w-1>y and copy_of_maze[x][y+1]==1 :
		find(x,y+1,cnt+1,copy_of_maze)
	elif h-1>x and copy_of_maze[x+1][y]==1 :
		find(x+1,y,cnt+1,copy_of_maze)
	elif y>0 and copy_of_maze[x][y-1]==1 :
		find(x,y-1,cnt+1,copy_of_maze)
	elif x>0 and copy_of_maze[x-1][y]==1 :
		find(x-1,y,cnt+1,copy_of_maze)
	copy_of_maze[x][y]=1

#input h, w, maze
# .:trail, #:wall S:start G:end
#output shortest way out of maze
ind=[int(a) for a in raw_input().split()]
h=ind[0]
w=ind[1]
index=[]
for i in range(h) :
	index.append([a for a in raw_input().split()])
#change into int type
#0=blocked
#1=pass
#print h
#print w
aa=[]
for i in range(w+1) :
	aa.append(0)
for i in range(h) :
	for j in range(w) :
		#print j
		if index[i][j]=="#" :
			aa[j]=0
		elif index[i][j]=="." :
			aa[j]=1
		elif index[i][j]=="S" :
			start.append(i)
			start.append(j)
			aa[j]=1
		elif index[i][j]=="G" :
			end.append(i)
			end.append(j)
			aa[j]=1
	maze.append(aa)
#find
max=0
find(start[0],start[1],0,maze)
print(len(ans))