def Move(current):
    
    # If starting, move down
    if grid[current[1]][current[0]] == 'S':
        current = (current[0], current[1] + 1)
    
    elif 
    
    
    return current
        

input = open('test.txt', 'r')

lines = input.readlines()

grid = []

# Build grid

for line in lines:
    line = line.strip('\n')
    
    grid.append(list(line))
    
# Find Start & End
x = 0
y = 0

while y < len(grid):
    
    while x < len(grid[y]):
        
        if grid[y][x] == 'S':
            start = (x, y)
        
        elif grid[y][x] == 'E':
            end = (x, y)
        
        x += 1
    
    y += 1
    x = 0




# Starting at S, move through grid to find E
steps = 0

current = (start[0], start[1])

while grid[current[1]][current[0]] != 'E':
    
    print('not E')
    current = Move(current)
    steps += 1