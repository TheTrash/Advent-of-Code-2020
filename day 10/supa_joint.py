from functools import lru_cache
l = [int(n) for n in open("input.txt", "r").readlines()]
#add first and last adapter 
l.append(min(l)-1)
l.append(max(l)+3)
#sort my magic collection
l.sort()

path = 0

@lru_cache()
def child(node):
    i=l.index(node)
    c=[ t for t in l[i:i+4] if (1 <= (t - node) and (t-node) <= 3) ]
    
    return c

@lru_cache()
def visit(node):
    path = 0
    if node == l[-1]:
        return 1 #"the path end here"
    for n in child(node):
        path += visit(n)

    return path

print("paths:",visit(l[0]))