import re

input = open('input.txt', 'r')

lines = input.readlines()

matches = []

for line in lines:
    
    line = line.split(":")[1]
    winning, current = line.split("|")
    
    winning = set(re.findall("[0-9]+", winning))
    current = set(re.findall("[0-9]+", current))
    
    
    match = winning.intersection(current)
    matches.append(match)


total = 0
for match in matches:
    
    if len(match) > 0:
        temp = pow(2,len(match)-1)
        total += temp



print(total)