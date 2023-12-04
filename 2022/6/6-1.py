input = open('input.txt', 'r')

line = input.readline()


window = []

index = 0

for char in line:
    
    index += 1
    
    window.append(char)
    
    if len(window) > 4:
        window.pop(0)
    
    if len(window) == 4:
        
        
        unique_test = set(window)
        
        if len(unique_test) == 4:
            
               
               print(index)
               break
    
    
