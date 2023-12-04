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
    
    
    temp = (l+l+w+w) + (l*w*h)
    
    total += temp
    
    

print(total)
    
    