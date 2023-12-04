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

maxes = []


for line in stripped:
    
    red_max = 0
    blue_max = 0
    green_max = 0
    
    # Break game into each set
    sets = line.split(";")
    
    # Check each set for red, blue, and green for maxes

    for x in sets:
        x = x.replace(" ", "")
        red = x.find("red")
        blue = x.find("blue")
        green = x.find("green")
        
        if red != -1:
            num = int(x[x.find(",", red-3)+1:red])
            
            if num > red_max:
                red_max = num
            
        if blue != -1:
            num = int(x[x.find(",", blue-3)+1:blue])
            
            if num > blue_max:
                blue_max = num
        
        if green != -1:
            num = int(x[x.find(",", green-3)+1:green])
            
            if num > green_max:
                green_max = num
    
    maxes.append([red_max,blue_max,green_max])
    



# Sum up successful games

total = 0
  
for x in maxes:
    total += (x[0] * x[1] * x[2])


print(total)