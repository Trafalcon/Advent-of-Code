input = open('input.txt', 'r')

lines = input.readlines()

red_limit = 12
green_limit = 13
blue_limit = 14


# strip leading info
stripped = []
for line in lines:
    index = line.find(" ", 5)
    line = line[index+1:-1]
    stripped.append(line)



# For each game

successes = []


for line in stripped:
    
    # Break game into each set
    sets = line.split(";")
    
    # Check each set for red, blue, and green
    success = True
    for x in sets:
        x = x.replace(" ", "")
        red = x.find("red")
        blue = x.find("blue")
        green = x.find("green")
        
        if red != -1:
            num = int(x[x.find(",", red-3)+1:red])
            
            if num > red_limit:
                success = False
            
        if blue != -1:
            num = int(x[x.find(",", blue-3)+1:blue])
            
            if num > blue_limit:
                success = False
        
        if green != -1:
            num = int(x[x.find(",", green-3)+1:green])
            
            if num > green_limit:
                success = False
    
    if success == True:
        successes.append(stripped.index(line)+1)



# Sum up successful games

total = 0

for x in successes:
    total += x
    



print(total)