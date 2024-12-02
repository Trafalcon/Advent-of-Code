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


# Starting location of AAA
location = "AAA"

# Read instructions to find next node until "ZZZ" is found
num_steps = 0

while location != "ZZZ":
    
    for char in instructions:
        if location != "ZZZ":
        
            location = nodes.get(location)[int(char)]
            num_steps += 1


print(num_steps)