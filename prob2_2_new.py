
# INPUT : Queen List & # of Queen placed so far
# OUTPUT: True if safe. False otherwise
def queen_is_safe(queen_list) :
  #ex) queen_list[i] -> queen is in (i,queen_list[i])
  last_index = len(queen_list) - 1
  for i in range(last_index) :
    if i-last_index == queen_list[i]-queen_list[last_index]  :
      return False
    elif last_index-i == queen_list[i]-queen_list[last_index]  :
      return False
    elif queen_list[last_index] == queen_list[i]  :
      return False
  return True

# INPUT : Queen List & # of Queen placed so far
# OUTPUT: # of possibility
def queen_placement(queen_list, max_number_of_queens) :
  if queen_is_safe(queen_list) :
    if len(queen_list) == max_number_of_queens :
      return 1
    possibilities = 0
    for current_queen_position in range(max_number_of_queens) :
      next_queen_list = queen_list[:]
      next_queen_list.append(current_queen_position)
      possibilities += queen_placement(next_queen_list, max_number_of_queens)
    return possibilities
  else :
    return 0
  # Pick one position to place current queen
  # Check whether current queen can be attacked by other queens
  # if so, place to another position
  # if not, proceed

if __name__ == "__main__" :
  # num_of_queens = input()
  # print queen_placement([], num_of_queens)
  for i in range(1,10) :
    print "# of possibilities for N =", i, "is", queen_placement([], i)