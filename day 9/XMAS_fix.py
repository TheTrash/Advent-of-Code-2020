f = open("input.txt", "r")
l = [int(n) for n in f.readlines()]



print(l[561])
for n in range(0,561):
    i=0
    tmp = l[561]
    li = []
    print(n,"-->",l[n])
    while tmp > 0:
        tmp -= l[n+i]
        li.append(l[n+i])
        print(tmp,i)
        i+=1
    if(tmp == 0):
        print("n",n,"i",i,"tmp",tmp)
        print(min(li),max(li),min(li)+max(li))
        break
