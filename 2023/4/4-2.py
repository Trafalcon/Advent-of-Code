import re

input = open('input.txt', 'r')

lines = input.readlines()

num_cards = [0]*len(lines)

index = 0

while index < len(lines):
    
    num_cards[index] += 1
    line = lines[index]
    line = line.split(":")[1]
    winning, current = line.split("|")
    
    winning = set(re.findall("[0-9]+", winning))
    current = set(re.findall("[0-9]+", current))
    
    
    match = winning.intersection(current)
    
    temp_index = index
    
    for x in match:
        temp_index += 1
        num_cards[temp_index] += num_cards[index]

    index += 1




print(sum(num_cards))