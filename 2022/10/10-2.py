def cycle_up(cycle, x, sig_list, CRT):
    
    if (x-1) == (cycle % 40) or x == (cycle % 40) or (x+1) == (cycle % 40):
        CRT.append('#')
    
    else:
        CRT.append('.')
    
    cycle += 1
    if cycle - 20 == 0 or (cycle - 20) % 40 == 0:
        sig_list.append((cycle * x))
        
    return cycle, sig_list, CRT
        

input = open('input.txt', 'r')

lines = input.readlines()

x = 1
cycle = 0
sig_list = []
CRT = []


# CPU Instructions

for line in lines:
    
    line = line.strip('\n')
    line = line.split(' ')
    
    command = line[0]
    if command != "noop":
        val = int(line[1])
        
    
    if command == "addx":
        
        cycle, sig_list, CRT = cycle_up(cycle, x, sig_list, CRT)
        cycle, sig_list, CRT = cycle_up(cycle, x, sig_list, CRT)
        
        x += val
        
    else:
        
        cycle, sig_list, CRT = cycle_up(cycle, x, sig_list, CRT)
        




start = 0
end = 40

while end < len(CRT)+1:
    print(''.join(CRT[start:end]))
    start += 40
    end += 40