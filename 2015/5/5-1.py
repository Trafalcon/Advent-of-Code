import re

input = open('input.txt', 'r')

lines = input.readlines()


nice = []
naughty = []

for line in lines:
    
    vowels = re.findall("([aeiou].*?)", line)
    consecutive = re.findall("([a-z])\\1", line)
    bad = re.findall("ab|cd|pq|xy", line)
    
    if len(bad) >= 1:
        naughty.append(line)
        continue
    
    elif len(vowels) >= 3 and len(consecutive) >= 1:
        nice.append(line)
    


print(len(nice))