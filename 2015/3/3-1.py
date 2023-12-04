input = open('input.txt', 'r')

line = input.readline()

visits = [(0,0)]

x = 0
y = 0

for char in line:
    
    if char == "^":
        y += 1
    
    elif char == ">":
        x += 1
    
    elif char == "<":
        x -= 1
    
    elif char == "v":
        y -= 1
    
    visits.append((x,y))


visits = set(visits)

print(len(visits))

