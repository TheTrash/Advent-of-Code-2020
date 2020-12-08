import sys
row = int(sys.argv[1])

def read(command):
    global acc,p, cl
    if command[0] == "nop":
        p+=1
    if command[0] == "jmp":
        p+=int(command[1])
    if command[0] == "acc":
        acc+=int(command[1])
        p+=1

f = open("input.txt", "r")
l = [n.split() for n in f.readlines()]
cl = []

#This needed for the array generation
#np = [n for n in range(len(l)-1) if (l[n][0] == "nop" or l[n][0]=="jmp") ]
#print(np)

#print(l[row])
if l[row][0] == "nop":
    l[row][0] = "jmp"
else:
    l[row][0] = "nop"
#print(l[row])

acc=0 #accumulator
p=0 #program counter

while True :
    if p == 648:
       print("program counter",p,"command:",l[p], "acc:",acc)
       break
    #print(p,":",l[p], "acc:",acc)
    elif p not in cl:
       cl.append(p)
    else:
        #print(cl)
        break
    read(l[p])
