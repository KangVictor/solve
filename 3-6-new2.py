def check(matrix, start_region, dir_x, dir_y) :
  print "-"*80
  for start_x in range(len(start_region)) : 
    for start_y in range(len(start_region[start_x])) :
      color = matrix[start_x][start_y]
      print (start_x, start_y), "=>", color
      if color == '0' : # Nothing
        continue
      for count in range(5) :
        if matrix[start_x+count][start_y+count] != color :
          return False
      print color
      print start_x, start_y
      return True
    return False
  return False


#function execute is method to read file input
def execute (filename):
  with open(filename, "r") as text:
    matrix = [line.split(" ") for line in text.read().split("\n")]
    length = len(matrix)
    if len(matrix) != len(matrix[0]) : 
      print "Invalid Input Width", len(matrix[0]), "& Height", len(matrix)
      return
    checked = False
    if not checked : checked = check(matrix, [row[:length-4] for row in matrix[:]], 0, 1) # Horizontal
    if not checked : checked = check(matrix, [row[:] for row in matrix[:length-4]], 1, 0) # Vertical
    if not checked : checked = check(matrix, [row[:length-4] for row in matrix[:length-4]], 1, 1) # Diagonal
    if not checked : checked = check(matrix, [row[:length-4] for row in matrix[4:]], -1, 1) # Inv. Diag.
    if not checked : print 0

# [s[j:j+h] for s in pond[i:i + w]]
if __name__ == "__main__" :
  execute(raw_input("Enter filename to execute: "))