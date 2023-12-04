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
    
    
# Find 3 largest elf bags and index of them

sub_totals = []
for num in all_totals:
    sub_totals.append(num)

max_bag1 = max(sub_totals)

sub_totals.remove(max_bag1)

max_bag2 = max(sub_totals)

sub_totals.remove(max_bag2)

max_bag3 = max(sub_totals)



print("The 1st largest bag is elf " + str(all_totals.index(max_bag1) + 1) + "'s, which has a value of " + str(max_bag1))
print("The 2nd largest bag is elf " + str(all_totals.index(max_bag2) + 1) + "'s, which has a value of " + str(max_bag2))
print("The 3rd largest bag is elf " + str(all_totals.index(max_bag3) + 1) + "'s, which has a value of " + str(max_bag3))
print("The total value of these 3 bags is: " + str(max_bag1+max_bag2+max_bag3))