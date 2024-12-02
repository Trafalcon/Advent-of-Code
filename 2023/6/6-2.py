input = open('input.txt', 'r')

lines = input.readlines()

time = int(lines[0].split(":")[1].strip())

distance = int(lines[1].split(":")[1].strip())


# Find lower bound where result > distance

lower_hold = 0
lower = False

while lower == False:
    
    speed = lower_hold * (time-lower_hold)
    
    if speed > distance:
        lower = True
    
    if lower == False:
        lower_hold += 1


# Find upper bound where result > distance


upper_hold = time
upper = False

while upper == False:
    
    speed = upper_hold * (time-upper_hold)
    
    if speed > distance:
        upper = True
    
    if upper == False:
        upper_hold -= 1

    

print(upper_hold-lower_hold+1)

