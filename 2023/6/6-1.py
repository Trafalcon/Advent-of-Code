input = open('input.txt', 'r')

lines = input.readlines()

times = lines[0].split(":")[1].split()

distances = lines[1].split(":")[1].split()


wins = [0] * len(times)


for time, distance, i in zip(times, distances, range(0,len(times))):
    
    time = int(time)
    distance = int(distance)
    hold = 0
    
    while hold <= int(time):
        
        speed = hold * (time-hold)
        
        if speed > distance:
            wins[i] += 1
        
        
        hold +=1
    

total = 1

for win in wins:
    total *= win

print(total)