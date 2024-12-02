from multiprocessing import Pool

input = open('test.txt', 'r')

lines = input.readlines()

# List of seeds
temp_map = lines[0].split(":")[1].split()
seeds = []

index = 0
while index < len(temp_map):
    start = int(temp_map[index])
    length = int(temp_map[index+1])
    seeds.append((start, length))
    index += 2



# Store all mappings in (index, destination, source, length) format
mappings = []

index = -1
for line in lines:
    
    if "map:" in line:
        index += 1
    
    elif line[0].isdigit():
        
        line = line.split()
        dest = int(line[0])
        src = int(line[1])
        lth = int(line[2])
        
        mappings.append((index, dest, src, lth))




def search(mappings, seeds, location):
    # Work backwards from 0 to find a valid location
    print("Now checking: " + str(location))
    found = False
    map_index = 6
    # Number checking from Part 1 but reversed
    while map_index >= 0:
        mapped = False
        
        for mapping in mappings:
             if mapping[0] == map_index and mapped == False:
                 
                 dest = int(mapping[1])
                 src = int(mapping[2])
                 lth = int(mapping[3])
                 
                 if dest <= location < dest+lth-1:
                     x = location-dest
                     location = src + x
                     
                     map_index -= 1
                     mapped = True
        
        # If no mapping found, continue on with the same number
        if mapped == False:
            map_index -= 1
    
    
    # Check if location is within seeds
    for seed in seeds:
        start = seed[0]
        length = seed[1]
        if start <= location <= start+length:
            found = True
        
    return found
        
    
with Pool(8) as pool:

        results = [pool.apply(search, (mappings, seeds, i)) for i in range(0,100)]




print(results[0])









