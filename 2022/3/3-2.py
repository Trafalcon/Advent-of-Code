input = open('input.txt', 'r')

lines = input.readlines()

total = 0

# 3 rucksacks at a time

index = 0

while index < len(lines):
    
    bag1 = lines[index]
    bag1 = bag1[:-1]
    index += 1
    
    bag2 = lines[index]
    bag2 = bag2[:-1]
    index += 1
    
    bag3 = lines[index]
    bag3 = bag3[:-1]
    index += 1
    
    # Find unique characters in each bag
    
    bag1 = set(bag1)
    bag2 = set(bag2)
    bag3 = set(bag3)
    
    
    # Find common character between 3 rucksacks
    
    temp = bag1.intersection(bag2)
    value = temp.intersection(bag3)
    value = value.pop()
    
    
    # Convert character to number - a-z -> 1-26, A-Z -> 27-52
    
    if value == value.lower():
        val = ord(value) - 96
        total += val
    else:
        val = ord(value) - 38
        total += val
        
print(total)