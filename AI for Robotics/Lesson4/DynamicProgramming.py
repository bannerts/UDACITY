# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    dvalue = []    
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                row.append(99)
            else:
                row.append(0)
        dvalue.append(row)
    open = []
    open.append([0, goal])
    iteration = 0
    while len(open) > 0:
        iteration += 1
        open.sort(reverse=True)
        take = open.pop()
        val2, pos = take
        for d in delta:
            x = d[0] + pos[0]
            y = d[1] + pos[1]
            val = val2 + cost
            if 0 <= x and x < len(grid):
                if 0 <= y and y < len(grid[x]):
                    if x == goal[0] and y == goal[1]:
                        pass
                    elif dvalue[x][y] == 0:
                        dvalue[x][y] = val
                        open.append([val, [x, y]])
                    elif dvalue[x][y] == 99:
                        print dvalue[x][y]
                    elif dvalue[x][y] > val:
                        dvalue[x][y] = val
                        open.append([val, [x, y]])
                        
    value = dvalue                    
    return value 

value = compute_value(grid,goal,cost)
print value
