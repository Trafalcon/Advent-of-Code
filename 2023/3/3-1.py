import re

input = open('input.txt', 'r')

lines = input.readlines()


# Remove newlines
for x in range(len(lines)):
    lines[x] = lines[x].strip()


# Grab indices of all symbols & numbers

symbols = []
nums = []

x = 0
y = 0

for line in lines:
    length = len(line)
    x = 0
    
    # Search nums & store index
    test = re.finditer("[0-9]+", line)
    
    for match in test:
        nums.append((match.start(), y, match.end()-match.start(), int(match.group())))

    
    for char in line:
        
        # Check if symbol & store index
        if char.isdigit() == False and char != ".":
            symbols.append((x,y))
        
        
        x += 1
    y += 1
    

output_set = []

# For each symbol, check if there is a number adjacent or diagonal
for symb in symbols:
    
    x = symb[0]
    y = symb[1]
    
    min_x = max(x-1,0)
    min_y = max(y-1,0)
    max_x = min(x+1, length)
    max_y = min(y+1,len(lines))
    
    options = [(min_x,min_y),(x,min_y),(max_x,min_y),(min_x,y),(max_x,y),(min_x,max_y),(x,max_y),(max_x,max_y)]
    
    for option in options:
        test = lines[option[1]][option[0]]
        if test.isdigit() == True:
            
            
            
            for num in nums:
                if num[1] == option[1]:
                    if num[0] <= option[0] <= (num[0]+num[2]):
                        output_set.append(num[3])
                        nums.remove(num)
                        break
                


total = 0
for out in output_set:
    total += out


print(total)