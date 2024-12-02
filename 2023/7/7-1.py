input = open('input.txt', 'r')

lines = input.readlines()

hands = []

for line in lines:
    line = line.split()
    hands.append((line[0], int(line[1])))
    

# Build out card type comparison

def rank(hand):
    temp = hand[0]
    
    cards = {item: temp.count(item) for item in temp}

    # Check for 5 of a kind
    if 5 in cards.values():
        return 5
    elif 4 in cards.values():
        return 4
    elif 3 in cards.values() and 2 in cards.values():
        return 3
    elif 3 in cards.values():
        return 2
    elif list(cards.values()).count(2) == 2:
        return 1
    elif 2 in cards.values():
        return 0
    else:
        return -1


def suit(char):
    if char == "A":
        return 14
    elif char == "K":
        return 13
    elif char == "Q":
        return 12
    elif char == "J":
        return 11
    elif char == "T":
        return 10
    elif char == "9":
        return 9
    elif char == "8":
        return 8
    elif char == "7":
        return 7
    elif char == "6":
        return 6
    elif char == "5":
        return 5
    elif char == "4":
        return 4
    elif char == "3":
        return 3
    elif char == "2":
        return 2



hands = sorted(hands, key=lambda e: (rank(e), suit(e[0][0]), suit(e[0][1]), suit(e[0][2]), suit(e[0][3]), suit(e[0][4])))

print(hands)



total = 0

for hand in hands:
    
    total += (hands.index(hand)+1) * hand[1]


print(total)