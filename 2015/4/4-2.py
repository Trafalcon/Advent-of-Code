import hashlib

input = open('input.txt', 'r')

key = input.readline()


num = 0

while True:


    hash_input = key + str(num)
    
    h = hashlib.md5()
    
    h.update(bytes(hash_input, "utf-8"))
    
    output = h.hexdigest()
    
    check = output[:6]
    
    if check == "000000":
        break

    num += 1


print(num)
    