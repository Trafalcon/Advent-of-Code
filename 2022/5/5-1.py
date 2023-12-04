input = open('input.txt', 'r')

lines = input.readlines()


# Parse Input

split = lines.index('\n')


# Boxes

stacks = lines[:4]


# Moves

moves = lines[10:]


# Turn Boxes input into List containing boxes **MAKE AUTOMATIC IN FUTURE**

test_boxes = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
input_boxes = [['F', 'C', 'J', 'P', 'H', 'T', 'W'], ['G', 'R', 'V', 'F', 'Z', 'J', 'B', 'H'], ['H', 'P', 'T', 'R'], ['Z', 'S', 'N', 'P', 'H', 'T'], ['N', 'V', 'F', 'Z', 'H', 'J', 'C', 'D'], ['P', 'M', 'G', 'F', 'W', 'D', 'Z'], ['M', 'V', 'Z', 'W', 'S', 'J', 'D', 'P'], ['N', 'D', 'S'], ['D', 'Z', 'S', 'F', 'M']]                                


# Perform Moves on boxes

for move in moves:
    move = move.split(' ')
    
    # Get useful info out of Move
    
    num = int(move[1])
    startPos = int(move[3]) - 1
    endPos = int(move[5]) - 1
    
    
    # Move num top boxes from startPos to endPos (1 at a time)
    
    i = 0
    while i < num:
        
        moved_box = input_boxes[startPos].pop()
        
        input_boxes[endPos].append(moved_box)
        
        i += 1
        
        
        
for stack in input_boxes:
    print(stack.pop())