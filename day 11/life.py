import copy
f = open('input.txt', 'r').readlines()
l = [[el for el in row.strip()] for row in f]

print(l)

def neigh(x, y):
    c = 0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if( -1 < i < (len(om))  and -1 < j < (len(om[x])) and (x,y) != (i,j)):
                #print(x,y)
                if(om[i][j] == "#"):
                    c+=1
    return c

step = 0

om=copy.deepcopy(l)
while True:
    nm=[]
    for x,line in enumerate(om):
        r=[]
        for y,seat in enumerate(line):
            t = neigh(x,y)
            if( t == 0 and om[x][y] == 'L'):
                r.append('#')
            elif( t >= 4 and om[x][y] == '#' ):
                r.append('L')
            else:
                r.append(om[x][y])
            
        nm.append(r)
    

    
    if om == nm:
        break
    om=copy.deepcopy(nm)
    step+=1
print(step)

count = 0
for i, line in enumerate(om):
    for j, seat in enumerate(line):
        if(seat == '#'):
            count+=1

print(count)