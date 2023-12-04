input = open('input.txt', 'r')

lines = input.readlines()

grid = []
max_value = 0

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
        
        
    # Find scenic score
    
    # Flip left_trees and up_trees so first values are those closest to current tree
    left_trees = left_trees[::-1]
    up_trees = up_trees[::-1] 
    
    
    # Travel along each line until value is GREATER THAN OR EQUAL TO current value
    
    left = 0
    
    for val in left_trees:
        if val < current:
            left += 1
        else:
            left += 1
            break
        
    right = 0
    
    for val in right_trees:
        if val < current:
            right += 1
        else:
            right += 1
            break
        
    up = 0
    
    for val in up_trees:
        if val < current:
            up += 1
        else:
            up += 1
            break
        
    down = 0
    
    for val in down_trees:
        if val < current:
            down += 1
        else:
            down += 1
            break
    
    score = left * right * up * down
    
    max_value = max(max_value,score)
    
    x += 1
    
    if x >= len(grid[0]):
        x = 0
        y += 1
    
    
    
    







print("Largest scenic score: " + str(max_value))