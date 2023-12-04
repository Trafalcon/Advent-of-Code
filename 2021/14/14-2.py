from collections import Counter
import time
import math
        

# In a dict, keep track of each possible TYPE of pair, not individual pairs
# EXAMPLE: NN: 5 - means 5 occurences of NN pair, so next step adds 5 B's
# We know that B in the center will create 5 new NB & 5 BN pairs, which are then added to dict for next step



# Start
start = time.time()
file = 'input.txt'
input = open(file, 'r')
lines = input.readlines()

# Formatting input data
polymer = []
rules = []
breakPoint = False

for line in lines:
    if line == '\n':
        breakPoint = True
        continue
    
    if not breakPoint:
        polymer = line.strip('\n')
    else:
        rules.append(line.strip('\n'))
        
        
ruleNum = 0
for rule in rules:
    rule = rule.partition(' -> ')
    rules[ruleNum] = [rule[0], rule[2]]
    ruleNum += 1
    

# Turn rules into dictionary of key:value pairs
rules = dict(rules)


# Create count dict to track count of each letter (adding H since it doesn't exist at the start)
count = dict(Counter(polymer))
if file =='test.txt':
    count.update({'H':0})
else:
    count.update({'N':0})
for key in count.keys():
    count[key] = 0


# Make pairDict from rules
pairs = dict.fromkeys(rules)
for key in pairs:
    pairs[key] = 0

# Add in starting pairs to pairDict
startingPairs = list(zip(polymer[:-1], polymer[1:]))
for pair in startingPairs:
    index = pair[0] + pair[1]
    pairs[index] +=1


# Iterate
step = 0


while step < 40:
    
    # Create temp_pairs to hold temp updates
    temp_pairs = {}
    for key in pairs.keys():
        temp_pairs.update({key: 0})
    
    # update step
    for rule in rules.keys():
        num = pairs[rule]
        first = rule[0]
        second = rule[1]
        add = rules[rule]
        first += add
        second = add + second
        temp_pairs[first] += num
        temp_pairs[second] += num
            
    
    
    # Apply temp_pairs changes to pair
    pairs = temp_pairs
    
    
    # Print pairs
    #print(pairs)
    
    # Increment step counter
    step += 1


# Find count of specific character
for key in pairs.keys():
    first = key[0]
    second = key[1]
    count[first] += pairs[key]
    count[second] += pairs[key]
    

for key in count.keys():
    count[key] = count[key]/2
    count[key] = math.ceil(count[key])

end = time.time()
#print( "Time taken for", step, "steps: ",str(end-start))

maxNum = max(val for val in count.values())
minNum = min(val for val in count.values())


for key in count.keys():
    print(key, ' : ', count[key])
    
print(maxNum - minNum - 1)







































