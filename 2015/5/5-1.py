import re

input = open('test.txt', 'r')

lines = input.readlines()


nice = []
naughty = []

for line in lines:
    
    vowels = re.search("([aeiou].*?)", line)
    print(vowels.groups())