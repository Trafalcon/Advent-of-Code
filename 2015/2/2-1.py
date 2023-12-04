input = open('input.txt', 'r')

lines = input.readlines()

nums = []

for line in lines:
    temp = line.split("x")
    num = []
    for x in temp:
        num.append(int(x))
    num.sort()
    nums.append(num)


total = 0

for num in nums:
    
    l = num[0]
    w = num[1]
    h = num[2]
    
    
    temp = (2*l*w) + (2*w*h) + (2*h*l) + (l*w)
    
    total += temp
    
    

print(total)
    
    