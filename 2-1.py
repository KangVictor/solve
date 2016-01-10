num = 0
cnt = 0
index = []
def find(i,j):
  global cnt
  global num
  cnt+=1
  index[i][j]=num
  try :
    if(index[i+1][j]==1):
      find(i+1,j)
  except :
    print(""),
  try :
    if(index[i-1][j]==1) :
      find(i-1,j)
  except :
    print(""),
  try :
    if(index[i][j]==1):
      find(i,j+1)
  except :
    print(""),
  try :
    if(index[i+1][j]==1):
      find(i,j-1)
  except :
    print(""),
#input
n=input()
for i in range(n) :
  index.append([int(a) for a in raw_input().split()])
#find
raw=[]
for i in range(n):
  for j in range(n):
    if index[i][j]==1 :
      num+=1
      cnt=0
      find(i,j)
      raw.append(cnt)

print("")
for i in range(n) :
  for j in range(n) :
    print index[i][j],
  print("")
print len(raw)
raw.sort()
for i in range(len(raw)):
  print raw[i]
# 5
# 0 1 1 0 1
# 0 1 1 1 0
# 0 0 0 1 1
# 1 0 1 0 0
# 1 1 1 1 0