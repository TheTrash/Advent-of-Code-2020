def find_bus(id,buss):
    for i in range(id,id+buss[-1]+1):
        for n in buss:
            print(i, "->",n,":", i%n)
            if(i%n == 0):
                print(i)
                find = False
                return n, i


f = open('input.txt', 'r')
id= int(f.readline())
buss =[int(n) for n in f.readline().split(",") if n != "x"]
buss.sort()
print(id,buss)
#c correct bus, timestamp
c, t = find_bus(id,buss)

print(c,t)

res = (t - id) * c
print(res)




