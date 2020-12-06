f = open("input.txt", "r")
l = [str(n).replace('\n', '') for n in f.readlines()]


start=3
s = 0
for i in range(0,len(l)):
    s = s+ l[i][(start*i)%m].count("#")

print(sum)