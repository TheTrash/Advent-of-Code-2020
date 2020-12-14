f = open('input.txt', 'r')
t = int(f.readline())
buss =[n for n in f.readline().split(",")]
stable =[int(n) for n in buss if n != "x"]
step=0
find = True
tmp=1


for i,line in enumerate(buss):
        if line == "x":
            continue
        while (step+i)%int(line):
            step+=tmp
        tmp*=int(line)

print(step)
