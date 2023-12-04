def generate_board():
    # Finding max X & Y
    maxX = 0
    maxY = 0

    for dot in dots:
        x = dot[0]
        y = dot[1]
        maxX = max(x, maxX)
        maxY = max(y, maxY)
    print(maxX, maxY)

    # Generating board dimensions
    board = [['.'] * (maxX+1)] * (maxY+1)

    # Adding dots to board
    for dot in dots:
        x = dot[0]
        y = dot[1]
        temp = list(board[y])
        temp[x] = '#'
        board[y] = temp
        
    return board

def print_board():
    print('\n')
    # Printing formatted board
    for line in board:
        print(' '.join(line))

    return board


def fold_board(axis, location):
    print(axis, location)
    
    # Folding board in half based on axis & location
    
    # If axis is y
    if axis == 'y':
        trackY = location+1
        trackX = 0
        
        # Move dots from lower half to upper half
        for line in board[trackY:]:
            trackX = 0
            for x in line:
                if x == '#':
                    temp = list(board[location - (trackY-location)])
                    temp[trackX] = '#'
                    board[location - (trackY-location)] = temp
                
                trackX = trackX+1
                
            trackY = trackY+1
            
    
        # Remove folded section
        del board[location:]
    
    
    # If axis is x
    if axis == 'x':
        trackY = 0
        trackX = location+1
        
        # Move dots from right half to left half
        for line in board:
            trackX = location+1
            for x in line[trackX:]:
                if x == '#':
                    temp = list(board[trackY])
                    temp[location - (trackX-location)] = '#'
                    board[trackY] = temp
                    
                trackX = trackX + 1
                    
            trackY = trackY +1
            
        # Remove folded section
        for line in board:
            del line[location:]
   
        
        
    return board





# Start
input = open('cole_input.txt', 'r')

lines = input.readlines()

dots = []
folds = []
board = []

InputBreakPoint = False


# Formatting data

for line in lines:
    if line == '\n':
        InputBreakPoint = True
        continue
    if not InputBreakPoint:
        line = line.strip('\n')
        temp = line.partition((','))
        dots.append([int(temp[0]), int(temp[2])])
    if InputBreakPoint:
        folds.append(line.strip('\n'))
    
    
# Generate starting board from input
board = generate_board()
    

# Print starting board
print_board()

# Fold board & print result after each fold
for fold in folds:
    fold = fold.partition('=')
    board = fold_board(fold[0][-1], int(fold[2]))
    print_board()
    

















































