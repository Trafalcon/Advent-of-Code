input = open('input.txt', 'r')

lines = input.readlines()


num = []


left = []
right = []
sums = []

for line in lines:
    temp = line.split()
    left.append(temp[0])
    right.append(temp[1])


left.sort()
right.sort()

for x in range(len(left)):
    temp = int(right[x]) - int(left[x])
    sums.append(abs(temp))




print(sum(sums))