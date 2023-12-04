input = open('message.txt', 'r')

lines = input.readlines()

grid = []

# Create tree grid

for line in lines:
    line = line.strip('\n')
    line = list(line)
    grid.append(line)




# Tree Visibility Check - Down, Up, Left, Right
# Tree is visible if all other trees between it and edge are SHORTER than current tree

x = 0
y = 0
visible = 0

while x < len(grid[0]) and y < len(grid):
    
    current = grid[y][x]
    
    # if tree is on edge, automatically visible
    
    if x == 0 or y == 0 or x == (len(grid[0]) - 1) or y == (len(grid) - 1):
        visible += 1
    
    
    # Else check tree heights
    else:
        
        # get list of trees above, below, left, and right of current
        
        left_trees = grid[y][:x]
        right_trees = grid[y][x+1:]
        up_trees = []
        down_trees = []
        
        i = 0
        
        # Fill up_trees
        
        while i < y:
            
            up_trees.append(grid[i][x])
            i += 1
            
        # Fill down_trees
        i = y + 1
        while i < len(grid):
            down_trees.append(grid[i][x])
            i += 1
    
    
        
        # If all values in 4 lists are LESS THAN current value, current is VISIBLE
        left_test = (all(val < current for val in left_trees))
        right_test = (all(val < current for val in right_trees))
        up_test = (all(val < current for val in up_trees))
        down_test = (all(val < current for val in down_trees))
        
        if left_test or right_test or up_test or down_test:
            visible += 1
        
       
    
    
    
    
    x += 1
    
    if x >= len(grid[0]):
        x = 0
        y += 1
    
    
    
    







print("visible tress: " + str(visible))