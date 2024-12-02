import itertools

input = open('input.txt', 'r')

lines = input.readlines()

levels = []
safe = []

for line in lines:
    strings = line.split()
    temp = []
    for x in strings:
        temp.append(int(x))
    test = []
    test = list(itertools.combinations(temp, len(temp)-1))
    levels.append(test)


for report_set in levels:
    set_flag = False
    
    for report in report_set:
        flag = True
    
        inc = all(i < j for i, j in zip(report, report[1:]))
        dec = all(i > j for i, j in zip(report, report[1:]))
        
        if not inc and not dec:
            flag = False
        
        for x in (range(len(report)-1)):
            if (report[x] == report[x+1]) or (abs(report[x] - report[x+1]) > 3):
                flag = False
        if not set_flag and flag:
            set_flag = True
            break
        
    safe.append(set_flag)


print(safe.count(True))