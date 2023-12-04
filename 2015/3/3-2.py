input = open('input.txt', 'r')

line = input.readline()

visits = [(0,0)]

x = 0
y = 0

x1 = 0
y1 = 0

index = 0

for char in line:
    
    if char == "^":
        if (index%2) == 0:
            y += 1
        else:
            y1 += 1
        
    
    elif char == ">":
        if (index%2) == 0:
            x += 1
        else:
            x1 += 1
    
    elif char == "<":
        if (index%2) == 0:
            x -= 1
        else:
            x1 -= 1
    
    elif char == "v":
        if (index%2) == 0:
            y -= 1
        else:
            y1 -= 1
    
    
    if (index%2) == 0:
        visits.append((x,y))
    else:
        visits.append((x1,y1))
    
    index += 1


visits = set(visits)

print(len(visits))