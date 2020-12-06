import math
f = open("input.txt", "r")
l = [n for n in f.readlines()]

max = 0

for phrase in l:
    row = 127
    col = 7
    ir = 0
    ic = 0
    for letter in phrase: 
        if(letter == "F"):
            row = math.floor((ir + row)/2) #down
        elif(letter == "B"): 
            ir = math.ceil((row + ir)/2) #up
        elif(letter == "L"):
            col = math.floor((ic + col)/2)   #down
        elif(letter == "R"):
            ic = math.ceil((col + ic)/2)   #up

    print(ir, row, ic, col)
    res = ((row * 8)+col)
    if max < res:
        max = res
    print(res)    
print("max: ",max)