import re

input = open('input.txt', 'r')

lines = input.readlines()


nice = []
naughty = []

for line in lines:
    
    no_overlap = re.findall("([a-z][a-z]).*?\\1", line)
    overlap = re.findall("([a-z])([a-z])\\1", line)

    if len(no_overlap) >= 1 and len(overlap) >= 1:
        nice.append(line)
    


print(len(nice))