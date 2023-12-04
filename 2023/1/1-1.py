input = open('input.txt', 'r')

lines = input.readlines()


num = []


for line in lines:
    temp = ""
    for i in line:
        if i.isdigit():
            temp += i
    temp = temp[0] + temp[-1]
    num.append(int(temp))



sum = 0

for x in num:
    sum += x



print(sum)