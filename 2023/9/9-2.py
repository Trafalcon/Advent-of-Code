input = open('input.txt', 'r')

lines = input.readlines()

# Build out instruction set
instructions = lines[0].replace("R","1").replace("L","0").strip()
    
# Build out node network
nodes = {}

for line in lines[2:]:
    key = line.split("=")[0].strip()
    values = line.split("=")[1].replace("(","").replace(")","").strip().split(",")
    
    nodes.update({key: (values[0].strip(), values[1].strip())})


# Find starting locations that end in "A"
locations = []
for node in nodes.keys():
    if node[2] == "A":
        locations.append(node)

# Read instructions to find next node until "ZZZ" is found
num_steps = 24346967268

not_found = True
while not_found == True:
    print(num_steps)
    
    for char in instructions:
        for x in range(0, len(locations)):
            if locations[x][2] == "Z":
                not_found = False
            else:
                not_found = True
                break
            
        if not_found == True:
            for x in range(0, len(locations)):
                locations[x] = nodes.get(locations[x])[int(char)]
            num_steps += 1


print(num_steps)
