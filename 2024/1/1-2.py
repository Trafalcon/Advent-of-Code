input = open('input.txt', 'r')

lines = input.readlines()


num = []


left = []
right = []
score = 0

for line in lines:
    temp = line.split()
    left.append(temp[0])
    right.append(temp[1])


for val in left:
    occur = right.count(val)
    score += int(val) * occur




print(score)