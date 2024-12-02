import re

input = open('test.txt', 'r')

lines = input.readlines()

# List of seeds
current_map = lines[0].split(":")[1].split()

# Make the seeds ints
for num in current_map:
    current_map[current_map.index(num)] = int(num)


# Use a dictionary to store source/destination mappings
mappings = {}


index = 1
while index < len(lines):
    line = lines[index]
    new_map = [-1] * len(current_map)
    
    # Look for new mapping section
    if ":" in line:
        
        # Check for mapping line
        index += 1
        while lines[index][0].isdigit():
            
            # Grab first mapping line & split by Destination, Source, & Length
            line = lines[index].split()
            dest = int(line[0])
            src = int(line[1])
            lth = int(line[2])
            
            
            # Convert current_map numbers from source to destination
            
            for num in current_map:
                num = int(num)
                if src <= num < src+lth:
                    x = num-src
                    
                    new_map.pop(current_map.index(num))
                    new_map.insert(current_map.index(num), dest+x)
    
            index += 1
        
        # Anything that hasn't changed keeps the same number
        count = new_map.count(-1)
        x = 0
        while x < count:
            new_map[new_map.index(-1)] = current_map[new_map.index(-1)]
            x += 1
        
        print(current_map)
        print(new_map)
        print("\n")
        current_map = new_map
    
    index += 1


current_map = new_map

print(min(current_map))