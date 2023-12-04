input = open('input.txt', 'r')

lines = input.readlines()

total = 0

# For each rucksack

for line in lines:
    
    
    # Split rucksack into 2 halves
    
    line = line[:-1]
    comp1 = line[:(int(len(line)/2))]
    comp2 = line[(int(len(line)/2)):]
    
    
    # Find unique characters in each compartment
    
    comp1 = set(comp1)
    comp2 = set(comp2)
    
    
    # Find common character
    
    value = comp1.intersection(comp2)
    value = value.pop()
    
    
    # Convert character to number - a-z -> 1-26, A-Z -> 27-52
    
    if value == value.lower():
        val = ord(value) - 96
        total += val
    else:
        val = ord(value) - 38
        total += val
        
print(total)