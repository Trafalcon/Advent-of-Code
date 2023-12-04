input = open('input.txt', 'r')

lines = input.readlines()

count = 0

# For each pair

for line in lines:
    
    # Break line down into 2 ranges
    
    line = line.strip('\n')
    line = line.split(',')
    
    range1 = line[0]
    range2 = line[1]
    
    range1 = range1.split('-')
    range2 = range2.split('-')
    
    range1[0] = int(range1[0])
    range1[1] = int(range1[1])
    range2[0] = int(range2[0])
    range2[1] = int(range2[1])
    
    # Compare each range to see if one overlaps the other
    
    # Bottom number overlaps
    
    if range1[0] <= range2[0] and range1[1] >= range2[0]:
        count += 1
               
    elif range2[0] <= range1[0] and range2[1] >= range1[0]:
        count += 1
        
        
    # Upper number overlaps

    elif range1[1] >= range2[1] and range1[0] <= range2[1]:
        count += 1
               
    elif range2[1] >= range1[1] and range2[0] <= range1[1]:
        count += 1



print(count)