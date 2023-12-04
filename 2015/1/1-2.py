input = open('input.txt', 'r')

lines = input.readline()


floor = 0
basement = 0

index = 1

for char in lines:
    
    if char == "(":
        floor += 1
        
    elif char == ")":
        floor -= 1
    
    if floor < 0:
        basement = index
        break
    
    index += 1


print(basement)