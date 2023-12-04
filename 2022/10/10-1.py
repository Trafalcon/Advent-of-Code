def cycle_up(cycle, x, sig_list):
    
    cycle += 1
    if cycle - 20 == 0 or (cycle - 20) % 40 == 0:
        sig_list.append((cycle * x))
        
    return cycle, sig_list
        

input = open('input.txt', 'r')

lines = input.readlines()

x = 1
cycle = 0
sig_list = []


# CPU Instructions

for line in lines:
    
    line = line.strip('\n')
    line = line.split(' ')
    
    command = line[0]
    if command != "noop":
        val = int(line[1])
    
    if command == "addx":
        
        cycle, sig_list = cycle_up(cycle, x, sig_list)
        cycle, sig_list = cycle_up(cycle, x, sig_list)
        
        x += val
        
    else:
        
        cycle, sig_list = cycle_up(cycle, x, sig_list)




print(sig_list)

print(sum(sig_list))