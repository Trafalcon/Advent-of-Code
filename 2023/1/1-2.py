input = open('input.txt', 'r')

lines = input.readlines()



index = 0
for full_line in lines:
    
    line = ""
    temp = ""
    end = False
    for char in full_line:
        line += char
        if char.isdigit():
            temp += char
            end = True
            break
            
        if line.replace("one","1")!=line:
            temp += "1"
            end = True
            break
        if line.replace("two","2")!=line:
            temp += "2"
            end = True
            break
        if line.replace("three","3")!=line:
            temp += "3"
            end = True
            break
        if line.replace("four","4")!=line:
            temp += "4"
            end = True
            break
        if line.replace("five","5")!=line:
            temp += "5"
            end = True
            break
        if line.replace("six","6")!=line:
            temp += "6"
            end = True
            break
        if line.replace("seven","7")!=line:
            temp += "7"
            end = True
            break
        if line.replace("eight","8")!=line:
            temp += "8"
            end = True
            break
        if line.replace("nine","9")!=line:
            temp += "9"
            end = True
            break
     
        
    line = ""
    end = False
    for char in reversed(full_line):
        line = char + line
        if char.isdigit():
            temp += char
            end = True
            break
            
        if line.replace("one","1")!=line:
            temp += "1"
            end = True
            break
        if line.replace("two","2")!=line:
            temp += "2"
            end = True
            break
        if line.replace("three","3")!=line:
            temp += "3"
            end = True
            break
        if line.replace("four","4")!=line:
            temp += "4"
            end = True
            break
        if line.replace("five","5")!=line:
            temp += "5"
            end = True
            break
        if line.replace("six","6")!=line:
            temp += "6"
            end = True
            break
        if line.replace("seven","7")!=line:
            temp += "7"
            end = True
            break
        if line.replace("eight","8")!=line:
            temp += "8"
            end = True
            break
        if line.replace("nine","9")!=line:
            temp += "9"
            end = True
            break
        
    
    lines[index] = int(temp)
    index += 1









sum = 0

for x in lines:
    sum += x



print(sum)