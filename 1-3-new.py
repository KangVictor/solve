n = input()
raw = raw_input()
numbers = [int(n) for n in raw.split()]
target = input()

try :
  print numbers.index(target)
except ValueError :
  print -1
# target_index = -1
# for i in range(len(numbers)) :
#   if numbers[i] == target :
#     target_index = i
#     break

# print target_index
