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

acc=0 #accumulator
p=0 #program counter

while True :
    # print(p,":",l[p], "acc:",acc) #here is for debug
    if p not in cl:
       cl.append(p)
    else:
        print("program counter",p,"command:",l[p], "acc:",acc)
        break
    read(l[p])