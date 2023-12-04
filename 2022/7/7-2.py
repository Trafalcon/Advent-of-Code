input = open('input.txt', 'r')

lines = input.readlines()


AVAILABLE_SPACE = 70000000
REQUIRED_UNUSED = 30000000


index = 0

file_dict = {}

current_dir = '/'

while index < len(lines):
    
    line = lines[index].strip('\n')
    output = line.split(' ')
    
    index += 1
    
    # If "$", then command
    
    if output[0] == '$':
        
        # cd - Change Directory
        if output[1] == 'cd':
            
            print('cd')
            
            if output[2] == '/':
                current_dir
            
            elif output[2] == '..':
                if len(current_dir) > 1:
                    current_dir = current_dir[:current_dir.rindex('/')]
                    current_dir = current_dir[:current_dir.rindex('/')+1]
                
            else:
                current_dir += output[2] + "/"
        
        
        
        # ls - List current directory and files
        if output[1] == 'ls':
            
            print('ls')
            
            while True:
                
                if index < len(lines):
                    line = lines[index]
                    
                    temp = line.strip('\n')
                    temp = temp.split(' ')
                    if temp[0] != 'dir' and temp[0] != '$':
                        filesize = int(temp[0])
                        filename = temp[1]
                        file_dict.update({current_dir + filename: filesize})
                    
                else:
                    break
                    
                index += 1
                    
                if line[0] != '$':
                    print(line)
                    
                    
                else:
                    break

            index -= 1
    
    

# Calculate directory size from file_dict

dir_dict = {}

for key in file_dict.keys():
    
    filesize = file_dict.get(key)
    
    directory = key[:key.rindex('/')+1]
    
    while directory != '':
    
        test = dir_dict.get(directory)
        
        if test is None:
        
            dir_dict.update({directory: filesize})
        
        else:
            
            dir_dict.update({directory: filesize + dir_dict.get(directory)})
        
        if directory == '/':
            directory = ''
        else:
            directory = directory[:directory.rindex('/')]
            directory = directory[:directory.rindex('/')+1]






# How much space is used - size of '/' directory

USED_SPACE = dir_dict.get('/')

CURRENT_UNUSED = AVAILABLE_SPACE - USED_SPACE

SPACE_TO_DELETE = REQUIRED_UNUSED - CURRENT_UNUSED

print(USED_SPACE)
print(SPACE_TO_DELETE)

values = list(dir_dict.values())

potentials = []

values.sort(reverse=True)

for value in values:
    if value >= SPACE_TO_DELETE:
        potentials.append(value)
    else:
        break


print(potentials[len(potentials)-1])

















