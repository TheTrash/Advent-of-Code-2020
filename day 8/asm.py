def read(command):
    global i,n, cl
    if command[0] == "nop":
        i+=0
        n+=1
    if command[0] == "jmp":
        i+=1 
        n+=int(command[1])
    if command[0] == "acc":
        i+=int(command[1])
        n+=1

    return n,i

f = open("input.txt", "r")
l = [n.split() for n in f.readlines()]
cl = []
i=0 #accumulator
n=0 #program counter
while True :
    print(l[n])
    if n not in cl:
        cl.append(n)
    else:
        print(cl)
        break
    print(read(l[n]))

