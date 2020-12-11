f = open("input.txt", "r")
l = [int(n) for n in f.readlines()]
l.sort()
j,t,u = (0,1,0)
for a in l:
    tmp = a - j
    if( tmp == 1):
        j=a
        u+=1
        print("jmp 1")
    elif ( tmp <= 3):
        j=a
        t+=1
        print("jmp 3")
    print(j)

print(u,t,(u*t))
