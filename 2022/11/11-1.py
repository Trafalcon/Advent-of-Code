input = open('input.txt', 'r')

lines = input.readlines()


item_list = []
op_list = []
test_list = []
true_list = []
false_list = []
inspect_list = []


cur_round = 0
max_round = 20

op = {'+': lambda x, y: x + y,
      '*': lambda x, y: x * y}


# Split input by Monkey
for line in lines:
    line = line.strip('\n')
    line = line.split(' ' )
    print(len(line))
    
    if (len(line)) == 1:
        continue

    if line[0] == "Monkey":
        index = int(line[1][:1])
        
    elif line[2] == "Starting":
        items = line[4:]
        temp = []
        
        # Insert items into item_list at index Monkey
        for item in items:
            item = item.strip(',')
            item = int(item)
            temp.append(item)
        
        items = temp
        item_list.append(items)
    
    elif line[2] == "Operation:":
        items = line[6:]
        items[1] = items[1]
        op_list.append(items)
        
    elif line[2] == "Test:":
        test_list.append(int(line[5]))
    
    elif line[5] == "true:":
        true_list.append(int(line[-1]))
    
    elif line[5] == "false:":
        false_list.append(int(line[-1]))
        



# Time to do something with the input

# Initialize list to track number of inspects
inspect_list = [0] * len(false_list)

# Rounds

while cur_round < max_round:
    
    # Start with first monkey
    
    cur_monk = 0
    
    while cur_monk < len(false_list):
        
        # Make current monkey item list to hold items
        
        cur_list = []
        for item in item_list[cur_monk]:
            cur_list.append(item)
            
            
        # For each item monkey holds
        
        for item in cur_list:
            
            item_list[cur_monk].remove(item)
            
            # Inspect item, performing Operation
            inspect_list[cur_monk] += 1
            
            if op_list[cur_monk][1] == 'old':
                item = op[op_list[cur_monk][0]](item, item)
            
            else:
                item = op[op_list[cur_monk][0]](item,int(op_list[cur_monk][1]))
                
            item = item // 3
            
            if item % test_list[cur_monk] == 0:
                item_list[true_list[cur_monk]].append(item)
                
            else:
                item_list[false_list[cur_monk]].append(item)
        
            
        
        
        cur_monk += 1
    
    
    
    
    
    cur_round += 1
    print(item_list)




inspect_list.sort(reverse=True)

print(str(inspect_list[0]*inspect_list[1]))
























