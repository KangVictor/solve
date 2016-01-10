# input  : 9 distinct numbers
# output 
#   0th-line : maximum value
#   1st-line : index of max-value
max_value = -1
max_index = -1
for i in range(1, 10) :
  input_value = input()
  if max_value < input_value : 
    max_value = input_value
    max_index = i
print max_value
print max_index