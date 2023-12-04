input = open('test.txt', 'r')

lines = input.readlines()

# Generate map from input & initialize Distance From Goal Map
Map = []
dfgMap = []


for line in lines:
    line = [int(char) for char in line[:-1]]
    Map.append(line)
    
Max = len(Map) - 1

# Start point is [0,0]
# End point is [Max, Max] Since Map is a square



openList = [(0, 0)]
closedList = []

totalCost = 0


# Looping through pathfinding until found the goal
while (len(openList)) > 0:
    
    
    # Choosing node with smallest risk
    current = openList[0]
    
    for node in openList:
        x = node[0]
        y = node[1]
        temp = Map[y][x]
        current = (x, y) if temp < Map[current[1]][current[0]] else current
        
        
    # Removing current node from openList
    openList.remove(current)
    
    
    # Adding current node to closedList
    closedList.append(current)
    
    
    # Adding current node's risk to total
    totalCost += Map[current[1]][current[0]]
    
    
    # If goal is found, return total trip cost
    if current == (Max, Max):
        print("Total risk: ", totalCost)
        
    
    # Generating children from adjacent nodes (up, down, left, right) (Nodes are in x,y order)
    children = [(current[0], current[1]-1), (current[0], current[1]+1), (current[0]-1, current[1]), (current[0]+1, current[1])]
    
    
    # Prune children that are out of bounds
    remain_children = []
    for child in children:
        if (child[0] >= 0) and (child[0] <= Max) and (child[1] >= 0) and (child[1] <= Max):
            remain_children.append(child)
            
            
    # Add remaining children to openList
    for child in remain_children:
        if child not in openList and child not in closedList:
            openList.append(child)