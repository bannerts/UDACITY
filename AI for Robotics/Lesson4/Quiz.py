# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    
    value = [[ [999, 999, 999, 999] for row in range(len(grid[0]))] for col in range(len(grid))] 
    pa = [[ [-1, -1, -1, -1] for row in range(len(grid[0]))] for col in range(len(grid))]
    policy2D =  [[' ' for row in range(len(grid[0]))] for col in range(len(grid))] 
    
    def heuristic(x, y, d):
        h = 0
        isvalid = True
        if not (d in range(len(forward))):
            return h, False
        elif not (x in range(len(grid))):
            return h, False
        elif not (y in range(len(grid[x]))):
            return h, False
        elif grid[x][y] == 1:
            return h, False
        return 0, True
    
    
    x0 = init[0]
    y0 = init[1]
    d0 = init[2]
    g0 = 0
    h0, _ = heuristic(x0, y0, d0)
    f0 = g0 + h0
    open = [ [ (f0,g0,h0), x0, y0, d0 ] ]
    value[x0][y0][d0] = g0
    found = False
    resign = False
    count = 0
    dirs = ['up', 'left', 'down', 'right']
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'Fail'
        open.sort(reverse=True)
        next = open.pop()
        [(fi, gi, hi), xi, yi, di] = next
        if [xi, yi] == goal:
            found = True
        else:
            for i in range(len(action)):
                d = (di + action[i]) % len(forward);
                x = xi + forward[d][0]
                y = yi + forward[d][1]
                g = gi + cost[i]
                h, isvalid = heuristic(x, y, d)            
                f = g + h
                # print x, y, dirs[di], dirs[d], isvalid
                if isvalid:
                    if g <= value[x][y][d]:
                        value[x][y][d] = g
                        pa[x][y][d] = i
                        # print x, y, dirs[d]
                        open.append([(f, g, h), x, y, d])
    
    if found:
        policy2D[xi][yi] = '*'

        while [xi, yi, di] != init:
            # print xi, yi, dirs[di]
            i = pa[xi][yi][di]
            a_name = action_name[i]
            a = action[i]
            [dx, dy] = forward[di]
            xi = xi - dx
            yi = yi - dy
            di = (di - a) % (len(forward))
            policy2D[xi][yi] = a_name
    
    return policy2D

out = optimum_policy2D(grid,init,goal,cost)
print out
