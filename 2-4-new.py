# trail : [(0,0), (1,0), (1,1), (1,2), ...]
def check(place_to_check, trail) :
  for i in trail :
    if i == place_to_check :
      return True

  return False

def explore(x, y, trail, end_point) :
  if (x, y) == end_point :
    return len(trail)
  if check((x, y), trail) :
    # check if visited
    return 10000 #if visited, returns big number to tell it's wrong path
  else :
    new_trail = trail[:]
    new_trail.append((x, y))
    # Right
    trail_right = explore(x, y + 1, new_trail, end_point)
    # Down
    trail_down = explore(x + 1, y, new_trail, end_point)
    # Left
    trail_left = explore(x, y - 1, new_trail, end_point)
    # Up
    trail_up = explore(x - 1, y, new_trail, end_point)
    #find minimum
    minimum=100
    if minimum>trail_right :
      minimum=trail_right
    if minimum>trail_left :
      minimum=trail_left
    if minimum>trail_up :
      minimum=trail_up
    if minimum>trail_down :
      minimum=trail_down

    return minimum #trail_right,left,down,up minimum
    # NOT VISITED CURRENT POSITION

def get_position_of(maze, target) :
  #for searching where is the start and the goal
  for x in range(len(maze)) :
    if target in maze[x] :
      return x, maze[x].index(target)

def execute(filename) :
  with open(filename, "r") as text :
    data = text.read().split()
    height = data[0]
    width = data[1]
    maze = data[2:]
    start_point = get_position_of(maze, "S")
    end_point = get_position_of(maze, "G")
    print start_point
    print end_point
    aa=[]
    print len(explore(start_point[0], start_point[1], aa, end_point)) - 1

if __name__ == "__main__" :
  #file input execute
  execute(raw_input("Enter Testcase File to run : "))