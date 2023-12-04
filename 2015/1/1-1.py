input = open('input.txt', 'r')

lines = input.readline()


floor = 0

for char in lines:
    
    if char == "(":
        floor += 1
        
    elif char == ")":
        floor -= 1


print(floor)