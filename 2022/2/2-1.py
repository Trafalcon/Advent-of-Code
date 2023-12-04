input = open('input.txt', 'r')

lines = input.readlines()


total_score = 0

# Play RPS

for line in lines:
    
    # Select the moves ABC -> RPS, XYZ -> RPS
    
    enemy = line[0]
    you = line[2]
    
    round_score = 0
    
    if enemy == 'A' and you == 'X':
        round_score = 4
    elif enemy == 'A' and you == 'Y':
        round_score = 8
    elif enemy == 'A' and you == 'Z':
        round_score = 3
    elif enemy == 'B' and you == 'X':
        round_score = 1
    elif enemy == 'B' and you == 'Y':
        round_score = 5
    elif enemy == 'B' and you == 'Z':
        round_score = 9
    elif enemy == 'C' and you == 'X':
        round_score = 7
    elif enemy == 'C' and you == 'Y':
        round_score = 2
    elif enemy == 'C' and you == 'Z':
        round_score = 6
        
    total_score += round_score
    
    
print(total_score)
    