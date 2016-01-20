perimeter=input()
#a, b, c is 3 sides of triangle
#and also a >= b >= c
#setting
a = b = c = perimeter/3
if perimeter%3==1 :
  a+=1
elif perimeter%3==2 :
  a+=1
  b+=1
cnt=0
for side_c in range(c) :
  for side_b in range(side_c, b) :
    for side_a in range(side_b, a) :
      if side_a < side_b + side_c :
        cnt+=1
        print side_a, side_b, side_c
print cnt