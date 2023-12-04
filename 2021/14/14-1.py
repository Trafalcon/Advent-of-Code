from collections import Counter
import time

# Start
start = time.time()
input = open('input.txt', 'r')

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
    
    
# Iterate
step = 0

while step < 10:
    
    # Create list of pairs in polymer
    pairNum = 0
    pairs = list(zip(polymer[:-1], polymer[1:]))
    for pair in pairs:
        pairs[pairNum] = ''.join(pair)
        pairNum += 1
        
    
    # Walk through rules for each pair IN ORDER
    pairNum = 0
    for pair in pairs:
        for rule in rules:
            if rule[0] == pair:
                pairs[pairNum] = pair[0] + rule[1] + pair[1]
                break
                
        pairNum += 1
    
    
    # Re-construct pairs into polymer chain for next step
    temp_polymer = ''
    pairNum = 0
    for pair in pairs:
        if pairNum == len(pairs)-1:
            temp_polymer += pair
            break
        else:
            temp_polymer += pair[0:2]
        
        pairNum += 1
    
    
    polymer = temp_polymer
    
    step += 1

#print(polymer)




# Count occurences of each element
collection = Counter(polymer)
print(collection)

maxCount = max(val for val in collection.values())
minCount = min(val for val in collection.values())

print(maxCount - minCount)

end = time.time()
print( "Time taken: " + str(end-start))







































