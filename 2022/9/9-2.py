def Tail_Follow(H_X, H_Y, T_X, T_Y):
    if H_X - T_X > 1 and H_Y == T_Y:
        T_X += 1
    
    elif T_X - H_X > 1 and H_Y == T_Y:
        T_X -= 1
    
    elif H_Y - T_Y > 1 and H_X == T_X:
        T_Y += 1
        
    elif T_Y - H_Y > 1 and H_X == T_X:
        T_Y -= 1
        
    elif H_X - T_X > 1 and H_Y != T_Y:
        T_X += 1
        
        if H_Y - T_Y > 0:
            T_Y += 1
        elif T_Y - H_Y > 0:
            T_Y -= 1
        
    elif T_X - H_X > 1 and H_Y != T_Y:
        T_X -= 1
        
        if H_Y - T_Y > 0:
            T_Y += 1
        elif T_Y - H_Y > 0:
            T_Y -= 1
        
    elif H_Y - T_Y > 1 and H_X != T_X:
        T_Y += 1
        
        if H_X - T_X > 0:
            T_X += 1
        elif T_X - H_X > 0:
            T_X -= 1
        
    elif T_Y - H_Y > 1 and H_X != T_X:
        T_Y -= 1
        
        if H_X - T_X > 0:
            T_X += 1
        elif T_X - H_X > 0:
            T_X -= 1

    return T_X, T_Y


input = open('input.txt', 'r')

lines = input.readlines()

numKnots = 10
Coords = []
x = 0
while x < numKnots:
    Coords.append([0,0])
    x += 1

HeadX = 0
HeadY = 0
TailX = 0
TailY = 0

Tail_Pos = set({})

# Reading moves

for line in lines:
    
    line = line.strip('\n')
    line = line.split(' ')
    
    direction = line[0]
    count = int(line[1])
    
    # Find Direction to Move Head
    
    # Right
    
    if direction == 'R':
        i = 0
        while i < count:
            
            Coords[0][0] += 1
            
            index = 1
            
            while index < len(Coords):
            
                Coords[index][0], Coords[index][1] = Tail_Follow(Coords[index-1][0], Coords[index-1][1], Coords[index][0], Coords[index][1])
                
                index += 1
            
            Tail_Pos.add((Coords[-1][0], Coords[-1][1]))
            
            i += 1
            print(Coords)
    
    
    
    # Left
    
    elif direction == 'L':
        i = 0
        while i < count:
            
            Coords[0][0] -= 1
            
            index = 1
            
            while index < len(Coords):
            
                Coords[index][0], Coords[index][1] = Tail_Follow(Coords[index-1][0], Coords[index-1][1], Coords[index][0], Coords[index][1])
                
                index += 1
            
            Tail_Pos.add((Coords[-1][0], Coords[-1][1]))
            
            i += 1
            print(Coords)
        
     
    # Up    
    
    elif direction == 'U':
       i = 0
       while i < count:
           
           Coords[0][1] += 1
           
           index = 1
           
           while index < len(Coords):
           
               Coords[index][0], Coords[index][1] = Tail_Follow(Coords[index-1][0], Coords[index-1][1], Coords[index][0], Coords[index][1])
               
               index += 1
           
           Tail_Pos.add((Coords[-1][0], Coords[-1][1]))
           
           i += 1
           print(Coords)
        
     
        
    # Down
    
    elif direction == 'D':
       i = 0
       while i < count:
           
           Coords[0][1] -= 1
           
           index = 1
           
           while index < len(Coords):
           
               Coords[index][0], Coords[index][1] = Tail_Follow(Coords[index-1][0], Coords[index-1][1], Coords[index][0], Coords[index][1])
               
               index += 1
           
           Tail_Pos.add((Coords[-1][0], Coords[-1][1]))
           
           i += 1
           print(Coords)
        
        
        
    print('\n')  
        
        
        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
print("Number of tail positions: " + str(len(Tail_Pos)))    
        
        