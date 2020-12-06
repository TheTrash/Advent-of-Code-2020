import math

def fi(position):
    row = 127
    col = 7
    ir = 0
    ic = 0
    for letter in position: 
        if(letter == "F"):
            row = math.floor((ir + row)/2) #down
        elif(letter == "B"): 
            ir = math.ceil((row + ir)/2) #up
        elif(letter == "L"):
            col = math.floor((ic + col)/2)   #down
        elif(letter == "R"):
            ic = math.ceil((col + ic)/2)   #up

    #print(ir, row, ic, col)
    res = ((row * 8)+col)
    return res

f = open("input.txt", "r")
l = [n for n in f.readlines()]

seats = [int(fi(n)) for n in l ]

seats.sort()
print(seats)
for n in range(seats[0],seats[-1]):
    if n != int(seats[n-13]):
        print(n)
        break
