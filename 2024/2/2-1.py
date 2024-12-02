input = open('input.txt', 'r')

lines = input.readlines()

levels = []
safe = []

for line in lines:
    strings = line.split()
    temp = []
    for x in strings:
        temp.append(int(x))
    levels.append(temp)


for report in levels:
    flag = True
    
    inc = all(i < j for i, j in zip(report, report[1:]))
    dec = all(i > j for i, j in zip(report, report[1:]))
    
    if not inc and not dec:
        flag = False
    
    for x in (range(len(report)-1)):
        if (report[x] == report[x+1]) or (abs(report[x] - report[x+1]) > 3):
            flag = False
    safe.append(flag)


print(safe.count(True))