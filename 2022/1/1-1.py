input = open('input.txt', 'r')

lines = input.readlines()

all_bags = []
bag = []

# Creating inventories for all elves

for line in lines:
    if line != '\n':
        bag.append(int(line))
    else:
        all_bags.append(bag)
        bag = []
if len(bag) > 0:
    all_bags.append(bag)
    bag = []
    
    
# Sum up each elf's inventory

all_totals = []
total = 0

for bag in all_bags:
    for num in bag:
        total += num
    all_totals.append(total)
    total = 0
    
    
# Find largest elf bag and index of it

max_bag = max(all_totals)
print("The largest bag is elf " + str(all_totals.index(max_bag) + 1) + "'s, which has a value of " + str(max_bag))