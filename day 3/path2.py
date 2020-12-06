def move(a):
    x,y = a
    s=0
    for i in range(n):
        if y*i < n:
            s += l[(y*i)][(x*i)%m].count("#")
    return s



f = open("input.txt", "r")
l = [str(n).replace('\n', '') for n in f.readlines()]
s, mu = (0,1)
m = len(l[0])
n = len(l)

path = [(1,1),(3,1),(5,1),(7,1),(1,2)]

for a in path:
    mu *= move(a)

print(mu)
