# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    def isvalid(pos, gridspace):
        y = pos[0]
        x = pos[1]
        if (y < len(grid) and y >= 0):
            if (x < len(grid[y]) and x >= 0):
                if grid[y][x] == 0:
                    return True
        return False

    def isgoal(pos):
        if pos == goal:
            return True
        else:
            return False
        
    def take(openlist):
        if openlist == []:
            taken = []
        else:
            taken = min(openlist)
            openlist.remove(taken)
        return taken, openlist
    
    def move(taken, openlist, grid2, deltas):
        goalpoint = False
        if taken != []:
            for dd in deltas:
                value, y, x = taken[0]+cost, taken[1]+dd[0], taken[2]+dd[1]
                if isvalid([y,x], grid2):
                    grid2[y][x] = 1
                    openlist.append([value, y, x])
                    zz = isgoal([y,x])
                    if zz:
                        goalpoint = [value, y, x]
        return openlist, grid2, goalpoint
        
    path = False
    isagoal = False
    openlistpoints = [[0, init[0], init[1]]]
    totalgrid = grid
    while (not(path or isagoal)):
        taken, openlistpoints = take(openlistpoints)
        openlistpoints, totalgrid, isagoal = move(taken, openlistpoints, totalgrid, delta)
        if openlistpoints == []:
            path = 'fail'
        if isagoal:
            path = isagoal
    return path

result = search(grid,init,goal,cost)
print result

grid55 = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 0]]
result2 = search(grid55,init,goal,cost)
print result2
