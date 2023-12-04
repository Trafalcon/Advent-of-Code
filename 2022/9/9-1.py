def Tail_Follow(H_X, H_Y, T_X, T_Y):
    if H_X - T_X > 1 and H_Y == T_Y:
        T_X += 1
    
    elif T_X - H_X > 1 and H_Y == T_Y:
        T_X -= 1
    
    elif H_Y - T_Y > 1 and H_X == T_X:
        T_Y += 1
        
    elif T_Y - H_Y > 1 and H_X == T_X:
        T_Y -= 1
        
    elif H_X - T_X > 1:
        T_X += 1
        T_Y = H_Y
        
    elif T_X - H_X > 1:
        T_X -= 1
        T_Y = H_Y
        
    elif H_Y - T_Y > 1:
        T_Y += 1
        T_X = H_X
        
    elif T_Y - H_Y > 1:
        T_Y -= 1
        T_X = H_X

    return T_X, T_Y


input = open('input.txt', 'r')

lines = input.readlines()


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
            
            HeadX += 1
            TailX, TailY = Tail_Follow(HeadX, HeadY, TailX, TailY)
            Tail_Pos.add((TailX, TailY))
            
            i += 1
    
    
    
    # Left
    
    elif direction == 'L':
        i = 0
        while i < count:
            
            HeadX -= 1
            TailX, TailY = Tail_Follow(HeadX, HeadY, TailX, TailY)
            Tail_Pos.add((TailX, TailY))
            
            i += 1
        
     
    # Up    
    
    elif direction == 'U':
       i = 0
       while i < count:
           
           HeadY += 1
           TailX, TailY = Tail_Follow(HeadX, HeadY, TailX, TailY)
           Tail_Pos.add((TailX, TailY))
           
           i += 1
        
     
        
    # Down
    
    elif direction == 'D':
       i = 0
       while i < count:
           
           HeadY -= 1
           TailX, TailY = Tail_Follow(HeadX, HeadY, TailX, TailY)
           Tail_Pos.add((TailX, TailY))
           
           i += 1
        
        
        
        
        
        
        
        
        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
print("Number of Y positions: " + str(len(Tail_Pos)))    
        
        